"""
JSON - JavaScript Object Notation is a popular data format used for representing structured data
It's a commonly used format to transfer data between a server and a web application
"""

import json
# print(help(json))

req_file = "/home/jkrys/Desktop/Programming/Python for Automation/Exercises/jsondata.json"

fo = open(req_file, 'r')
content = json.load(fo)
print(content)
print(type(content))  # Imported JSON data is a dictionary
fo.close()

# Write a JSON file:
filename = "/home/jkrys/Desktop/Programming/Python for Automation/Exercises/jsondata2.json"
my_dict = {'Name': 'John', 'Gender': 'M', 'Age': 34}

fo = open(filename, 'w+')  # the + is just so that we can read the file we'll create
json.dump(my_dict, fo, indent=2)
# json.dump([1,2,3], fo, indent=2)

# Move the pointer to the top and see what we have written:
fo.seek(0)
print(fo.read())

fo.close()
