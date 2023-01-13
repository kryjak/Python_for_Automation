print(f'__name__ in function_18.py = {__name__}')

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    try:
        assert b != 0, 'Dividing by 0'
    except AssertionError as e:
        return (e)
    else:
        return a / b

def not_needed():
    print(f'This content should only be executed if the function is called from a script, not a module')
    return None

if __name__ == '__main__':
    not_needed()

# The print statement in not_needed will be executed if we run this function from this script
# But if this function is called when running a different file (i.e. it is imported into that file), then
# it will not be printed because that file's __name__ != this file's __name__
