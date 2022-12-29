# https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/

# In Python, indexing starts from 0 !!!
# But backward indexing starts from -1
# Slicing is done with single square brackets
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(string[0], string[-1])

# Slicing is very different to Mathematica! The syntax is:
# [start AT this index:stop BEFORE this index:step size]
print(string[:3])
print(string[3:])
print(string[:-3])
print(string[-3:])
print(string[0:2])

print('The full thing', string[::])
print('Every 2nd element:', string[::2])
print('Every 2nd element, starting AT 1st and finishing BEFORE 8th:', string[1:8:2])
print('Every 2nd element, but starting from the back:', string[::-2])
print('Every 2nd element, but starting AT -8th and finishing BEFORE 1st:', string[-8:1:-2])

print("-".center(50, "-"))
# Interesting behaviour - [:] creates a copy of an array
num = [10, 20, 30, 40, 50, 60, 70, 80, 90]
num_copy = num[:]
num_copy[0:1] = ["AAA", 420, "BBB"]  # Note we can replace an element with a greater number of items
print('num_copy is modified:', num_copy)
print('but num is not:', num)

# BUT assigning tmp = expr does not create a copy, it makes them equal!
num2 = num
num2[0:3] = ["BBB"]  # Note we can replace multiple elements of an array with a single items
print('num2 is modified:', num2)
print('Now num changes as well!', num)

print("-".center(50, "-"))
# Note the difference: [i] replaces position i, [i:j] replaces positions i to j
num = [10, 20, 30, 40, 50, 60, 70, 80, 90]; num[0]   = ["XXX", "YYY", "ZZZ"]; print('num:', num)
num = [10, 20, 30, 40, 50, 60, 70, 80, 90]; num[0:1] = ["XXX", "YYY", "ZZZ"]; print('num:', num)
# Note the different syntax when trying to do the same, but at the end:
num = [10, 20, 30, 40, 50, 60, 70, 80, 90]; num[-1]    = ["XXX", "YYY", "ZZZ"]; print('num:', num)
num = [10, 20, 30, 40, 50, 60, 70, 80, 90]; num[-1:] = ["XXX", "YYY", "ZZZ"]; print('num:', num)
# Because slicing from the end starts at -1, not 0 (as -0 = 0, so the interpreter would get confused),
# We need to select: -1 as the starting element and slice until the end, that is -1:
# Doing -2:-1 will actually be select the -2 element
# num = [10, 20, 30, 40, 50, 60, 70, 80, 90]; num[-1:-2:-1] = ["XXX", "YYY", "ZZZ"]; print('num:', num)  # doesn't work
# We can also do:
num = [10, 20, 30, 40, 50, 60, 70, 80, 90]; num = num[:-1] + ["XXX", "YYY", "ZZZ"]; print('num:', num)

del num[-1]
print('num with deleted last element:', num)

print("-".center(50, "-"))
# Strings are immutable, so if we try to delete/change a part of the string like string[0] = "new_string", we'll get:
# TypeError: 'str' object does not support item assignment
# To get around this, we can do:
string = string[:5] + "XXX" + string[5:]; print('string =', string)
# And to replace a particular character use 'replace':
print('string with X->Y:', string.replace("X", "Y"))

# We can also create a 'slice object' so that we can reuse it multiple times:
myslice = slice(3, 10, 2)
print(string[myslice], 'of length', len(string[myslice]))

print("-".center(50, "-"))
# Case conversion on strings:
test_string = 'Some test sTrInG'
print('To uppercase:', test_string.upper())
print('To lowercase:', test_string.lower())
print('Swap cases:', test_string.swapcase())
print('Capitalise first letters:', test_string.title())
print('Capitalise only first word:', test_string.capitalize())
print('Capitalise only first word:', "Stronger lower case: ß".casefold())

print("-".center(50, "-"))
# The dir() function returns all properties and methods of the specified object, without the values
print(dir(string))
print(dir(num))

print("-".center(50, "-"))
# For example:
print(string.startswith('ABC'))
print(string.endswith('ABC'))
print(string.isupper())

# We can print help:
# help(str)  # or better just press Ctrl+Q in PyCharm

print("-".center(50, "-"))
# Join - the string whose method is called is inserted in between each given string.
# The result is returned as a new string.
print(".".join(string))
print(".".join([string, "123"]))
print("\n".join("123"))

print("-".center(50, "-"))
# Center - return a centered string of specified length - default padding char is space
print("123".center(5))
print("123".center(20, "-"))
print("123".ljust(20, "-"))
print("123".rjust(20, "-"))

# Zfill
print("123".zfill(20))

print("-".center(50, "-"))
# Strip - leading and trailing chars removed. Default char: space
print("  AABBBBCCCDD ".strip())
print("AABBBAAACCCAA".strip('A'))
print("AABBBAAACCCAA".rstrip('A'))  # Right strip
print("AABBBAAACCCAA".lstrip('A'))  # Left strip
print("pythonyy".strip('p').strip('y'))

# Split
print("String to be split".split())
print("String-to-be-split".split('-'))

print("-".center(50, "-"))
# Count
print(string)
print(string.count('X'))
print(string.count('X', 1, 10))

# Index - returns only the FIRST index of a particular character!
print(string.index('X'))
print(string.index('X', 20))  # We can also supply the start and stop indices for the search
# print(string.index('?', 20))  # If a char has not been found, index() throws an exception

# Find
print(string.find('X'))
print(string.find('X', 20))  # We can also supply the start and stop indices for the search
print(string.find('?', 20))  # If a char has not been found, find() returns -1

print("-".center(50, "-"))
# Practise:
# The goal is to take a string input and print it in the centre, right-justified and left-justified

# import os
# ncols = os.get_terminal_size().columns  # this will work in the terminal, but not here
ncols = 158

given_str = eval(input('Enter your string: ')).title()
print(given_str.center(ncols))
print(given_str.rjust(ncols))
print(given_str.ljust(ncols))
