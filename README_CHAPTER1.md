# Chapter 1 Python Distilled 

## Python On the Command Line
To use Python on the command line, just type Python.
This will allow you to use Python as a calculator, for example.  

Use the '_' character to use the last variable in memory to continue with calculations.

It is common to use #! to specify the interpreter on the first line of a program, as below:
#!/usr/bin/env python3 

## Debugging 
In VSCode, use the Debugging icon on the left hand side, or press F5.

## Indentation
Common to use 4 spaces for indentation.  

## True and False
A value is considered false if it is literally False, None, numerically zero, or empty.  Otherwise it's considered true.  

## Increment/Decrement
x = x + 1   # Can be written x += 1
y *= n      # Can be written y*=n  

Note, there are no x++ or y-- operators in Python.  

## Conditions and Control Flow
The 'while' 'if' and 'else' statements are used for looping and conditional code execution.  Use 'elif' for multiple test cases.

Use 'break' to break out of a loop.
Use 'continue' to move back up to the start of the loop.


## Use the walrus operator := for assignment and conditional.

## Strings
Strings can be enclosed in single, double or triple quotes.
Triple quoted strings are useful to allow strings over multiple lines.  

## Exceptions
When an exception occurs, the program resumes in exactly the position AFTER the except block.  The program does not return to the location where the exception occurred.  

Use `raise` to raise an exception.  

Typically, can use the `with` statement for resource management, to simplify complex try/except statements.  

## Program termination
Force a program to quit either using:
`rasie SystemExit()  # Exit with no error message `
`raise SystemExit("Something is wrong")  # Exit with error message`

Can use the atexit module to perform specific cleanup operations.  

import atexit

connection = open_connection('google.com')

def cleanup():
  print "Going away..."
  close_connection(connection)

atexit.register(cleanup)

## Objects and Classes
The dir() function lists the methods available on an object.  It is a useful tool for interactive experimentation when no fancy IDE is available.

You will see special methods that begin and end with double underscores, e.g. items.__add__([73, 101])

