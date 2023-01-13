"""
map()
"""

"""
The builtin function map() applied a specified function to the elements of an iterable.
(Similar to Map in Mathematica).
map(fun, iterable1, iterable2, ...) -> iterator
https://www.programiz.com/python-programming/methods/built-in/map
"""

numbers = range(11)

def square(n):  # Create the test condition
    return n ** 2

square_iterator = map(square, numbers)  # returns an iterator
square_list = list(square_iterator)  # convert iterator to a list
print(square_list)

# We can also use a lambda function to achieve the same:

square_list = list(map(lambda n: n ** 2, numbers))
print(square_list)

# Moreover, we can supply more than one iterable object:
numbers2 = range(0, -11, -1)
sum_list = list(map(lambda n1, n2: n1 + n2, numbers, numbers2))
print(sum_list)

# The iterables can even be of a mixed type, for example:
numbers = list(range(11))
numbers2 = tuple(range(0, -11, -1))
sum_list = list(map(lambda n1, n2: n1 + n2, numbers, numbers2))
print(sum_list)

# If the two iterables are of different lengths, map will execute up until the shorter iterator is used up:
numbers2 = range(0, -5, -1)
sum_list = list(map(lambda n1, n2: n1 + n2, numbers, numbers2))
print(sum_list)
