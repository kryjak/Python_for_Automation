# The datetime module is used to work with dates and times (obviously...)
# The pytz module allows us to work with timezone information
import datetime
import sys

import pytz
import os  # for practice later on

print(dir(datetime))

date = datetime.datetime.now()
print(date)
print(date.year)  # We can do .attribute
print(type(date))  # Note a special type

print("-".center(50, "-"))
# strftime converts a datetime object into a string which can be analysed with 'format codes':
format_code = "%d %m %Y, %-H:%-M:%-S%p"
date_string = date.strftime(format_code)
print(date_string)
print(type(date_string))  # Note the output is now a string!
# The full list of format codes https://strftime.org/
# See also https://www.programiz.com/python-programming/datetime/strftime

print("-".center(50, "-"))
# We can use strptime for the reverse - converting a string to a 'datetime' object
format_code = format_code.replace('-', '')  # See https://stackoverflow.com/a/41191435 as for why this is necessary
datetime_object = datetime.datetime.strptime(date_string, format_code)
print(datetime_object)
print(type(datetime_object))  # Note the output is now a string!

"""
We can also view information about different times zones
View countries and their codes:
for key, val in pytz.country_names.items():
    print(key, '=', val, end=',')

View the timezones:
for key, val in pytz.country_timezones.items():
    print(key, '=', val, end=', ')`

Or view time zones in a particular country:
print(pytz.country_timezones['BR'])
"""

print("-".center(50, "-"))
my_timezone = pytz.timezone('America/Sao_Paulo')
print(datetime.datetime.now(my_timezone))  # Change time zone
print(type(my_timezone))  # Note the special type!
# print(datetime.datetime.now('America/Sao_Paulo'))  # This doesn't work, tz has to have a special format from pytz

print("-".center(50, "-"))
# timestamps are calculated from the Unix time: 00:00:00 UTC for 1 January 1970
time_stamp = datetime.datetime.timestamp(datetime_object)
print(time_stamp)
time = datetime.datetime.fromtimestamp(time_stamp)
print(time)

print("-".center(50, "-"))
# Minimum and maximum Unix time
print(datetime.datetime.min)
print(datetime.datetime.max)

print("PRACTICE".center(50, "-"))
# Write a script to look for files in a path that are older than n days
# path = input("Enter path: ")
path = "/home/jkrys/gitrepos/myfiniteflowexamples/amplitudes/2q2aW3pt"

if os.path.exists(path):
    if os.path.isdir(path):
        print('Valid directory')
        req_age = int(input("Enter required age (in days): "))
    elif os.path.isfile(path):
        print('Provide a directory, not a file.')
        sys.exit()
    else:
        print(f'Unknown type of {path}')
        sys.exit()
else:
    print('Directory does not exist.')
    sys.exit()

if len(os.listdir(path)) == 0:
    print('Directory empty')
    sys.exit()
else:
    time_now = datetime.datetime.now()
    print(path, "\n")
    for item in os.listdir(path):
        fullpath = os.path.join(path, item)
        if os.path.isfile(fullpath):
            timestamp = os.path.getctime(fullpath)
            creation_time = datetime.datetime.fromtimestamp(timestamp)
            print((time_now - creation_time))
            file_age = (time_now-creation_time).days
            if file_age >= req_age:
                print(f"{item} is {file_age} old")
