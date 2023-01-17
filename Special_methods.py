"""Special methods"""

"""
Special methods are built-in methods associated with a class that implement some kind of behaviour.
They are also known us 'dunder' methods because they begin with a double underscore, __
"""

class Employee:
    company = 'IBM'

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f"{self.first}, {self.last}"

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.pay}"

    # we can override a special method so that it is understood for a particular class
    # see Operator_overloading.py
    def __add__(self, other):
        return self.pay + other.pay

employee1 = Employee('John', 'Smith', 10000)
employee2 = Employee('Alan', 'Johnson', 25000)

print(employee1)
# if neither __repr__ nor __str__ is not defined, it will print:    <__main__.Employee object at 0x7f5e705627a0>
# if __repr__ is defined, it will print:    Employee(John, Smith, 10000)
# if __str__ is defined, it will print:     John, Smith - 10000

print(employee1.__str__())  # same as str(employee1)
print(employee1.__repr__())  # same as str(employee1)

print("-".center(50, "-"))
"""
print(2+3) is actually using the __add__ dunder method of class 'int'

print(help(int))
__add__(self, value, /)
 |      Return self+value.
"""

print(int.__add__(2, 3))

# if we comment out __add__ in Employee:
# print(employee1 + employee2)  # TypeError: unsupported operand type(s) for +: 'Employee' and 'Employee'

print(employee1 + employee2)
print(employee1.__add__(employee2))
print(Employee.__add__(employee1, employee2))
