"""
Working with text files in Python.
Three modes:
r - read only (default)
w - write
a - append
x - The 'x' mode implies 'w' and raises an `FileExistsError` if the file already exists.
t - text mode (default)
b - binary mode
+ - update
e.g. 'r+b' means read and write in binary mode
r+ - open to read and write, without truncating - pointer at the top
w+ - open existing file with truncating or create a new one. Read and write - pointer at the top
a+ - open existing file without truncating or create a new one. Read and write - pointer at the bottom
For a detailed explanation of modes and pointer positions, see:
https://mkyong.com/python/python-difference-between-r-w-and-a-in-open/
"""

fo = open('newfile.txt', 'w')  # Kind of like streams in Mathematica
print('Mode:', fo.mode)  # which mode is the file open in?
print('Writeable?:', fo.writable(), '\b, Readable?:', fo.readable())  # is the file readable?

fo.write('This is the 1st line.\n')
fo.write('This is the 2nd line.\n')
fo.write('This is the 3rd line.\n')
fo.write('This is the 4th line.\n')

# print(fo.read())  # not allowed in 'w' mode
fo.close()

print("-".center(50, "-"))
fo = open('newfile.txt', 'r+')  # r+: read and write
# pointer is at the beginning of the file
fo.writelines(['This is the 5th line.\n', 'This is the 6th line.\n'])  # these two lines replace 1st and 2nd
# pointer is now at 3rd line:
print(f'r+ first read:\n{fo.read()}')  # Moves the pointer to the bottom
# pointer is now on the fifth line
fo.writelines(['This is the 7th line.\n', 'This is the 8th line.\n'])
fo.seek(0)  # Brings the pointer to the beginning to read the entire file
print(f'r+ second read:\n{fo.read()}')  # prints the updated file and moves the pointer to the bottom
# The first two lines have been replaced with 'fifth' and 'sixth'.
# This is because r+ can read and write the file, but the pointer position is at the beginning of the file!
fo.close()

print("-".center(50, "-"))
fo = open('newfile.txt', 'a+')  # read and append
# in a, pointer is at the bottom
print(f'a+ first read:\n{fo.read()}')  # Prints nothing because the pointer is at the end already
# now the pointer is automatically at the end of the file
fo.writelines(['This is the 9th line.\n', 'This is the 10th line.\n'])
fo.seek(0)  # Bring the pointer to the top again
print(f'a+ second read:\n{fo.read()}')

fo.seek(0)
print(f'a+ second read as a list:\n{fo.readlines()}')

fo.seek(10)
print(f'Read from current pointer position:\n{fo.readline()}')  # Read line from the current pointer position
fo.close()

# print(fo.tell())  # Get pointer position

print("-".center(50, "-"))
# Copy the contents of a file to another one
loremipsum = open('sampletext.txt', 'r')
readlorem = loremipsum.readlines()[0]
loremipsum.close()

fo = open('newfile.txt', 'a+')
fo.write(readlorem)
fo.seek(0)
print(f'File with appended loremipsum:\n{fo.read()}')
fo.close()
