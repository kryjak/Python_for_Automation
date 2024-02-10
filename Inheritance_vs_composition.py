"""
Tutorial based on https://realpython.com/inheritance-composition-python/ and
https://www.geeksforgeeks.org/inheritance-and-composition-in-python/
Inheritance and composition are two major concepts in object-oriented programming that model the relationship between
two classes. They drive the design of an application and determine how the application should evolve as new features
are added or requirements change.

Inheritance defines an 'is a' relationship between the parent and child classes. It is strongly coupled, in the sense
that coupled classes affect each other when changes are made. E.g. class 'car' IS A 'vehicle'.

On the other hand, composition introduces a 'has a' relationship. Classes are no longer each other's subtypes,
but rather they are related to each other. There are no longer parent/child classes, 'composite' and 'component'
classes.
The 'composite' class 'has a' 'component'. The relationship is loosely coupled, in the sense that changes to the
component classes rarely affect the composite class, while changes to the composite class never affect the
component class.
For example, class 'car' can be composed of class 'engine'. We say that the composite class 'car' 'has a' component
class 'engine'.
"""

# a basic example:
class Component:
    def __init__(self):
        print('Component class object created...')

    def m1(self):
        print('Component class m1() method executed...')

class Composite:
    def __init__(self):
        self.obj1 = Component()
        print('Composite class object also created...')

    def m2(self):
        print('Composite class m2() method executed...')
        self.obj1.m1()

obj2 = Composite()
obj2.m2()

print('-'.center(50, '-'))

# a more realistic example involving both inheritance and composition.
# We will create parent classes Vehicle and Engine. Vehicle is going to have child classes Car and Truck,
# while Engine is going to have child classes CombustionEngine and ElectricEngine.
# We will include either of these two engine types as 'components' of the composite classes Car or Truck.

# the component classes:
class Engine:
        pass

class ElectricEngine(Engine):  # inheritance from the Engine class
    def start(self):
        print('Electric engine\n')

class CombustionEngine(Engine):
    def start(self):
        print('Combustion engine\n')

# the composite classes:
class Vehicle:
    def __init__(self, engine: Engine, drive=None):  # ': Engine' here is just a type hint
        # def __init__(self, engine):  # we can omit it or specify something stupid, like ': Composite'
        self.engine = engine  # note the difference wrt to the simpler example above
        self.drive = drive

    def start(self):
        self.engine.start()  # will call the 'start' method of the appropriate engine class

    def select_drive(self):
        print('Selecting drive:')
        self.drive.select_drive()

class Car(Vehicle):
    def start(self):
        print('Car started with')
        super().start()

class Truck(Vehicle):
    def start(self):
        print('Truck started with\r')
        super().start()

electric_car = Car(ElectricEngine())
electric_car.start()

combustion_truck = Truck(CombustionEngine())
combustion_truck.start()

print('-'.center(50, '-'))
# let's try to extend this example further
class Drive:
    pass

class RearWheel(Drive):
    def select_drive(self):
        print('Rear wheel')

class FrontWheel(Drive):
    def select_drive(self):
        print('Front wheel')

off_road_car = Car(CombustionEngine())
off_road_car.start()
# off_road_car.select_drive()  # gives an error, because the drive has not been specified yet
off_road_car.drive = FrontWheel()  # set the attribute of the instance - this initiates an object of the FrontWheel
off_road_car.select_drive()  # now the drive has been selected and we can print it
