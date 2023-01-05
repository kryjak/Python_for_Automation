"""
Operator Overloading in Python
"""

"""
Operator overloading allows us to change the way operators work for user-defined types.
For example, the '+' operator can add two numbers, merge two lists or concatenate two strings, depending on the context. 
https://www.programiz.com/python-programming/operator-overloading
"""

class Complex:
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag

	# overload +
	def __add__(self, other):
		return self.real + other.real, self.imag + other.imag

obj1 = Complex(1, 2)
obj2 = Complex(3, 4)
obj3 = obj1 + obj2
obj4 = obj1.__add__(obj2)  # same thing
print(obj3)
print(obj4)

print("-".center(50, "-"))
# The example above is fairly useless, but we can think of something more realistic.
# For example, we can overload the comparison operator < such that it can compare objects in user-defined classes:

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __lt__(self, other):
		return self.age < other.age

young = Person('Mike', 25)
old = Person('Peter', 60)

print(young < old)
print(young.__lt__(old))

# This is actually useful because without overloading <, we wouldn't be able to compare two objects of class Person
