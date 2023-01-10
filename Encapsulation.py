""""""
"""
Encapsulation - if we want to make a certain attribute or module 'private', i.e. not accessible from anywhere outside 
the class, we can do that by preceding the attribute/module name with __.
Moreover, we can make the attribute/module 'protected', i.e. accessible only within the class + its child classes in 
case of inheritance by using _ instead.

https://stackoverflow.com/questions/20261517/inheritance-of-private-and-protected-methods-in-python
Note: Python does not really have a notion of protected/private members, i.e. 'access' modifiers.
In fact, everything is public. The effect of declaring a variable private, __var, is that it is 'mangled', 
i.e. at compilation time such variables are replaced with _Class__var.
This is done to avoid conflicts in case of inheritance onto child classes, in which case their private variables are
replaced with _ChildClass__var.

But we can easily access even such private variable on the outside, using the mangled name: _ClassName__var.
"""

class Secret:
	def __init__(self, lvl, rcp):
		self.secret = 'This is a secret message.'
		self.__secrecy_level = lvl  # accessible only within Secret
		self._recipient = 'The recipient is ' + rcp  # accessible within Secret and its subclasses

	def get_secrecy_lvl(self):
		return 'The secrecy level is ' + str(self.__secrecy_level)

class Recipient(Secret):  # this class doesn't really make sense, but ok, just to demonstrate encapsulation
	def __init__(self, lvl, rcp):
		super().__init__(lvl, rcp)

	def recipient_list(self):
		return self._recipient
	# return self.__secrecy_level  # does not work
	# return self._Secret__secrecy_level  # works because we have used the mangled name of the private var

sensitive_data = Secret(10, 'NSA')
recipient = Recipient(99, 'CIA')

print("public".center(12, "-"))
print(sensitive_data.secret)
# print(sensitive_data.__secrecy_level)  # gives an AttributeError

print("private".center(12, "-"))
print(sensitive_data.get_secrecy_lvl())  # but we can access the attribute from within the class
# ...unless the method is defined as __get_secrecy_lvl
# We can also use 'name mangling': instance._ClassName__secret
print(sensitive_data._Secret__secrecy_level)

print("protected:".center(12, "-"))
# The child class is able to access the protected attribute, but not private ones
print(recipient.recipient_list())

# The protected attributes are also accessible from the outside - no mangling going on here:
print(recipient._recipient)
print(sensitive_data._recipient)

"""
Getters and setters allow us to implement a better encapsulation scheme
"""


print("-".center(50, "-"))
class Student:
	def __init__(self, name):
		self.__name = name

	@property  # a getter
	def name(self):
		return self.__name

	@name.setter  # a setter - note the name is the same as defined under @property above!
	def name(self, value):
		self.__name = value

student = Student('Alice')

# print(student.__name)  # AttributeError because it's private
print('student.name:', student.name)  # access using the getter

student.__name = 'Bob'  # let's do something stupid like that

print('student.name:', student.name)  # prints 'Alice' - the value of the private variable __name has not been changed
print('student.__name:', student.__name)  # this is treated as a different variable to student._Student__name,
# which is 'Alice'. For explanation of mangling, see Property.py

student.name = 'Charlie'  # modify using the setter

print('student.name:', student.name)  # equivalent to the mangled variable student._Student__name
