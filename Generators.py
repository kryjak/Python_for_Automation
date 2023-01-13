"""
Generators in Python
"""

"""
Generators are functions that return an iterator that produces a sequence of values when iterated over.
They are useful when we want to store a large sequence of values, but we don't want to store them all in memory at once.
https://www.programiz.com/python-programming/generator

To define a generator, we use the usual 'def', but instead of 'return' we finish the function with 'yield'.
When such a generator is called, it does not execute the code immediately, but instead returns a generator that can 
be iterated over at a later time.
'yield' produces a value but then pauses the execution until the next value is requested.
"""

def fun(n):
    i = 0
    while i <= n:
        print(i)
        i += 1

fun(5)

# Now do the same using a generator:
print("-".center(10, "-"))

def generator(n):
    i = 0
    while i <= n:
        yield i
        i += 1

my_gen = generator(5)
print(type(my_gen))
for value in my_gen:
    print(value)

print("-".center(10, "-"))
for value in my_gen:
    print(value ** 2)  # Nothing is being printed - because my_gen acts like an iterator which it has been used up!

print("-".center(10, "-"))
# Just like a normal iterator, we can apply next() to it
my_gen = generator(5)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

print("INFINITE GENERATOR".center(50, "-"))
"""
Just like we can create an infinite iterator (e.g. using itertools.count(n), where n = starting value), we can also
create an infinite generator:
"""

def infinite_generator():
    while True:
        yield 0

inf_gen = infinite_generator()
print(next(inf_gen))
print(next(inf_gen))
print(next(inf_gen))
print(next(inf_gen))

print("GENERATOR EXPRESSION".center(50, "-"))
"""
Instead of using the full syntax above, we also use a shortcut to create a generator.
This shortcut is similar to list comprehension, but instead of a list, it creates a generator type object.
The syntax is:
(expression for ii in iterable)
"""
my_gen = (ii for ii in range(5 + 1))
for value in my_gen:
    print(value ** 3)

print("-".center(10, "-"))
# Or:
my_gen = (ii ** 3 for ii in range(5 + 1))
for value in my_gen:
    print(value)
