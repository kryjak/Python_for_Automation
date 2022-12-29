"""
CSV - Comma Separated Values
I's a simple file format used to store tabular data, such as a spreadsheet or a database
"""

import csv

# print(help(csv))

req_file = "/home/jkrys/Desktop/Programming/Python for Automation/Exercises/csvdata.csv"

fo = open(req_file, 'r')
# content = fo.readlines()  # Don't use that for csv files
content = csv.reader(fo)
print(type(content))  # Special type - csv.reader

for each in content:  # has to be included before close()
    print(each)

print(f"Content as a list: {list(content)}")
fo.close()

print("-".center(50, "-"))
fo = open(req_file.replace('csvdata', 'csvdata2'), 'r')
content = csv.reader(fo, delimiter='|')  # Change the delimiter
content_list = list(content)  # csv.reader returns an iterator, which can be iterated over only once! See below

for each in content_list:
    print(each)

print(f"Content as a list: {content_list}")
fo.close()

"""
Interlude - difference between an iterator and an iterable object.
An 'iterable' is an object that can be iterated over. It produces a new iterator each time we pass it into the iter() 
function or use it in a for loop.
An 'iterator' is an object representing a data stream. We can think of it as having a pointer which keeps track of 
which part of the data we are at.
Every time we call the iterator, successive items in the streams are returned. When no more items are available, 
StopIteration exception is raised.
At this point, the iterator is exhausted and further calls to it with the next() method return the same exception.

Every iterator is also an iterable object, but not every iterable is an iterator.

https://stackoverflow.com/questions/25336726/why-cant-i-iterate-twice-over-the-same-data
https://docs.python.org/3/glossary.html#term-iterator
https://www.geeksforgeeks.org/python-difference-iterable-iterator/

my_list = [1,2,3]
my_list_iterator = iter(my_list)
print('list type:', type(my_list))
print('iter(list) type', type(my_list_iterator))  # Similarly, we have str_iterator etc

print("-".center(10, "-"))
for it in my_list:
    print(it**2)

print("-".center(4, "-"))
for it in my_list:  # That's fine. A new iterator is created from the list, which is an iterable
    print(it**2)

print("-".center(10, "-"))
for it in my_list_iterator:
    print(it**2)
    # At this point, the iterator is exhausted
print("-".center(4, "-"))
for it in my_list_iterator:
    print(it**2)  # Nothing is printed

# We can manually move the iterator to the next position:
print("-".center(10, "-"))
new_iter = iter(my_list)
for it in new_iter:
    if it == 1:
        next(new_iter)  # Move the iterator to the next position. Similar to 'skip'
    print(it**2)
    
"""

# Write a new csv file
print("-".center(50, "-"))
filename = "/home/jkrys/Desktop/Programming/Python for Automation/Exercises/csvdata3.csv"

fo = open(filename, 'w+')  # the + is just so that we can read the file we'll create
content = csv.writer(fo, delimiter='|')  # The comma can be skipped as it's the default setting
# .writerow for writing individual rows
content.writerows([['Name', 'Gender', 'Age'], ['Maria', 'F', '46'], ['John', 'M', '34']])

# Move the pointer to the top and see what we have written:
fo.seek(0)
print(fo.read())

fo.close()
