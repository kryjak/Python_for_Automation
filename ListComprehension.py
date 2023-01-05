"""
List comprehension in Python
"""

"""
List comprehension allows us to avoid using a full 'for' loop to iterate over iterable objects and instead use a 
one-line notation. It is somewhat similar to a lambda function in that it allows us to write neater code.
Every list comprehension can be written in for loop, but not every for loop can be written as list comprehension.
The syntax is:
[expression for ii in list]
https://www.programiz.com/python-programming/list-comprehension
"""

squares = []

for ii in range(1, 6):
	squares.append(ii ** 2)

print(squares)

# the same can be achieved using list comprehension:
squares = [ii ** 2 for ii in range(1, 6)]
print(squares)

# yet another way to achieve this:
squares = list(map(lambda ii: ii ** 2, range(1, 6)))
print(squares)

print("CONDITIONAL STATEMENTS".center(50, "-"))
"""We can also use conditional statements in list comprehension. The syntax is:
[expression for ii in list if condition]
"""

# Recall the example from Filter.py - filter out all letters from a string that are after 'k' in the alphabet
my_string = 'This is some test string'.lower()

after_k = list(filter(lambda letter: letter > 'k', my_string))
print(after_k)

# Now redo this using list comprehension with a condition:
after_k = [letter for letter in my_string if letter > 'k']
print(after_k)

# We can also apply multiple conditions:
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
after_k = [letter for letter in my_string if letter > 'k' if letter in vowels]
# after_k = [letter for letter in my_string if letter > 'k' and letter in vowels]  # or just combine them into one 'if'
print(after_k)

# We can even use the 'else' part of 'if' as well:
after_k = [letter if letter in vowels else 'Consonant' for letter in my_string if letter > 'k']
print(after_k)

print("MULTIPLE LOOPS".center(50, "-"))
list1 = ['A', 'B', 'C']
list2 = ['a', 'b', 'c']

list3 = [[ii, jj] for ii in list1 for jj in list2]
print(list3)

list4 = lambda ii, jj: [ii, jj]  # Nope
print(list4(list1, list2))

list5 = list(map(lambda ii, jj: [ii, jj], list1, list2))  # Note the difference!
print(list5)

list6 = list(map(lambda ii: [ii, list(map(lambda jj: jj, list2))], list1))  # Still not the same
print(list6)

print("NESTED LOOPS".center(50, "-"))
# We can also do nested list comprehension:

transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

# this is how a transpose of a matrix is calculated using a proper for loop:
for i in range(len(matrix[0])):
	transposed_row = []

	for row in matrix:
		transposed_row.append(row[i])
	transposed.append(transposed_row)

print(transposed)

# but we can achieve this in one line using a nested list comprehension:
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)
# note that the outer statement is entered first

print("SET COMPREHENSION".center(50, "-"))
# We can repeat everything discussed above but obtain a set instead of a list.
# This might come in useful - for example, sets do not repeat items:

after_k = {letter for letter in my_string if letter > 'k'}
print(after_k)

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
after_k = {letter for letter in my_string if letter > 'k' if letter in vowels}
print(after_k)

after_k = {letter if letter in vowels else 'Consonant' for letter in my_string if letter > 'k'}
print(after_k)

print("DICTIONARY COMPREHENSION".center(50, "-"))
# We can also use comprehension to create or update a dictionary:

dict1 = {ii: ii ** 2 for ii in range(1, 6)}
print(dict1)

old_price = {'milk': 1.02, 'coffee': 3.0, 'bread': 2.5}

new_price = {ii: (old_price[ii] * 1.5 if old_price[ii] > 2 else old_price[ii]) for ii in old_price}
print(new_price)
# a neater way:
new_price = {key: (value * 1.5 if value > 2 else value) for (key, value) in old_price.items()}
print(new_price)

"""
Final note - we have seen list/set/dictionary comprehension, but not tuple comprehension Why is that?
Well, the ( ) brackets were already taken for a generator expression.
Ironically, we can use a generator to generate such a tuple...
tuple(ii for ii in range(1, 6))
https://stackoverflow.com/questions/16940293/why-is-there-no-tuple-comprehension-in-python

Be careful, the following syntax introduced in Python 3.5:
*(ii for ii in range(1, 6)),		# (note the * and , )
is NOT tuple comprehension. It unpacks an iterable (a generator is an iterable) into a tuple literal.
https://stackoverflow.com/questions/52026406/are-python3-5-tuple-comprehension-really-this-limited
"""
