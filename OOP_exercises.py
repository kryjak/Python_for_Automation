"""
OOP Exercises
Based on: https://pynative.com/python-object-oriented-programming-oop-exercise/
"""

print("EXERCISE 1".center(50, "-"))
class Vehicle(object):
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

ferrari = Vehicle(300, 1500)
print(f'Max speed: {ferrari.max_speed}, mileage: {ferrari.mileage}')

print("EXERCISE 2".center(50, "-"))
class Vehicle(object):
    pass

mercedes = Vehicle()
print(mercedes)

print("EXERCISE 3".center(50, "-"))
class Vehicle(object):
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

solaris = Bus('solaris', 70, 20000)
print(f'Bus name: {solaris.name}, max speed: {solaris.max_speed}, mileange: {solaris.mileage}')

print("EXERCISE 4".center(50, "-"))
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, route):
        super().__init__(name, max_speed, mileage)
        self.route = route  # add another instance variable to the child class

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

# bus = Bus('solaris', 70, 20000, 'red')
bus = Bus('solaris', 70, 20000, '16CS')
print(bus.seating_capacity())
print(bus.route)

print("EXERCISE 5".center(50, "-"))
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    colour = 'white'

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus = Bus('solaris', 70, 20000)
print(f'The colour is {bus.colour}.')

print("EXERCISE 6".center(50, "-"))
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        return super().fare() * 1.1

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

print("EXERCISE 7 + 8".center(50, "-"))
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(type(School_bus))
print(isinstance(School_bus, Vehicle))
