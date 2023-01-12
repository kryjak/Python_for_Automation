"""
filter()
"""

"""
The builtin function filter() extracts elements from an iterable for which a specified function returns True.
(Similar to Select in Mathematica).
filter(fun, iterable) -> iterator
https://www.programiz.com/python-programming/methods/built-in/filter
"""

numbers = range(11)


def test_even(n):  # Create the test condition
    if n % 2 == 0:
        return True
    else:
        return False


even_iterators = filter(test_even, numbers)  # returns an iterator
even_list = list(even_iterators)  # convert iterator to a list
print(even_list)

# Note we can clean up the test function by using a neater return statement:

my_string = 'This is some test string'.lower()


def test_letters(letter):
    return True if letter > 'k' else False  # True if a letter occurs after 'k'


after_k = list(filter(test_letters, my_string))
print(after_k)
# Note that Python can also compare letters, e.g. 'd' > 'c', but they have to be both upper or lowercase

print("-".center(50, "-"))
# Even better, we can use a lambdo function within the filter()
# Let's redo the above examples:

even_iterators = filter(lambda x: x % 2 == 0, numbers)
even_list = list(even_iterators)
print(even_list)

after_k = list(filter(lambda letter: letter > 'k', my_string))
print(after_k)

print("-".center(50, "-"))
"""
Note: if None is passed as the test function, filter() selects all 'truthy' elements,
that is elements whose boolean value is True
https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false
https://docs.python.org/3/library/stdtypes.html#truth-value-testing
"""

random_list = [1, 'a', 0, False, '', ' ', True, '0']

filtered = list(filter(None, random_list))
print(filtered)
# Note '0' and ' ' are truthy because they are non-empty strings
