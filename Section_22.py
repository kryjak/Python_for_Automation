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
    def __init__(self, name="", chnrng=[], cst=[]):  # the arguments do not need to have default values
        self.name = name
        self.chainring = chnrng  # Note the names on LHS and RHS do not need to be the same
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

try:
    print(Bike.casette)  # this class attribute does not exist!
except AttributeError as e:
    print(f'Bike.casette: {e}')

print("-".center(50, "-"))
# A small example - addition of complex numbers:

# class Complex
