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
