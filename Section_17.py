"""
Exceptions
Whenever Python encounters an error, it stops. There are:
1. syntax errors - no way to get around these, need to follow the correct syntax
2. runtime errors - can be handled using exceptions

Exceptions can be handled using the try-except (-else-finally) block. Examples of exceptions:
- IndexError
- ZeroDivisionError - print(4/0)
- ImportError
- IndentationError
- ValueError
- TypeError - print(4 + 'string')
- NameError - print(a) if a is not defined
- FileNotFoundError - open('thisfiledoesnotexist.txt')
- IOError

https://www.geeksforgeeks.org/errors-and-exceptions-in-python/?ref=lbp
https://www.geeksforgeeks.org/python-try-except/
https://www.programiz.com/python-programming/exception-handling
"""

try:
    print(4 / 0)
    # print(4 / 2)
except Exception as e:  # A generic exception that we might not know about in advance
    print('Encountered an error:', e)
else:
    print('Valid division')  # Executes only if 'try' does not raise an exception
finally:
    print('Final code')  # Executes after normal end of 'try' or after 'try' terminates due ot an exception

print('The code does not stop even if there is an exception thrown.')

print("-".center(50, "-"))
# We can manually raise a particular, user-defined error
# Note: we can have more than one 'except' block to handle each exception separately
try:
    amount = 5
    # amount = 15  # Try this line
    if amount < 10:
        raise ValueError("please add money in your account")  # raise the ValueError
    else:
        print("Valid amount")
    res = amount/0

except ValueError as e:
    print('Encountered an error:', e)
except ZeroDivisionError as e:
    print('Encountered an error:', e)
except Exception as e:  # A generic exception that we might not know about in advance
    print('Encountered an error:', e)

else:
    print('Process finished successfully')
finally:
    print('This will be printed regardless if there is an exception or not')


print("-".center(50, "-"))
# We can also raise an error elsewhere, e.g. in an 'if' statement
age = 19
if age >= 18:
    print('Adult')
else:
    raise ValueError('The subject is not an adult')

print("-".center(50, "-"))
# Assertions are boolean expressions that check if the condition returns true or not. If it is true,
# the program does nothing and moves on. If it is false, the program stops and throws an error.
# https://www.programiz.com/python-programming/assert-statement
age = 15
try:
    # Equivalent to: if not age >= 18: raise AssertionError('The subject is not an adult')
    assert age >= 18, 'The subject is not an adult'
except AssertionError as e:
    print(e)
else:
    print('Adult')
