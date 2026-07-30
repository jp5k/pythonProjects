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

## Imports
If the import statemnet fails with an ImportError exception, you need to check a few things in your environment.  Check the directories listed on sys.path (using REPL), if your file isn't saved in one of those directories, Python won't be able to find it.  

Can use `as` to import a module under a different name, e.g. 
`import readport as rp`

As with objects, the dir() function lists the contents of a module.  It is as useful tool for interactive experimentation.
`import scripts.fundamentals.lists`
`dir(scripts.fundamentals.lists)`

See https.pypi.org for a vast array of 3rd party modules that can be installed to solve almost any imaginable task.  

## Package structure 
Organise Python projects into the following structure.

Ensure you include the __init__.py file, which may be empty.  Once you've done this, you should be able to make nested import statements.  

You can use a package-relative import like this:
`from . import readport`
This has the benefit of not hardcoding the package name.  This makes it easier to later rename a package or move it around within your project.  

## Structuring an application
Typical to have the following structure:

tutorial-project/
  tutorial/
      __init__.py
      readport.py
      pcost.py
      stack.py
      ...
  tests/
      test_stack.py
      test_pcost.py
      ...
  examples/
      sample.py
      ...
  doc/
      tutorial.txt
      ...

## Third party packages
Python Package Index (https://pypi.org) has a large libray of contributed packages.  To install a third party package, use a command such as pip:
`python3 -m pip install somepackage`

Installed packages are placed into a special site-packages directory that you can find if you inspect the value of sys.path.  If you need to find out where package comes from, inspect the __file__ attribute of a package after importing it:
`import pandas`
`pandas.__file__`

To make a sandbox where you can install packages and work without worrying about breaking anything, create a virtual environment:
`python3 -m venv myproject`

This will set up a dedicated Python installation for you in a directory called myproject/.  Within that directory, you'll find an interpreter executable and library where you can safely install packages.  For example, if you run `myproject/bin/python3`, you'll get an interpreter configured for your personal use.  You can install packages into this interpreter without worrying about breaking any part of the default Python installation.  To install a package, use pip as before but make sure to specify the correct interpreter:
`./myproject/bin/python3 -m pip install somepackage`

