"""
Iterators in Python
https://www.programiz.com/python-programming/iterator
"""
import itertools

"""
In Section_15.py, we have seen the difference between an 'iterable' and an 'iterator'.
Technically, an iterator must have two special methods: __iter__() and __next__().
For example, each list has __iter__, because a list is an iterable, but it does not have __next__.
On the other hand, an iterator has both (it has __iter__ because every iterator is an iterable).
We use __iter__ to create an iterator from an iterable and __next__ to skip to the next item of the iterator.
"""

my_list = [3, 4, 5, 6, 7]
my_iterator = iter(my_list)

print(dir(my_list))  # __iter__
print(dir(my_iterator))  # __iter__ and __next__

"""
The behaviour of the iterator in the for loop might be confusing.
Every time the code within 'for' is executed, the iterator is assigned the value of the next element in the iterable.
In the example below, 'it' is given the value 3 at the first run, then 4.
At the third run, the iterator moves on to 5, hence it == 5, but then using 'next', we move the iterator's 
value to 6. That's why 
	print(next(my_iterator))  # prints 6
but
	print(it**2)  # prints 25
When Python enters the loop again, the iterator automatically moves on to the next element, which is 7.
Therefore, 36 is skipped and the final number printed is 49.
"""

for it in my_iterator:
	if it == 5:
		print(next(my_iterator))
	print(it**2)

print("-".center(10, "-"))
# Note that this is equivalent to using 'continue', but shifted one element further:
for it in iter(my_list):  # needed to create a new iterator because my_iterator at this point is exhausted!
	if it == 6:
		print(it)
		continue
	print(it**2)

print("CUSTOM ITERATORS".center(50, "-"))
# We can also create a custom iterator from scratch:

class PowTwo:
	def __init__(self, start=0, stop=0, stepsize=1):
		self.stop = stop
		self.start = start
		self.stepsize = stepsize

	def __my_iter__(self):
		self.n = self.start
		return self

	# def current_stepsize(self):
	# 	return self.stepsize

	# def __my_next__(self, newstepsize=current_stepsize()):
	# 	if newstepsize != self.stepsize:
	# 		# self.stepsize = newstepsize
	# 		pass

	# pass an argument to __my_next__ to temporarily override the default stepsize
	# How to set the default value of tmpstepsize to self.stepsize?
	def __my_next__(self, tmpstepsize=1):
		if tmpstepsize != self.stepsize:
			self.stepsize = tmpstepsize

		if self.n <= self.stop:
			result = 2 ** self.n
			self.n += self.stepsize
			return result
		else:
			raise StopIteration


numbers = PowTwo(3, 10, 1)
# numbers = PowTwo(3, 10, 2)  # Don't know how to implement cases where stepsize > 1

iterator = numbers.__my_iter__()

print(iterator.__my_next__())  # default is to move one by one
print(iterator.__my_next__(3))  # move to the third next item (i.e. skip the next two)
print(iterator.__my_next__())
print(iterator.__my_next__())
print(iterator.__my_next__())


print("INFINITE ITERATORS".center(50, "-"))
# We can also create an infinite operator using a function that increments by 1 every time it is called

from itertools import count

infinite_iterator = itertools.count(1)  # this iterator will never end

for i in range(5):
    print(next(infinite_iterator))
