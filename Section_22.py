"""
OOP - Object-Oriented Programming
Python is a multi-paradigm programming language - it supports different programming approaches, including
object-oriented programming. Like other OOP languages, it also supports the notion of objects and classes.

What is an object?
Each object has attributes (variables) and methods (functions), e.g. person has attributes such as name/age,
while its functions are walking, talking, etc.

In OOP, attributes and methods of an object are grouped together in a template/blueprint known as a class.
Then, we can create any desired number of objects from that class (known as instances).
"""


# Define a class
class Bike:
	price = 'Expensive!'
	name = ""
	chainring = []
	casette = []

	def gear_ratio(self):
		return round(self.chainring[0] / self.casette[0], 1), round(self.chainring[0] / self.casette[-1], 1)


"""
Whenever we define a function within a class, we need to supply 'self' as the first argument.
The 'self' is replaced by the object's name during instantiation.
(Any other name is fine too, but we use 'self' by convention).
"""

# Create objects (instances) of class
bike1 = Bike()
bike2 = Bike()

# Access attributes and assign new values
bike1.name = "Road Bike"
bike1.chainring = [54]
bike1.casette = [11, 34]

bike2.name = "Mountain Bike"
bike2.chainring = [20]
bike2.casette = [10, 50]

for bike in [bike1, bike2]:
	print(f"Name: {bike.name}, Chainring: {bike.chainring}, Casette: {bike.casette} ")  # Attributes
	print(f"Gear ratio of the {bike.name.lower()} is: {bike.gear_ratio()}")  # Method
	print(f"This bike is: {bike.price}")  # The attribute that has not been overwritten for each instance

print("-".center(50, "-"))
"""
Note that the Bike class above can also be written using the so-called 'constructor'.
Such constructors initialise values of attributes during instantiation. This is advantageous because we don't have to 
access the attributes and assign them the desired values after creating the instance - we can do both in one step.
There are two types of constructors:
1. default constructor - it does not accept any arguments, only 'self', e.g.:
	class Bike:
		def __init__(self):
			self.say = 'I love bikes!'  # this is a global class value, i.e. self.say is the same for any class instance
		
		def statement(self):
			return self.say
			
	bikeobj = Bike()
	print(bikeobj.statement())  # prints 'I love bikes!'

This situation is equivalent to not using the constructor like above:

	class Bike:
		say = 'I love bikes!'
		def statement(self):
			return self.say
			
	bikeobj = Bike()
	print(bikeobj.statement())  # prints 'I love bikes!'
	
2. parametrised constructors - accepts 'self' and other arguments which are provided by the user at the time of 
instantiation. See below for an example.

Note: we can declare certain attributes within the constructor, and some outside. The former will be 
instance-specific (object/instance attributes) while the latter are global to the class (class attributes).
References:
https://www.programiz.com/python-programming/class-object
https://www.geeksforgeeks.org/constructors-in-python/
"""


class Bike:
	price = 'Expensive!'  # The attribute outside the constructor is global to the class

	# The attributes inside the constructor are instance-specific and need to be supplied during instantiation
	def __init__(self, name="", chnrng=[], cst=None):  # the arguments do not need to have default values
		self.name = name
		self.chainring = chnrng  # Note the names on LHS and RHS do not need to be the same
		if cst is None:  # mutable data types should not be used for default arguments, use this syntax
			self.casette = []
		else:
			self.casette = cst

	def gear_ratio(self):
		return round(self.chainring[0] / self.casette[0], 1), round(self.chainring[0] / self.casette[-1], 1)


# Instantiation - note we now have to provide the arguments within the constructor:
bike1 = Bike("Road Bike", [54], [11, 34])
bike2 = Bike("Mountain Bike", [20], [10, 50])

for bike in [bike1, bike2]:
	print(f"Name: {bike.name}, Chainring: {bike.chainring}, Casette: {bike.casette} ")
	print(f"Gear ratio of the {bike.name.lower()} is: {bike.gear_ratio()}")
	print(f"This bike is: {bike.price}")  # Global to this class

print("-".center(50, "-"))
print('Class attributes vs object attributes:')
print(f'Bike.price: {Bike.price}')  # class attribute
print(f'bike1.casette: {bike1.casette}')  # instance attribute

print(bike1.__dict__)  # get the attributes of the object as a dictionary
print(Bike.__dict__)  # get the attributes of the class as a dictionary

try:
	print(Bike.casette)  # this class attribute does not exist!
except AttributeError as e:
	print(f'Bike.casette: {e}')

print("-".center(50, "-"))


