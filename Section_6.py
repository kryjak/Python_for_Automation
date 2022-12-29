"""
In this section, we will learn operators in Python. We will go through several types of operators:
1. Arithmetic  -
2. Assignment  - take values as inputs, perform operations on them and return values
3. Comparison
4. Identity
5. Membership - take values as inputs, perform operations on them and return True or False
6. Logical
7. Bitwise - take True or False as inputs, perform operations on them and return values

For more information, see:
https://www.programiz.com/python-programming/operators
"""

# ------------------------------ ARITHMETIC AND ASSIGNMENT OPERATORS -------------------------------------------
# Arithmetic operators: addition, subtraction, multiplication, division, exponential, modulo, floor division
# Exponential is inserted with **:
a = 5
b = 3
print(f"a**b = {a ** b}")
# Modulo is inserted with %:
print(f"a%b = {a % b}")
# Floor division is inserted with //:
print(f"a//b = {a // b}")
# Note floor division with negative values:
print(f"-a//b = {-a // b}")

# Assignment operators: =, +=, -=, *=, /=, %=, **=
a += b
print(f"a+=b = {a}")
a **= b
print(f"a**=b = {a}")

# ------------------------------ COMPARISON OPERATORS -------------------------------------------
# Comparison operators: ==, !=, >, <, <=, >=
# Note we can actually compare two strings:
print(f"\'a\' < \'b\': {'a' < 'b'}")
# How is that done? Based on Unicode codes:
print(ord('a'))
print(chr(97))

# ------------------------------ IDENTITY OPERATORS -------------------------------------------
# The operators 'is' and 'is not' test for object identity: x is y is true if and only if x and y are the same object.
# Another way of thinking about this is: do they point to the same memory location?
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]

print(x1 is not y1)  # prints False
print(x2 is y2)  # prints True
print(x3 is y3)  # prints False, because even though x3 and y3 are equal, they are not identical!
# x3 and y3 occupy different memory locations:
print(f"id(x3) = {id(x3)}, id(y3) = {id(y3)}")

# ------------------------------ MEMBERSHIP OPERATORS -------------------------------------------
# The operators 'in' and 'not in' test if a value/variable is in a string/list/tuple/dictionary
# In a dictionary we can only test for presence of key, not the value.
dict1 = {1: 'a', 2: 'b'}
# check if '1' key is present in dict1
print(1 in dict1)  # prints True
# check if 'a' key is present in dict1
print('a' in dict1)  # prints False

# ------------------------------ LOGICAL OPERATORS -------------------------------------------
# Logical operators: 'and', 'or', 'not'
print('and?:', 1 < 3 and 5 > 7)
print('or?:', 1 < 3 or 5 > 7)
print('not?:', not 5 > 7)
# Note a shortcut for 'and'
print('all?', all([2 < 3, 3 < 4, 4 < 5, 5 < 6]))
# Note a shortcut for 'any'
print('any?', any([2 > 3, 3 > 4, 4 > 5, 5 < 6]))

# Operator precedence: NOT > AND > OR.
# The full table can be found at: https://www.programiz.com/python-programming/precedence-associativity
print(not 2 < 4 or 1 < 3)  # Because it evaluates 'not' first: print(False or True)
print(not (2 < 4 or 1 < 3))  # Because it evaluates the bracket first: print(not True)

# ------------------------------ BITWISE OPERATORS -------------------------------------------
# Bitwise operators are '&' - and, '|' - or, '~' - not, '^' - xor, '>>' - bitwise shift right, '<<' - bitwise shift left
# They act on operands as if they were strings of binary digits, operating bit by bit
a = 5  # 0000 0101
b = 3  # 0000 0011

# bitwise 'and'
print("and: ", a & b)  # 0000 0101 and 0000 0011 = 0000 0001 = 1

# bitwise 'or'
print("or: ", a | b)  # 0000 0101 or  0000 0011 = 0000 0111 = 7

# bitwise 'not'
"""
The bitwise not operation is not easy to understand. First, convert the 'a' value to binary and apply not to the 
individual bits. Then, the first bit is the sign bit - it tells us whether the number is positive (0) or negative 
(1). How are negative numbers represented in binary notation in Python? A number -x in binary is not(binary of (x - 1)).
For example, to represent -10 in binary, we take 10 - 1 = 9 = 0000 1001 and flip the bits, so that:
-10 = 1111 0110
Coming back to the above example, the bitwise not operation leaves us with 1111 1010, which means that this is
a negative number. We need to swap the bits, add 1 and take the negative:
0000 0101 = 5, add 1: 6, and take the negative: -6.
For practical purposes: ~a = -(a+1).
Note that all this works only on signed integers!
"""
print("not: ", ~a)  # not 0000 0101 = 1111 1010 = -(0000 0101 + 1) = -(5 - 1) = -6

# bitwise 'xor'
"""
Xor returns True only if and only if 1 of the inputs is True:
00 ->0, 10 -> 1, 01 -> 1, 11 -> 0
Note that for more than two inputs, this definition changes to:
Return 1 iff an odd number of inputs is 1
So that, e.g.: 101 -> 0, but 111 -> 1
"""
print("xor: ", a ^ b)  # 0000 0101 xor 0000 0011 = 0000 0110 = 6

# bitwise left-shift and right-shift by 'n' positions
print("left-shift: ", a << 2)  # 0000 0101 << 2 = 0001 0100 = 20
print("right-shift: ", a >> 2)  # 0000 0101 >> 2 = 0000 0001 = 1
# note the value does not get wrapped around and reappear and txvcxxcxccxcxe other side
