print("MERGING DICTIONARIES".center(50, "-"))
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 10, 'c': 3}

# the dictionary on the right takes precedence
print({**dict1, **dict2})
print({**dict2, **dict1})

# this is a part of larger functionality known as unpacking operators:
# https://peps.python.org/pep-0448/
# * is an iterable unpacking operator
# ** is a dictionary unpacking operator

print(*range(5), 5)
print([*range(5), 5, *range(6, 10)])

print("TESTING FLAGS".center(50, "-"))
# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print('passed')

if 1 in (x, y, z):
    print('passed')

# These only test for truthiness:
if x or y or z:
    print('passed')

if any((x, y, z)):
    print('passed')

print("GET ON A DICTIONARY".center(50, "-"))
# get(self, key, default=None)
# Return the value for key if key is in the dictionary, else default.

dict1 = {'a': 1, 'b': 2}
print(dict1.get('a'))  # key exists, so the corresponding value is returned
print(dict1.get('c'))  # key doesn't exist
print(dict1.get('c', 'Default'))  # key doesn't exist, return the default value
