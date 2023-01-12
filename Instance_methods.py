"""
Static vs class vs instance methods in Python
"""
import types

"""
In Python, we have three types of methods:
1. Instance methods - they use instance attributes, i.e. attributes of a particular object of some class. As such, 
they also have access to (and can modify) class attributes.
2. Class methods - they use only class attributes, not a particular instance
3. Static methods - they don't have access to (or modify) instance or class attributes. In other words, they perform 
some task in isolation.

Any method we create in a class will automatically be created as an instance method unless we explicitly tell Python 
that it is a class or static method.

https://pynative.com/python-class-method-vs-static-method-vs-instance-method/
https://pynative.com/python-instance-methods/#h-create-instance-variables-in-instance-method
"""

print("INSTANCE METHODS".center(50, "-"))
class Student:
	subject = 'Physics'  # class attribute

	def __init__(self, name, age):
		# Instance variable
		self.score = None
		self.name = name
		self.age = age

	# instance method to access instance variable
	def show(self):
		print('Name:', self.name, '\b,', 'Age:', self.age)

	# instance method to modify INSTANCE variable
	def update(self, age, subject):
		self.age = age
		self.subject = subject

	# instance method to modify CLASS variable
	def update2(self, subject):
		# subject = subject  # this will NOT modify the class attribute 'subject' - it treats 'subject' as a local var
		# Student.subject = subject  # this will
		self.__class__.subject = subject  # this will as well

	# instance method to add instance variable
	def add_marks(self, marks):
		self.marks = marks

mary = Student('Mary', 22)

mary.show()
print('instance subject:', mary.subject)  # the class variable is inherited onto every instance of this class:
print('class subject:', Student.subject)

print("-".center(10, "-"))
mary.update(23, 'Maths')  # modifies the instance variable, but not class
mary.show()
print('instance subject:', mary.subject)
print('class subject:', Student.subject)

print("-".center(10, "-"))
mary.update2('Chemistry')  # modifies class variable, but not instance
mary.show()
print('instance subject:', mary.subject)
print('class subject:', Student.subject)

print("-".center(10, "-"))
mary.add_marks(87)  # adds a non-existing attribute
print('instance marks:', mary.marks)
# print('class marks:', Student.marks)  # AttributeError, because 'marks' is an instance var

setattr(mary, 'score', 46)  # can also do this, but note the attribute has to be given as a string
print('instance score:', mary.score)  # and we should add self.score = None to the constructor

# we can also delete an instance attribute:
delattr(mary, 'score')
# print('instance score:', mary.score)  # AttributeError

setattr(mary, 'age', 50)  # setattr can also modify the existing attribute, equivalent to mary.age = 50
print('instance age:', mary.age)

print("-".center(10, "-"))
# We can dynamically create a method associated with an object:

def inst_method(self):
	print('This method is associated with the instance.')

mary.instance_method = types.MethodType(inst_method, mary)  # note the syntax - method is tied to 'mary' object
mary.instance_method()

john = Student('John', 16)
# john.instance_method()  # AttributeError - 'john' does not have this attribute!

# now delete this instance method:
del mary.instance_method
# mary.instance_method()  # AttributeError

del mary.name  # deletes name only for this instance! this attribute is still accessible for other instances:
print(john.name)
