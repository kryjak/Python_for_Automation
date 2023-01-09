"""
@property decorator in Python
"""

"""
@property is a built in decorator that allows us to define methods that can be accessed as attributes.
A getter is a method that is used to retrieve the value of an attribute. 
A setter - set the value of an attribute. 
A deleter - delete the value of an attribute. 
https://www.youtube.com/watch?v=jCzT9XFZ5bw&ab_channel=CoreySchafer

Very important:
The getter, setter and deleter methods must have the same name!!!
But their name must be different to the attribute instantiated by __init__.
https://stackoverflow.com/a/17395735
"""

class Student:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.fullname = name + ' ' + surname
		"""
		Note: even if we use:
		self.fullname = self.name + ' ' + self.surname
		it still won't help us, because the attribute self.fullname is defined once, during instantiation
		We'd still have to change it manually apart from changing self.name.
		"""

	def get_fullname(self):  # a traditional method to access the name
		return self.name + ' ' + self.surname

	def set_name_and_fullname(self, value):  # a traditional method to modify the name
		self.name = value
		self.fullname = value + ' ' + self.surname


student = Student('Monica', 'Smith')
print(student.fullname)  # access the name using the attribute
print(student.get_fullname())  # access the name using the method

print("-".center(10, "-"))
student.name = 'John'
print(student.fullname)
print(student.get_fullname())

"""
The attribute 'fullname' displays the old name because its value for this instance has not changed!
This attribute's value for the instance 'student' was defined once, during instantiation - it was 'Monica Smith'.
To change it now for this instance, we would have to do:
	student.fullname = 'John Smith'
	
On the other hand, the method get_fullname() doesn't have a problem with this because every time it is called,
it grabs the current value of self.name and self.surname for this instance.
As we have now updated self.name, it will grab the updated value.

Naturally, we want to avoid updating the 'fullname' attribute as well, in addition to updating 'name'.
One way of doing it is just to define an internal method within the class:
"""

print("-".center(10, "-"))
student.set_name_and_fullname('Bob')
print(student.fullname)
print(student.get_fullname())

"""
Clearly, that's very ugly. We can change both 'name' and 'fullname' with one command, but still, we have to think in 
advance about which attributes need to be included within set_name_and_fullname.

Another way would be to stick to:
	student.name = 'John'  # outside the class definition
then delete:
	self.fullname = name + ' ' + surname  # from __init__.
Then, to print the full name, we could just use the method student.fullname() (once we delete self.fullname, 
we can rename get_fullname() to fullname() ) instead of the attribute student.fullname.
The downside is that this could potentially break the rest of the code for us (and potentially other users) 
because we would have to add () everywhere.

Instead, we'd like to have a neat command which can update both name and fullname AND act like student.fullname(), 
but be callable as an attribute, not a method.
For that purpose, we use a @property decorator.
"""

print("-".center(50, "-"))
class Student:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		# deleted the attribute we want to control with @property

	# Note: the name of the method decorated by @property cannot be the same as the attribute it refers to!
	@property  # a getter
	def fullname(self):
		return self.name + ' ' + self.surname

	@fullname.setter  # a setter - note the name is the same as defined under @property above!
	def fullname(self, value):
		self.name, self.surname = value.split(' ')

	@fullname.deleter  # a deleter - note the name is the same as defined under @property above!
	def fullname(self):
		print('Deleting name!')
		self.name, self.surname = None, None
		# del self.name

# create a new Student object
student = Student("Mark", "Corrigan")

# Now access the name using the getter:
print(student.fullname)  # like an attribute, without ()

# Modify the fullname using the setter
student.fullname = 'Alan Johnson'  # like an attribute, without ()

print(student.fullname)  # the fullname is updated
print(student.name)  # individually, name and surname are updated as well!
print(student.surname)

# Delete the name using the deleter
del student.fullname  # like an attribute, without ()

# print(student.name)  # prints an error
