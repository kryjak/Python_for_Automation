"""
Functions
"""
import os
import time


# A simple function:

def my_function(cmd1, cmd2):
    print('Executing first command')
    time.sleep(2)
    os.system(cmd1)
    print('Executing second command')
    time.sleep(2)
    os.system(cmd2)


# my_function('clear', 'ls')

# Another example - a function with no arguments:
print("-".center(50, "-"))


def printing():
    print('this is a test')
    return 100  # The 'return' statement defines the output of the function - default is None


ret = printing()
print(ret)

# We can call one function within another:
# Note the inner function can be defined later (this is contrary to Mathematica), as long as we define both before
# the outer function is called
print("-".center(50, "-"))


def my_cube(n):
    return my_square(n) * n


def my_square(n):
    return n * n


print(my_cube(4))

# Local and global variables:
print("-".center(50, "-"))
x = 10


def define_x():
    x = 4
    print(x)


define_x()  # Local x
print(x)  # Global x

# We can also declare a variable as global
print("-".center(50, "-"))
x = 10


def define_x():
    global x
    x = 4
    print(x)


define_x()  # Now x=4 is global
print(x)

"""
In Python, there are four types of arguments that can be passed into a function:
1. Positional arguments - are passed to the function according to their order in f(...)
2. Keyword arguments - are passed to the function based on the keyword, not their order, e.g. f(..., a=2, ...). If we 
   swap the order of the arguments in a call, positional arguments cannot come after keyword arguments (see example).
   Otherwise, Python does not understand which positional corresponds to which parameter of the function.
3. Default arguments - arguments which can be supplied to the function call, but if they are not, their default values
   are used. They have to be at the end, e.g.:
   def f(..., a=1)
   means that the default value of a=1.
4. Variable-length arguments - we do not need to specify the number of such arguments when defining the function.
   There are two types of such arbitrary arguments:
   a) arbitrary positional arguments (*args)
   b) arbitrary keyword arguments (**kwargs)
   
https://pynative.com/python-function-arguments/
"""

# We can specify default values of the arguments:
print("-".center(50, "-"))


def fun(x=10, y=7):
    return x * y


print(fun(3, 4))
print(fun())

# We can also specify the default value of not all arguments, but there is a catch:
# The argument with the default value needs to be at the end!
# Otherwise, Python would not know how to understand the order of arguments when this function is called
print("-".center(50, "-"))


def fun(y, x=10):
    return x * y


print(fun(3, 4))
print(fun(7))

# Keywords allow us to specify the values of arguments even if they are not in the order specified when defining the
# function
print("-".center(50, "-"))


def fun(a, b, c, d):
    print(f'a is {a}, b is {b}, c is {c}, d is {d}')
    return None


fun(5, 10, 15, 20)
fun(10, 5, 15, 20)  # These are passed as positional arguments
# fun(c=15, d=20, 5, 10)  # This does not work because positional arguments can not come after keyword arguments
# fun(5, b=10, c=15, 20)  # Same reason
# fun(5, 20, c=15, b=10)  # Nothing is printed because this is not a valid call to this function
fun(5, 10, c=15, d=20)  # Keyword arguments have to be at the end
fun(5, 10, d=20, c=15)  # But their order does not matter

print("-".center(50, "-"))


# Arbitrary positional arguments:
def my_avg(*args):
    sum = 0
    for number in args:
        sum = sum + number
    return sum / len(args)


print(my_avg(1, 2, 3))
print(my_avg(1, 2, 3, 4, 5))

print("-".center(50, "-"))


# Arbitrary keyword arguments are passed and accessed like a dictionary
def percentage(**kwargs):
    for sub in kwargs:
        sub_name = sub  # Note that each sub in kwargs refers to just the key
        sub_marks = kwargs[sub]  # To get the value, we need to do dict[key]
        print(sub_name, "=", sub_marks)


percentage(math=56, english=61, chemistry=73)  # This can be extended arbitrarily
percentage(math=56, english=61, chemistry=73, physics=100, art=11)

print("-".center(50, "-"))
# We can also import functions from a different script:
import functions_18 as extra  # without .py extension

# No print statement from not_needed() at this stage!
print(f'__name__ in Section_18.py = {__name__}')
# __name__ is a predefined variable equal to the name of the script
# if we call it from the script we are running, it gives __main__
# if we call it in a script which is imported into the file being run, we get the name of that script

# Now the functions from another file are loaded.
print(dir(extra))
# print(help(extra))

print(extra.addition(2, 3))
print(extra.subtraction(2, 3))
print(extra.multiplication(2, 3))
print(extra.division(2, 0))

"""
When importing another script, it might have some print statements or functions calls that we do not want here.
In this example, functions_18.py has a superfluous function not_needed() which is then called.
This results in an unwanted print right at the import stage, when the file is being read.
How do we suppress it?
We need to wrap the unwanted call in an 'if' statement, for example:
if __name__ == '__main__':
    not_needed()
Note that the print statement from not_needed() was not printed here when importing functions_18.py
It only appears when we explicitly call the function:
extra.not_needed()  # Now the print statement is invoked

More generally, the use of: 
if __name__ == '__main__':
    not_needed()
is a common way of defining some content that should be executed only when a file is run as a standalone script,
rather than as an imported module.
For example, in functions_18.py, which is imported as a module here, we could have some fun1, ... fun10, and then:

def main():
    fun1()
    .
    .
    .
    fun10()

if __name__ == '__main__':
    main()
    
This means that fun1...10 will be called only if functions_18.py is run as a script, but not as an imported module!
https://www.programiz.com/python-programming/main-function
https://realpython.com/python-main-function/#a-basic-python-main
"""
