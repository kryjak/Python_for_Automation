"""
Closure in Python
"""

"""
Closure is a nested function that allows us to access variable of the outer function even after it is closed.
For a more step-by-step explanation, see First_class_functions.py
https://www.youtube.com/watch?v=swU3c34d2NQ&ab_channel=CoreySchafer
"""

def f1(n):
    def mod(modulus):
        print(n % modulus)

    return mod  # mod, NOT mod() as we want to assign the function itself, not its execution

check5 = f1(5)  # check5 is now equivalent to mod with n being 5 - we can call it
print(check5.__name__)

check5(2)
check5(3)

print("-".center(10, "-"))
check6 = f1(6)
check6(2)
check6(3)

print("-".center(50, "-"))

# Another example:

def calculate():
    num = 1

    def inner_func():
        nonlocal num
        num += 2
        return num

    return inner_func

"""
The nonlocal keyword is used to work with variables inside nested functions, where the variable we are
referencing should not belong to the local scope of the inner function, but also not the global scope.
In other words, we can use it to reference a variable defined in the local scope of the outer function.
https://www.geeksforgeeks.org/python-nonlocal-keyword/
"""

odd = calculate()

print(odd())
print(odd())
print(odd())

print("-".center(10, "-"))
odd2 = calculate()
print(odd2())
