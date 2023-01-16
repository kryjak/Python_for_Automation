""""""
"""
Static methods - just like class methods, they are bound to the class, not an object. As such, they do not require 
instance creation. However, they do not work with any properties associated with the class, only their own parameters.

The advantages of static methods are that they can create some utility functions that do not depend on 
class or instance variables. Such functions can be defined outside the class as well, but sometimes in our workflow 
it is useful to bind them to a particular class, for the sake of clarity of the code.
Moreover, they save us memory - if we create 10 objects of the same class, an instance method is also stored 10 times.
On the other hand, we only have one static method for all these objects.

A static method can be created by either using:
1. staticmethod() function - not recommended, but can be used to add a static method to a class post-factum
2. @staticmethod decorator
 
In either case, a static method takes neither 'self' nor 'cls' as the first argument.

A static method can be called using ClassName.method(...), as well as directly through an object as each object of the 
class inherits its methods and attributes.

A static method can also be called from a class or an instance method belonging to the same class.

https://www.programiz.com/python-programming/methods/built-in/staticmethod
https://pynative.com/python-static-method/
"""

class Dates:
    timezone = 'GMT+1'
    def __init__(self, date):
        self.date = date

    def get_date(self):
        return self.date

    @staticmethod
    def to_dash_date(date):
        print(date.replace("/", "-"))

    # @staticmethod  # this doesn't make sense! The static method does not have access to class var 'timezone'
    # def get_timezone():
    #     print(cls.timezone)  # we can use Dates.timezone, but that's fixing our class name

    # if we define a method without @staticmethod, it is interpreted as an instance method
    # bad syntax, never use this!
    # def nonstatic(n1, n2):  # notice different colouring in PyCharm
    #     print(n1 + n2)

Dates.to_dash_date("22/06/1941")

date = Dates("15/12/2016")  # can also be accessed from the object, but that usage is weird
date.to_dash_date("22/06/1941")

print("-".center(20, "-"))
# we can also convert a method to a class method post-factum, but this is not nice syntax, so avoid using it
def to_dash_date2():  # note the argument is cls, but in theory we can use anything else
    print('\'to_dash_date2\' was defined outside the class and later added as a static method. Avoid this syntax')

Dates.to_dash_date2 = staticmethod(to_dash_date2)
Dates.to_dash_date2()

# print(Dates.nonstatic('AAA', 'BBB'))  # this works, but never use this syntax!
# print(date.nonstatic('AAA'))  # does not work, because it now thinks n1 is the equivalent of 'self'

print("-".center(20, "-"))
