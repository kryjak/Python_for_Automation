""""""
"""
Class methods - it has access and can modify only class variables, not instance variables.
Any method we create in a class will automatically be created as an instance method unless we explicitly tell Python 
that it is a class or static method.

A class method can be created by either using:
1. classmethod() function
2. @classmethod decorator - used to create factory methods, i.e. methods that return a class object for later use
 
In either case, the first argument should be 'cls', as opposed to 'self' for instance methods.

A class method can be called using ClassName.method(...), as well as directly through an object as each object of the 
class inherits its methods and attributes.

https://www.programiz.com/python-programming/methods/built-in/classmethod
https://pynative.com/python-class-method/
"""


class Person:
    species = 'human'

    def __init__(self, name):
        self.name = name

    @classmethod
    def print_species(cls):
        print('The species is:', cls.species)

    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species


Person.print_species()

john = Person('John')  # we can also call the class method from the instance
john.print_species()

print("-".center(20, "-"))


# we can also convert a method to a class method post-factum, but this is not nice syntax, so avoid using it
def print_species2(cls):  # note the argument is cls, but in theory we can use anything else
    print('The species2 is:', cls.species)


Person.print_species2 = classmethod(print_species2)
Person.print_species2()

print("-".center(20, "-"))
# we can use a class method to access and/or modify a class variable
Person.change_species('alien')
# john.change_species('dog')  # this can also be accessed from the level of an object of the class
Person.print_species()

print("-".center(20, "-"))
# We can dynamically set an attribute:
setattr(Person, 'nlegs', 2)  # same as Person.nlegs = 2
print('nlegs:', Person.nlegs)

# We can also dynamically delete the attribute:
# delattr(Person, 'nlegs')  # either of these two lines will work
del Person.nlegs
# print('nlegs:', Person.nlegs)  # AttributeError

print("inheritance".center(20, "-"))


# class methods get inherited by the children of the class:

class Man(Person):
    gender = 'male'


man = Man('Mike')
man.print_species()  # inherited from Person

print("FACTORY METHODS".center(50, "-"))
# We can use the @classmethod to create a 'factory method' - a method that returns an object of this class

from datetime import date


class Person:
    species = 'human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


# create an instance in the usual way
person = Person('Adam', 19)
person.display()

# create an instance using the factory method
person1 = Person.from_birth_year('John', 1985)
person1.display()

print("inheritance".center(20, "-"))


# factory methods are also understood in inheritance

class Woman(Person):
    gender = 'female'


woman = Woman.from_birth_year('Claudia', 1976)  # inherited from Person
woman.display()