# A small example - addition of complex numbers:
class Complex:
	count = 0

	def __init__(self, real, imag):
		self.re = real
		self.im = imag
		Complex.count += 1  # in this way we can increase a counter every time an instance is created

	def addition(self, n2):
		return Complex(self.re + n2.re, self.im + n2.im)  # the return can be an object of the same class


n1 = Complex(3, 4)
n2 = Complex(5, 2)
n3 = n1.addition(n2)

print(f'real: {n3.re}')
print(f'imag: {n3.im}')
print(f'Created {Complex.count} instances of class Complex.')

print("TRIANGLE-".center(50, "-"))
# Another simple example - a Triangle class to calculate the perimeter of a triangle:

class Triangle:
	def __init__(self, sides):
		self.sides = sides
		# self.perimeter()  # We can also call the methods at the instantiation stage

	def perimeter(self):
		print('Calculating the perimeter in Triangle.')
		return sum(self.sides)


tri1 = Triangle([3, 4, 5])
perimeter = tri1.perimeter()

print(f'The perimeter of tri1 is {perimeter}')

"""
Now we are in a position to understand that, in fact, everything in Python is an object, i.e. an instance of some class.
For example
print(type([1, 2, 3])) gives <class 'list'>
print(type('AAA')) gives <class 'str'>
and so on. The 'dir' function lists all attributes and methods of an object:
"""
print(dir(tri1))
print(dir(Triangle))  # Note the difference - a, b, c are attributes of tri1, not Triangle. Only 'perimeter' is shared.

print(dir(n1))
print(dir(Complex))  # Similarly, re, im are attributes of n1, not Complex. Only 'addition' and 'count' are shared.

print("DESTRUCTOR".center(50, "-"))
"""
Just like we use a constructor to initiate values of attributes using instantiation, we can use a destructor to
perform the clean-up activity before destroying the object, such as closing database connections or filehandle.
The destructor is called whenever the program ends or all references to an object have been deleted.
https://pynative.com/python-destructor/
"""

class Employee:

	# Constructor
	def __init__(self):
		print('Employee created.')

	# Destructor
	def __del__(self):
		print('Employee destroyed.')


obj = Employee()
obj2 = obj  # Creates a new reference to the same object
del obj  # destructor not yet called because we still have one reference pointing to the object
print('After deleting the first reference.')
print('Deleting second reference:')
del obj2  # destructor called when deleting an object
print('The destructor will also be called if we create an object and then the program ends.')
ob3 = Employee()
# destructor called at the end of the program

# The destructor will not work in two cases:
# 1. Circular references - because it does not know which object to destroy first, so it leaves both
# 2. If there is an exception in __init__()

print("CIRCULAR REFERENCES".center(30, "-"))
# Understanding circular references:

class Vehicle:
	def __init__(self, brand, car):
		self.brand = brand
		# saving reference of Car object
		self.dealer = car
		print('Vehicle', self.brand, 'created')

	def __del__(self):
		print('Vehicle', self.brand, 'destroyed')


class Car:
	def __init__(self, brand):
		self.brand = brand
		# saving Vehicle class object in 'dealer' variable
		# Sending reference of Car object ('self') for Vehicle object
		self.dealer = Vehicle(brand, self)
		print('Car', self.brand, 'created')

	def __del__(self):
		print('Car', self.brand, 'destroyed')


bmw = Car('BMW')

print(bmw)  # bmw is an object of the Car class
print(bmw.dealer)  # the .dealer attribute inside the Car class creates an object of the Vehicle class
print(bmw == bmw.dealer.dealer)
# the .dealer attribute inside the Vehicle class refers back to the 'car' attribute that was used to instantiate it -
# i.e. the 'self' within Vehicle(id, self), where for this object 'self' is bmw.
# So overall, bmw.dealer.dealer == bmw

del bmw  # the destructor should execute now, but nothing is happening
print('Did not destroy Car class object.')
print('Will be destroyed at end of program.')


print("ERROR IN __init__()".center(30, "-"))
# Error in __init__():
class Car:
	def __init__(self, brand):
		try:
			assert brand != 'BMW', 'Too expensive!'
		except AssertionError as e:
			print('AssertionError:', e)
		finally:
			self.brand = brand

	def __del__(self):
		print('Car', self.brand, 'destroyed')

bmw = Car('BMW')
del bmw  # nothing happens unless we uncomment the except line above


