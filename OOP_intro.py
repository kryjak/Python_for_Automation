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
			self.say = 'I love bikes!'  # this is a global class value, i.e. self.say is the same for any class 
			instance
		
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

print("-".center(50, "-"))
print('Now the remaining destructors are called:')
