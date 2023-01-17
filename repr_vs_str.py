"""repr vs str"""
import pytz

"""
The goal of str is to return a printable string, but it does not always return a string that is acceptable to eval().
The goal of repr is to return a printable string, in a form that is also acceptable to eval().

__repr__ is meant to be unambiguous
__str__  is meant to be readable
https://www.youtube.com/watch?v=5cvM-crlDvg&ab_channel=CoreySchafer
"""

import datetime

aa = datetime.datetime.now().replace(tzinfo=pytz.UTC)
bb = str(aa)

print(aa)
print("-".center(10, "-"))
print(str(aa))
print(str(bb))
print("-".center(10, "-"))
print(repr(aa))
print(repr(bb))
