"""
First-class functions in Python
"""

"""
A programming language is said to have first-class functions if its functions as treated as first-class citizens.
A first-class citizen/object is an entity which supports all the operations generally available to other entities.
These typically include being passed as an argument, returned from a function or assigned to a variable.
https://www.youtube.com/watch?v=kr0mpwqttM0&ab_channel=CoreySchafer
"""

print("ASSIGN A FUNCTION TO A VARIABLE".center(50, "-"))

def square(n):
	return n * n

f = square(5)  # This is NOT what we mean above - this is assigning the result of a function to a variable

print(square)
print(f)

print("-".center(10, "-"))
f = square  # This is assigning the function to a variable
# if we did f = square(), that would mean that the function square would execute, which is not what we want

print(square)
print(f)

print("PASS A FUNCTION AS AN ARGUMENT".center(50, "-"))
# map() is an example of passing a function as an argument:
numbers = [1, 2, 3, 4, 5]

print(list(map(square, numbers)))  # again, note square, NOT square()

print("RETURN A FUNCTION FROM A FUNCTION".center(50, "-"))
# First, consider the following example:

def logger(msg):
	def log_message():
		print('Log:', msg)

	return log_message()

log_hi = logger('Hi!')  # prints 'Log: Hi!' because log_hi is assigned to the execution: log_message()
print(type(log_hi))

print("-".center(10, "-"))
"""
Here, log_hi is equal to log_message(), i.e. the execution of the inner function - in this case, 'Log: Hi!'
But it is not callable
Now consider the following modification: 
return log_message 
instead of:
return log_message()
"""
def logger(msg):
	def log_message():
		print('Log:', msg)

	return log_message

log_hi = logger('Hi!')  # Now, this prints nothing because log_hi is assigned to log_message, not its execution!
print(type(log_hi))  # log_hi is indeed a function, not its execution!

# Therefore, we can call this function at any later time:
log_hi()  # Now it prints 'Log: Hi!'

print("-".center(10, "-"))
"""
An important point to note here is that log_hi() remembers the original argument passed to logger, i.e. at the
stage of log_hi = logger('Hi!')
This is an example of a 'closure'.
Let's see how this can be useful:
"""

def html_tag(tag):
	def wrap_text(msg):
		print(f'<{tag}>{msg}<>{tag}')

	return wrap_text

print_h1 = html_tag('h1')
print_h1('Test headline')
print_h1('Another headline')

print_p = html_tag('p')
print_p('Test paragraph')
print_p('Another paragraph')
