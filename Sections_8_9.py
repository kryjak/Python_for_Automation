"""
A module is a file with definitions and functions. It can contain functions, classes and variables.
We define a module so that it can be used across many files.
For example, we can define a simple module 'mymodule_8.py' which contains some user-defined value.
Third-party modules can be obtained with 'pip install module'
"""

import sys
import getpass
import platform
import math  # can also redefine the name: import math as m
# from math import *  # Another way of importing - can specify particular functions
# In this case, we can do pow(i, j) instead of math.pow(i, j)
import mymodule_8  # Imported without .py !  # Needs to be in the same directory

print(mymodule_8.my_value)  # The notation for calling a function from a module is module.function
print(math.pi)

# print(help("modules"))  # Note quotation marks
# print(help(math))  # No quotation marks
# print(dir(math))  # No quotation marks

"""
----------------------------- PLATFORM MODULE -----------------------------------
The platform module is used to access the underlying platform's data such as hardware, OS and interpreter data
"""
# print(help("platform"))
print(dir(platform))
print(f"system {platform.system()}")
print(f"python version {platform.python_version()}")
print(f"python version tuple {platform.python_version_tuple()}")
print(f"machine {platform.machine()}")
print(f"release {platform.release()}")
print(f"platform {platform.platform()}")
print(f"architecture {platform.architecture()}")
print(f"processor {platform.processor()}")
print(f"node {platform.node()}")
print(f"uname {platform.uname()}")

"""
----------------------------- GETPASS MODULE -----------------------------------
The getpass module is used to enter and handle passwords without echoing
Note the errors: this code should be run from the terminal, not an IDE
"""
# print(dir(getpass))
# password = getpass.getpass(prompt='Please enter your password: ')
# # Note the error: this code should be run from the terminal, not an IDE
# print(f"The entered password is {password}")

"""
----------------------------- SYS MODULE -----------------------------------
The sys module is used to work with python runtime environment
"""
print(dir(platform))
print(f"platform {sys.platform}")  # Note the lack of brackets - here 'platform' is a variable, not a function
print(f"version {sys.version}")
print(f"version info {sys.version_info}")
print(f"modules {sys.modules}")
print(f"path {sys.path}")

# sys.exit()  # Stop the interpreter
# print("Print after exiting?")

"""
sys.argv returns a list of command line arguments passed to a Python script
If we run from the terminal:
python script.py input 37 "test"
['Section_8.py', 'input', '37', 'test']  # Note that everything is understood as a string
where input, 37 and "test" are the so-called command line arguments
argv[0] is the script pathname

Note the errors: this code should be run from the terminal, not an IDE
"""

# my_str = eval(input("Enter your string: "))
# action = input("Enter your action (upper/lower/title): ")

# when running from the terminal, use command line arguments:
# python3 Section_8.py "sTriNg" upper

if len(sys.argv) - 1 != 2:
    print(f"sys.argv: {sys.argv}")
    print(f"Incorrect length of command line arguments: {len(sys.argv) - 1}")
    sys.exit()

my_str = sys.argv[1]
action = sys.argv[2]

if action == "upper":
    print(my_str.upper())
elif action == "lower":
    print(my_str.lower())
elif action == "title":
    print(my_str.title())
else:
    print('Your option is invalid.')
