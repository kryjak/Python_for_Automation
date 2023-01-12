"""
In Python, we have For and While loops.
They are very similar to Mathematica, so I will only point out some more interesting behaviour here.
"""

# Unlike languages like C,C++,... we can use 'else' in loops. When the loop condition of "for" or "while" statement
# fails then code part in "else" is executed. If a 'break' statement is executed inside the for loop then the "else"
# part is skipped.

# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
count = 0
while count < 5:
    print(count)
    count += 1
else:  # When the condition is no longer satisfied, this statement is executed
    print(f"count value reached {count}")

print("-".center(50, "-"))
# Prints out 1,2,3,4
for i in range(1, 6):
    if i == 3:
        # break  # 3 is not printed, and then the loop stops
        continue  # 3 is not printed, but then the loop continues
    print(i)
else:  # When the condition is no longer satisfied, this statement is executed
    print("This text is displayed if 'continue' is used, but not if 'break' is used.")

print("-".center(50, "-"))
# We also have the 'pass' statement, which acts as a Null placeholder for a piece of code:
if 2 < 10:
    pass  # Note no error is returned
    print('Hello after pass')

print("-".center(50, "-"))
# We can do a loop over any iterable object, e.g. a tuple, list, dictionary of even a string:
for char in "python":
    print(f'{char} --> {"python".find(char)}')

print("-".center(50, "-"))
for item in {'a': 'AAA', 'b': 'BBB'}:  # A loop over a dictionary prints only the keys!
    print(item)

print("-".center(50, "-"))
for item in {'a': 'AAA', 'b': 'BBB'}.items():  # Now it will print the full item
    print(item)

print("-".center(50, "-"))
for x, y in ([1, 2], (3, 4), "ab", {'a': 'AAA', 'b': 'BBB'}):  # Multiple variables and mixed types are fine.
    print(x, y)

print("-".center(50, "-"))
# Note the behaviour of range:
print(range(5))
print(list(range(5)))
