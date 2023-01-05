"""
Lambda (anonymous) functions in Python
"""

"""
A lambda function is a special function type without a name. It's also known as an 'anonymous function'.
Instead of the 'def' keyword, we use 
lambda argument(s) : expression
https://www.programiz.com/python-programming/anonymous-function
"""
lambda_fun = lambda: print('Hello World')

lambda_fun()

# A lambda function can also accept (multiple) arguments:

lambda_fun = lambda name1, name2: print('Hello there,', name1, 'and', name2, '\b!')

lambda_fun('John', 'Mary')

# A useful application of lambda functions is in filter() and map().
# See Filter.py and Map.py for explanation and examples.
