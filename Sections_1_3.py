#!/usr/bin/python
# The first line is called a 'shebang!'
# Its purpose is to serve as a shortcut for the interpreter.
# Without it, to run this script we need to type 'python hello_world.py' in the Linux shell
# But with this line, we can simply do './hello_world.py' from the shell
# Linux knows that the first line serves as the command to be applied to the filename
# (Bear in mind we might also need to do 'chmod +x' on the filename

print("Hello World!")
print("This is my first Python script.")

# Note that Python has automatic indentation. It helps with marking separate blocks of code
# The indentation throughout the block should be consistent for all lines.

if 3 > 1:
    print("First print statement")  # This is fine, but 'else' has to be aligned with 'if'
else:
  print("Another print statement")

# Note how PyCharm is giving us a warning:
# "Line 10 is unreachable."
# This is because it knows that the 'else' part of the 'if' statement will never be reached if 3 > 1. Clever!

print("This should be outside of the if statement")

# There are certain special characters that we can use to manipulate the output within the quotation marks.
# We escape the special characters by using \\
print("Now we're going to separate \nthese two lines using \\n ")
print("We can also join two words \btogether with \\b")
print("Try doing it multiple \b\btimes")
print("Another example is \t tab: \\t")

# The print statements can also be used with single quotation marks:
print('Try escaping Python\'s quotation marks')

print("We can also make a \a sound")
# The full list can be found at: https://chercher.tech/python-programming/python-special-characters

# Types of variables:
x = 4
y = 4.0
print(type(x))
print(type(y))

# Spaces in print statements are automatic:
print(x, "and", y)

# We can delete a variable to free up RAM:
del x
# print(x)

# id gives the address of an object in memory, i.e. a unique identifier
# remember that to get info about a function, in PyCharm we can press Ctrl+Q
print(id(y))

# Types:
x = 5
y = 5.2
z = 5.2 + 2.9j
s = "text"
my_value = True
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(s, type(s))
print(my_value, type(my_value))

# Type conversion:
print('Type conversion:')
print(str(x), type(str(x)))
print(bool(x), type(bool(x)))
print(bool(0), type(bool(0)))
print(int("420"), type(int("420")))
# print(int("test"), type(int("test")))

# Any data type can be converted to Boolean:
# bool(any_data_type) = True or False
# bool(empty) = False
# bool(non-empty) = True
print("converting to Boolean data type:")
print(bool(0), bool(""), bool(None), bool(()), bool([]), bool({}))
# Note:
print(bool(" "))  # because a space is a non-empty string
# Any data type can be converted to a string, but the reverse is not necessarily true

# f-strings:
non_f_string = "This string does not update the {x} and {y} values"
f_string = f"This string updates the {x} and {y} values"
print(non_f_string)
print(f_string)

# We can feed input into the program by using 'input'
a = input('Enter \'a\' value: ')

print(f"The value of a is {a} and its type is {type(a)}")  # The input is a string!

# We can convert such input to the desired class using type conversion, as explained above
# Or better, we can use 'eval':

b = eval(input('Enter \'b\' value: '))
print(f"b is {b} and its type is {type(b)}")
# Note that this automatically converts a number to int, float, or complex
# But if we want to enter a string, we need to include the quotation marks, e.g. "AAA"