print("POLYMORPHISM".center(50, "-"))
"""
Polymorphism allows us to use same method names in different classes without confusion.
For example, apart from the Triangle class, we can have the Square class with the same perimeter() method.
Python knows that tri1.perimeter() is different to square1.perimeter() - we say that perimeter() is polymorphic.
Btw, in PyCharm we can click Shift+F11 to view the bookmarks, Ctrl+B to jump to object definition, Shift+Ctrl+B to 
jump to class definition.
"""
class Square:
	def __init__(self, a):
		self.a = a

	def perimeter(self):
		return 4 * self.a

square1 = Square(3)
perimeter = square1.perimeter()

print(f'The perimeter of square1 is {perimeter}.')


print("INHERITANCE".center(50, "-"))
"""
Inheritance allows us to define a new 'child class' that is based on the 'parent class'.
This saves us from duplicating code and makes our program neater.
In the example below, the EquilateralTriangle class is a child class of Triangle (i.e. Triangle is the parent/super 
class). The __init__() and perimeter methods are inherited by the Equilateral Triangle, but the area() method is 
present only within the child class.
https://www.programiz.com/python-programming/inheritance
"""
import math  # to have sqrt below

class EquilateralTriangle(Triangle):
	def area(self):
		print('Calculating area in EquilateralTriangle')
		return round(self.sides[0] ** 2 * math.sqrt(3) / 4, 5)

equitri = EquilateralTriangle([7, 7, 7])
perimeter = equitri.perimeter()
area = equitri.area()
# tri1.area  # does not exist because area is only the child's function

print(f'The perimeter of equitri is {perimeter}.')
print(f'The area of equitri is ~ {area}.')

print("METHOD OVERRIDING".center(50, "-"))
"""
Method Overriding - what happens if the same method is present in both parent and child?
In this case, the method of the child always takes priority over the parent method.
For example, the perimeter of the EquilateralTriangle is simply 3*a, instead of a+b+c, so we can override the
method from the parent class in the child.
Note, however, that if we ever need to access the parent method, we can use super().
The super() builtin method returns a proxy object (temporary object of the superclass) that allows us to access 
methods of the base class.
https://www.programiz.com/python-programming/methods/built-in/super
"""
class EquilateralTriangle2(Triangle):
	# overrides perimeter() from the Triangle parent class
	def perimeter(self):
		print('I am now using the 3*a perimeter formula in EquilateralTriangle2.')
		return 3 * self.sides[0]

	def old_perimeter(self):
		return super().perimeter()  # access the method of the parent class

	def area(self):
		print('Calculating area in EquilateralTriangle2')
		return round(self.sides[0] ** 2 * math.sqrt(3) / 4, 5)

equitri = EquilateralTriangle2([7, 7, 7])
perimeter = equitri.perimeter()  # now the updated formula is being used
oldperimeter = equitri.old_perimeter()  # but we can still access the formula of the superclass by using super()
area = equitri.area()

print(f'The perimeter of equitri is {perimeter}.')
print(f'The old perimeter of equitri is {oldperimeter}.')
print(f'The area of equitri is ~ {area}.')

print("MULTIPLE INHERITANCE".center(50, "-"))
"""
Multiple inheritance - a child class can have more than one superclass.
Note: in case of polymorphic methods, the method from the class on the left always takes precendence over the method 
from the classes on the right, i.e. here some 'my_method' from Triangle would have precendence over 'my_method' from 
Polygon. We can view the inheritance structure using the __mro__ attribute (returns tuple) or mro() method (returns 
list) - Method Resolution Order.
Note: Every class in Python is derived from the object class. It is the most base type in Python.
So technically, all other classes, either built-in or user-defined, are derived classes and all objects are instances 
of the object class.
https://www.programiz.com/python-programming/multiple-inheritance
"""

class Polygon:
	def statement(self):
		print('I am a polygon.')

# this child class inherits __init__() and perimeter() from Triangle, as well as statement() from Polygon:
class EquilateralTriangle3(Triangle, Polygon):
	print('I am an EquilateralTriangle3 object.')

multitri = EquilateralTriangle3([7, 7, 7])
multitri.statement()
multitri.perimeter()

print('__mro__:', EquilateralTriangle3.__mro__)
print('mro():', EquilateralTriangle3.mro())

print("MULTI-LEVEL INHERITANCE".center(50, "-"))
"""
Mult-level inheritance - a child class can have a parent that is in itself a child of another parent.
Normal method overriding rules described above apply.
In the examples below, both EquilateralTriangle and EquilateralTriangle2 are children of Triangle.  
Note: super() moves up one level, not all the way to the highest superclass.
"""
# this child class inherits __init__() from Triangle, but perimeter() is overridden by the one in EquilateralTriangle2
# Note that area() is inherited from EquilateralTriangle, not EquilateralTriangle2, because it comes first.
class EquilateralTriangle3(EquilateralTriangle, EquilateralTriangle2):
	print('I am an EquilateralTriangle3 object.')

	def perimeter1(self):
		return super().perimeter()

	def perimeter2(self):
		return super().old_perimeter()

