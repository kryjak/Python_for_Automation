# ---------------------------------- CONDITIONAL STATEMENTS ----------------------------------------
# Note the ':' after if and else. Also note that if and else need to have an equal indentation.
# a = eval(input('Enter first number: '))
# b = eval(input('Enter second number: '))
a = 10
b = -2
if a > b:
    print('a is greater than b')
elif a < b:
    print('b is greater than a')
else:
    print('a is equal to b')  # the structure should be if...elif...elif...else
# elif a == b:
#     print('a is equal to b')  # we can also use another elif as the last one

# Practise
num = eval(input('Enter your number: '))
num_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10:'ten'}

if num in range(1, 11):
    print(num_dict.get(num))
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
else:
    print(f"{num} is not in the range")
