"""
Decorators in Python
https://www.programiz.com/python-programming/decorator
https://www.youtube.com/watch?v=FsAPt_9Bf3U&ab_channel=CoreySchafer
"""

"""
Decorators are design patterns that allow us to modify the behaviour of a function by wrapping it in another function.
This is very similar to the concept of Closure (see Closure.py and First_class_functions.py):

def decorator(msg):
	def wrapper():
		print(msg)
	return wrapper

hi_test = decorator('Hi!')
hi_test()  # prints 'Hi!'

A decorator takes this concept further.
Instead of passing a normal argument to the outer function, let's pass a function.
This allows us to add functionality to our existing function by including this functionality within the wrapper.
"""


def decorator(function):
    def wrapper():
        print('about to execute', function.__name__)
        return function()  # note instead of a print, we now return the execution of 'function'

    return wrapper


def display():
    print('display function has executed')


decorated_display = decorator(display)
decorated_display()

print("-".center(10, "-"))
# We can redefine our function such that from now onwards it will be decorated with the wrapper:
display = decorator(display)
display()

print("-".center(10, "-"))


# But there's a neater syntax for writing the same.
# We need to precede the function definition with @nameofdecorator:

@decorator
def display3():
    print('display function has executed')


display3()

print("-".center(10, "-"))
"""
notice that so far this works only if the function to be decorated takes no arguments

@decorator
def display_name_and_age(name, age):
	print(f'The name is {name} and the age is {age}.')

display_name_and_age('John', 25)  # prints TypeError

How to we change that? Just use *args and **kwargs:
"""


def decorator(function):
    def wrapper(*args, **kwargs):
        print('about to execute', function.__name__)
        return function(*args, **kwargs)  # note instead of a print, we now return the execution of 'function'

    return wrapper


@decorator
def display4():
    print('display function has executed')


display4()


@decorator
def display_name_and_age(name, age):
    print(f'The name is {name} and the age is {age}.')


display_name_and_age('John', 25)

print("-".center(10, "-"))


# We can also use a class as a decorator:
class decorator_class:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print('about to execute', self.function.__name__)
        return self.function


@decorator
def display5():
    print('display function has executed')


display5()


@decorator
def display_name_and_age(name, age):
    print(f'The name is {name} and the age is {age}.')


display_name_and_age('John', 25)

print("EXAMPLE: LOGGING".center(50, "-"))


# A classic example of how we might use a decorator is to log how many times and which functions have been used:

def logger(function):
    import logging
    logging.basicConfig(filename='decorators.log', level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(f'Ran function {function.__name__} with args {args} and kwargs {kwargs}.')
        return function(*args, **kwargs)

    return wrapper


@logger
def display6():
    print('display function has executed')


@logger
def display_name(name):
    print(f'The name is {name}.')


@logger
def display_name_and_age(name, age):
    print(f'The name is {name} and the age is {age}.')


display6()
display_name('John Cena')
display_name('Shaquille O\'Neal')
display_name_and_age('Mike', 25)

print("EXAMPLE: TIMING".center(50, "-"))


# Another classic example is timing a function:

def timer(function):
    import time

    def wrapper(*args, **kwargs):
        tic = time.time()
        result = function(*args, **kwargs)
        time.sleep(1)
        toc = time.time()
        print(f'Executed {function.__name__} in {toc - tic}s.')

        return result

    return wrapper


@timer
def display_name_and_age(name, age):
    print(f'The name is {name} and the age is {age}.')


display_name_and_age('Mike', 25)

print("STACKING DECORATORS".center(50, "-"))


# We can also stack multiple decorators on top of each other:

@timer  # top-most decorator applied last
@logger  # applied first
def display_name_and_age(name, age):
    print(f'The name is {name} and the age is {age}.')


display_name_and_age('Peter', 73)

print("-".center(10, "-"))
"""
Let's see what happened here. First, the 'logger' decorator was applied first at it wrote a line to decorators.py.
Then, the 'timer' decorator was applied and it seems to have timed the process correctly, but it prints:
Executed wrapper in ...
Why does it print 'wrapper' instead of 'display_name_and_age'?
Remember that the @decorator notation is equivalent to
	function = decorator(function)
so that:
	@timer
	@logger
	def display_name_and_age
is equivalent to:
display_name_and_age = timer(logger(display_name_and_age))
but the output of the inner decorator is the 'wrapper' function! So the outer decorator takes this as its input and 
we lose the information about the original function name.
To prevent this, we can use the 'functools' module and precede each wrapper with:
	@wrap(function)
"""
from functools import wraps


def logger(function):
    import logging
    logging.basicConfig(filename='decorators.log', level=logging.INFO)

    @wraps(function)  # keeps information about the function being decorated
    def wrapper(*args, **kwargs):
        logging.info(f'Ran function {function.__name__} with args {args} and kwargs {kwargs}.')
        return function(*args, **kwargs)

    return wrapper


def timer(function):
    import time

    @wraps(function)  # keeps information about the function being decorated
    def wrapper(*args, **kwargs):
        tic = time.time()
        result = function(*args, **kwargs)
        time.sleep(1)
        toc = time.time()
        print(f'Executed {function.__name__} in {toc - tic}s.')

        return result

    return wrapper


@timer  # top-most decorator applied last
@logger  # applied first
def display_name_and_age(name, age):
    print(f'The name is {name} and the age is {age}.')


display_name_and_age('Carlos', 37)

# Now we get:
# Executed display_name_and_age in ...

print("DECORATORS WITH ARGUMENTS".center(50, "-"))


# We can also use decorators with arguments by wrapping them in yet another function (but this is not very elegant...)
# https://www.youtube.com/watch?v=KlBPCzcQNU8&ab_channel=CoreySchafer

def prefix_decorator(prefix, suffix):
    def decorator(function):
        def wrapper(*args, **kwargs):
            print(prefix, 'about to execute', function.__name__, suffix)
            print(prefix, 'about to execute', function.__name__, suffix)
            return function(*args, **kwargs)  # note instead of a print, we now return the execution of 'function'

        return wrapper

    return decorator


@prefix_decorator('TESTING', 'END OF TEST')
def display_name_and_age(name, age):
    print(f'The name is {name} and the age is {age}.')


display_name_and_age('John', 25)