multitri = EquilateralTriangle3([7, 7, 7])
multitri.perimeter()  # inherited from EquilateralTriangle2
multitri.area()

print('super().perimeter():')  # super() moves up one level to EquilateralTriangle2, not Triangle
multitri.perimeter1()
print('super().old_perimeter():')  # here, super() has been applied twice (recursively) and now refers back to Triangle
multitri.perimeter2()
print('__mro__:', EquilateralTriangle3.__mro__)

# Same as above, but now area is inherited from EquilateralTriangle2
print("-".center(10, "-"))
class EquilateralTriangle3(EquilateralTriangle2, EquilateralTriangle):
	print('I am an EquilateralTriangle3 object.')

multitri = EquilateralTriangle3([7, 7, 7])
multitri.area()
print('__mro__:', EquilateralTriangle3.__mro__)


print("-".center(50, "-"))
"""
Encapsulation - if we want to make a certain attribute or module 'private', i.e. not accessible from anywhere outside 
the class, we can do that by preceding the attribute/module name with __.
Moreover, we can make the attribute/module 'protected', i.e. accessible only within the class + its child classes in 
case of inheritance by using _ instead.

https://stackoverflow.com/questions/20261517/inheritance-of-private-and-protected-methods-in-python
Note: Python does not really have a notion of protected/private members, i.e. 'access' modifiers.
In fact, everything is public. The effect of declaring a variable private, __var, is that it is 'mangled', 
i.e. at compilation time such variables are replaced with _Class__var.
This is done to avoid conflicts in case of inheritance onto child classes, in which case their private variables are
replaced with _ChildClass__var.

But we can easily access even such private variable on the outside, using the mangled name: _ClassName__var.
"""

class Secret:
	def __init__(self, lvl, rcp):
		self.secret = 'This is a secret message.'
		self.__secrecy_level = lvl  # accessible only within Secret
		self._recipient = 'The recipient is ' + rcp  # accessible within Secret and its subclasses

	def get_secrecy_lvl(self):
		return 'The secrecy level is ' + str(self.__secrecy_level)

class Recipient(Secret):  # this class doesn't really make sense, but ok, just to demonstrate encapsulation
	def __init__(self, lvl, rcp):
		super().__init__(lvl, rcp)

	def recipient_list(self):
		return self._recipient
		# return self.__secrecy_level  # does not work
		# return self._Secret__secrecy_level  # works because we have used the mangled name of the private var

sensitive_data = Secret(10, 'NSA')
recipient = Recipient(99, 'CIA')

print("public".center(12, "-"))
print(sensitive_data.secret)
# print(sensitive_data.__secrecy_level)  # gives an AttributeError

print("private".center(12, "-"))
print(sensitive_data.get_secrecy_lvl())  # but we can access the attribute from within the class
# ...unless the method is defined as __get_secrecy_lvl
# We can also use 'name mangling': instance._ClassName__secret
print(sensitive_data._Secret__secrecy_level)

print("protected:".center(12, "-"))
# The child class is able to access the protected attribute, but not private ones
print(recipient.recipient_list())

# The protected attributes are also accessible from the outside - no mangling going on here:
print(recipient._recipient)
print(sensitive_data._recipient)

"""
Getters and setters allow us to implement a better encapsulation scheme
"""


print("-".center(50, "-"))
class Student:
	def __init__(self, name):
		self.__name = name

	@property  # a getter
	def name(self):
		return self.__name

	@name.setter  # a setter - note the name is the same as defined under @property above!
	def name(self, value):
		self.__name = value

student = Student('Alice')

# print(student.__name)  # AttributeError because it's private
print('student.name:', student.name)  # access using the getter

student.__name = 'Bob'  # let's do something stupid like that

print('student.name:', student.name)  # prints 'Alice' - the value of the private variable __name has not been changed
print('student.__name:', student.__name)  # this is treated as a different variable to student._Student__name,
# which is 'Alice'. For explanation of mangling, see Property.py

student.name = 'Charlie'  # modify using the setter

print('student.name:', student.name)  # equivalent to the mangled variable student._Student__name

print("-".center(50, "-"))
print('Now the remaining destructors are called:')
