"""
Composition

Covers building a class out of another object instead of inheriting
from it. scripts/fundamentals/inheritance.py's MyStack *is a* Stack
(`class MyStack(Stack):`) -- it inherits Stack's methods directly, and
`isinstance(MyStack(), Stack)` is True. Calculator below takes a
different approach: it *has a* Stack, stored as a private attribute,
and defines its own push/pop methods that simply forward to that
internal Stack's push/pop. Calculator is not a Stack at all --
`isinstance(Calculator(), Stack)` is False -- it just uses one
internally to get LIFO storage without writing that logic itself. This
"has-a instead of is-a" relationship is called composition, and it's
often preferred over inheritance when a class wants to *reuse* another
class's behaviour without exposing itself as being interchangeable
with it, or without inheriting parts of that class's interface it
doesn't want.
"""

from scripts.fundamentals.objects_and_classes import Stack


class Calculator:
    """A stack-based (RPN-style) calculator: push operands, then combine them.

    e.g. to compute 3 + 4: push(3), push(4), add(), pop() -> 7.
    """

    def __init__(self):
        # The Stack here is an internal implementation detail, not
        # something Calculator exposes to its callers -- hence the
        # single leading underscore, the same "this is private, don't
        # touch it directly" convention used for Stack's own _items.
        # A caller of Calculator never sees this Stack object or
        # imports the Stack class themselves; they only ever call
        # Calculator's own push/pop/add/mul/sub/div methods. Swapping
        # this out for a different LIFO implementation later wouldn't
        # change Calculator's public interface at all.
        self._stack = Stack()

    def push(self, item):
        """Push a number onto the calculator's internal stack.

        This is composition's delegation pattern in miniature:
        Calculator doesn't inherit push from Stack (it isn't a
        subclass), so it defines its own push method -- with whatever
        behaviour it wants -- and that method's entire job here is to
        forward the call on to the internal Stack's push. Compare this
        to MyStack in inheritance.py, which gets push for free just by
        being declared `class MyStack(Stack):`; Calculator has to
        spell out the forwarding itself because it isn't a Stack.
        """
        self._stack.push(item)

    def pop(self):
        """Pop and return the top number from the calculator's internal stack."""
        return self._stack.pop()

    def add(self):
        """Pop the top two numbers, push their sum.

        Addition doesn't care which operand was pushed first, so the
        two pop() calls can be combined directly.
        """
        self.push(self.pop() + self.pop())

    def mul(self):
        """Pop the top two numbers, push their product.

        Like add(), multiplication doesn't depend on operand order.
        """
        self.push(self.pop() * self.pop())

    def sub(self):
        """Pop the top two numbers, push (first pushed) - (second pushed).

        Unlike add()/mul(), subtraction depends on order, so `right`
        (whichever number is on top -- the *second* one pushed) has to
        be captured in its own variable before the first pop() result
        is available to subtract it from. E.g. push(10), push(3),
        sub() computes 10 - 3, not 3 - 10.
        """
        right = self.pop()
        self.push(self.pop() - right)

    def div(self):
        """Pop the top two numbers, push (first pushed) / (second pushed).

        Same order-sensitivity as sub(): push(20), push(4), div()
        computes 20 / 4, not 4 / 20.
        """
        right = self.pop()
        self.push(self.pop() / right)


if __name__ == "__main__":
    # A quick, human-readable demo. Run as a module from the repo root:
    #   python -m scripts.fundamentals.composition
    #
    # (Not `python scripts/fundamentals/composition.py` -- see the note
    # in inheritance.py's __main__ block for why the direct path form
    # doesn't work once a script imports another scripts.* module.)

    c = Calculator()

    c.push(3)
    c.push(4)
    c.add()
    print(f"3 + 4 = {c.pop()}")

    c.push(10)
    c.push(3)
    c.sub()
    print(f"10 - 3 = {c.pop()}")

    c.push(6)
    c.push(7)
    c.mul()
    print(f"6 * 7 = {c.pop()}")

    c.push(20)
    c.push(4)
    c.div()
    print(f"20 / 4 = {c.pop()}")

    # Composition vs. inheritance, made concrete: Calculator uses a
    # Stack internally, but it is not one.
    print(f"isinstance(c, Stack) = {isinstance(c, Stack)}")
