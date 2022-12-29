"""
There are 4 data structures in Python:
1. Lists - [ ]
2. Tuples - ( )
3. Dictionaries - { } with key-value pair
4. Sets - { }
"""
# --------------------------------------- LISTS ------------------------------------------
empty_list = []
my_list = [1, 2 / 3, 4 + 5j, 6.7, "blabla"]  # A list can have mixed data types
print(f"The type of \'my_list\' is {type(my_list)}")
print(f"The boolean value of \'empty_list\' is {bool(empty_list)}")
print(f"The boolean value of \'my_list\' is {bool(my_list)}")
print(f"Multi-level indexing: {my_list[-1][1]}")

"""
Remember: lists are mutable, strings are immutable!
In the previous section, we saw that doing something like this is not allowed:
string = "ABC"
string[0] = "X"
print(f"string: {string}")
"""

# Remember that doing new_expr = old_expr does NOT create a copy - new_expr points to the same memory location
# To create a copy, use:
list_copy = my_list[:]  # Or:
list_copy = my_list.copy()

my_list[0] = "First item"
print("The list with the modified first item:", my_list)
# This means that an operation on a list automatically modifies it:
my_list.clear()
print("The cleared list, without defining a new variable:", my_list)
# We don't have to assign a new variable to the modified list

# Append, extend and insert:
list_copy.append(["X", "Y", "Z"])
print(f"List with an element appended at the end: {list_copy}")
list_copy.extend(["X", "Y", "Z"])
print(f"We can also extend the list, as if adding new indices: {list_copy}")
ind = 2
list_copy.insert(ind, "insertion")  # Inserts object BEFORE index
print(f"List with an element inserted BEFORE index {ind}: {list_copy}")

# Remove and pop
list_copy.remove("X")
print(f"List with \'X\' removed: {list_copy}")
list_copy.pop()
print(f"Pop removes last position by default: {list_copy}")
list_copy.pop(ind)
print(f"We can also specify the index to remove: {list_copy}")

# Reverse and sort
list_copy.reverse()
print(f"Reversed list: {list_copy}")

# Sort only works on a list where numerical operations can be applied
list_copy = [5, 1, 5, 7, 2, 3, 6]
list_copy.sort()
print(f"Sorted list: {list_copy}")
list_copy.sort(reverse=True)
print(f"Reverse sorted list: {list_copy}")

"""
By the way, note the documentation for sort includes an asterix:
sort(self: list[SupportsLessThanT], *, key: None = ..., reverse: bool = ...) -> None
This asterix forces us to use keyword arguments e.g. foo(a=10, b=20), 
i.e. when calling the function we HAVE to specify the keywords a and b. See
https://stackoverflow.com/questions/2965271/forced-naming-of-parameters-in-python/14298976#14298976
and also
https://stackoverflow.com/questions/400739/what-does-asterisk-mean-in-python
for the explanation of:
*args - excess positional parameters
**args - excess keyword parameters
"""

# ----------------------------------- TUPLES --------------------------------------------
my_tuple = (1, 2, 3)
empty_tuple = ()
print(f"The type of \'my_tuple\' is {type(my_tuple)}")
print(f"The boolean value of \'empty_tuple\' is {bool(empty_tuple)}")
print(f"The boolean value of \'my_tuple\' is {bool(my_tuple)}")

"""
Tuples, just like strings, are immutable!
For this reason, we don't have operations like pop, append, extend, remove, etc., as we did for Lists
Lists are better if we want to perform some operations on the objects.
Tuples are better if we just quickly need to retrieve some data. They are comparatively faster and take up less memory.
"""

another_tuple = 1, 2, 3
print(f"Another way to define a: {type(another_tuple)}")

# ----------------------------------- DICTIONARIES --------------------------------------------
# A dictionary is like an Association in Mathematica
# It is mutable!
# It supports mixed data types:
my_dict = {'fruit': 'apple', 'vegetable': 'beetroot', 'animal': 'dog', 'number': 10, 0: 'zero'}
empty_dict = {}
print(f"The type of \'my_dict\' is {type(my_dict)}")
print(f"The boolean value of \'empty_dict\' is {bool(empty_dict)}")
print(f"The boolean value of \'my_dict\' is {bool(my_dict)}")

# Two ways of retrieving the values:
print(f"The fruit is: {my_dict['fruit']} and the number is: {my_dict.get('number')}")

# Note the difference:
# print(f"With [ ]: {my_dict['star']}")  # Gives an error for missing keys
print(f"With .get: {my_dict.get('star')}")  # Does not give an error

# Print all the keys, values, or items - (key, value)
print(f"Print all the keys: {my_dict.keys()}")
print(f"Print all the values: {my_dict.values()}")
print(f"Print all the items: {my_dict.items()}")

# We can add the missing item:
my_dict['star'] = 'Sirius'
print(f"The new dictionary is: {my_dict}")

# We can also update a dictionary using another dictionary:
another_dict = {'car': 'Mercedes'}
my_dict.update(another_dict)
print(f"The updated dictionary with is: {my_dict}")

# pop removes a certain key-pair and returns the corresponding value:
new_dict = my_dict.pop('vegetable')
print(f"Dictionary with 'vegetable' key-pair removed: {my_dict} and the value is {new_dict}")

# popitem removes and returns the last key-pair inserted into the dictionary
# Before Python 3.7, the popitem() returned and removed a random element (key, value) pair from the dictionary.
my_dict.popitem()
print(f"Dictionary with the most recently inserted key-pair removed: {my_dict}")

# fromkeys
subjects = ['physics', 'math', 'chemistry', 'english']
grades = dict.fromkeys(subjects)
print(f"Newly created grade dictionary: {grades}")
grades = dict.fromkeys(subjects, 5)
print(f"We can also insert a value: {grades}")  # but note that this value is the same for all keys
"""
We can also use a mutable object, e.g. a list, as the value. This object can then be dynamically updated and the 
changes will be reflected in the dictionary. See an example and how to suppress this behaviour:
https://www.programiz.com/python-programming/methods/dictionary/fromkeys
"""

# setdefault value for a key:
grades.setdefault('physics', 6)  # if the key is already present, leave it alone
grades.setdefault('arts', 3)  # but if it's not present, update the dictionary with this default value
print(f"Grades updated with default values: {grades}")

# ----------------------------------- SETS --------------------------------------------
# A set is an unordered collection of data
# It automatically deletes duplicate items
my_set = {4, 5, 7, 2, 7, 0, 7, 2, 5}
print(f"The set is {my_set}")
# Note that to define an empty set, we can't just use empty {}, because that is understood as an empty dictionary:
empty_set = {}
print(f"The type of \'my_set\' is {type(empty_set)}")
empty_set = set({})
print(f"The type of \'my_set\' is {type(empty_set)}")

print(f"The boolean value of \'empty_set\' is {bool(empty_set)}")
print(f"The boolean value of \'my_set\' is {bool(my_set)}")

# We can perform the standard mathematical operations on sets:
another_set = {4, 5, 9, 12, 0, 3, 7}
print(f"The set intersection is, {my_set.intersection(another_set)}")
print(f"The set union is, {my_set.union(another_set)}")

print("possible operations are:", dir(set))