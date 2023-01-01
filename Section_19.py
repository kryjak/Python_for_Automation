"""
REGEX - regular expressions
Regex is a procedure to look for a specified pattern in a given text
We'll learn some basic pattern matching.
A nice tool to test your regex patterns:
https://regex101.com/

1. [ ] - square brackets represent possible characters:
   'Python[23]' = 'Python2' or 'Python3' (works like 'or')
   [^ ] complements the given set
2. \w - matches any single letter, digit or underscore
3. \W - not(\W)
4. \d - matches any letter 0-9
5. \D - not(\d)
6. . - matches any character except newline
   The normal dot can be searched for with \.
7. ^ - start of the string (or start of the line in case of multiline strings) (also complement for [ ])
8. $ - end of the string (or end of the line case of multiline strings)
9. \A -matches if the specified pattern is at the beginning of the string
10. \Z -matches if the specified pattern is at the end of the string
11. \b - matches if the specified pattern is at the beginning OR end of the word
12. \B - not(\b)
13. \t, \n, \r, \f, \v - tab, newline, carriage return, form feed, vertical tab
14. \s - matches any whitespace character (equivalent to [ \t\n\r\f\v])
15. \S - not(\s)
16. {n} - exactly n times
	{n,m} - exactly n, n+1, ... or m times
	{n,} - exactly n or more times
	+ - exactly one or more times (equivalent to {1,}
	* - exactly zero or more times (equivalent to {0,}
	? - once or no times (equivalent to {0,1}
17. | - or
18. ( ) - group, e.g.: (a|b|c)xy means axy or bxy or cxy
"""

import re

my_string = 'mate, method4, microscope, mom, music2022, myth, m , m@te'
print(my_string)

print('\'m[aei]\':', re.findall('m[aei]', my_string))  # [...] acts like 'or'
print('\'m[a-i]\':', re.findall('m[a-i]', my_string))
print('\'m[a-ix-z]\':', re.findall('m[a-ix-z]', my_string))
# Note: \'not space between i and x. Otherwise, the pattern will match 'm '
# Note: [0-37] means [01237], not [01234567]
# Note: [^abc] means any character that is not a, b or c
print('\'\\w\':', re.findall('\w', my_string))  # note no space or @ matched
print('\'\\w\\w\':', re.findall('\w\w', my_string))
print('\'\\w\\w\\w\':', re.findall('\w\w\w', my_string))

print('\'\\W\':', re.findall('\W', my_string))  # any character not in \w
print('\'\\W\\W\':', re.findall('\W\W', my_string))
print('\'\\W\\W\\W\':', re.findall('\W\W\W', my_string))

print('\'\\d\':', re.findall('\d', my_string))  # number 0-9
print('\'\\d\\d\'', re.findall('\d\d', my_string))
print('\'\\d\\d\\d\':', re.findall('\d\d\d', my_string))

print('\'.\':', re.findall('.', my_string))  # any character
print('\'..\':', re.findall('..', my_string))
print('\'...\':', re.findall('...', my_string))

print('\'^m[a-i]\':', re.findall('^m[a-i]', my_string))  # at the start of the string (or start of line in multiline strings)
print('\'te$\':', re.findall('te$', my_string))  # note the 'te' from the first 'mate' is not matched, only from 'm@te'

print("-".center(50, "-"))
foo_string = 'football, my foo, confoosion'
print(foo_string)

print('\'\\\\bfoo\':', re.findall('\\bfoo', foo_string))
print('\'\\\\Bfoo\':', re.findall('\\Bfoo', foo_string))
# why the double backlash? Because \b has a special meaning - it's the backspace character. See:
# https://stackoverflow.com/questions/50496846/why-are-double-backslashes-for-word-boundary-regular-expressions-but-single-bac
# https://stackoverflow.com/questions/33582162/confused-about-backslashes-in-regular-expressions?noredirect=1&lq=1

# We can also use 'raw strings':
print('r\'\\bfoo\':', re.findall(r'\bfoo', foo_string))
print('r\'\\Bfoo\':', re.findall(r'\Bfoo', foo_string))

print('r\'\\t\':', re.findall(r'\t', 'This	is	a	test	string.'))
# https://stackoverflow.com/questions/2054627/how-do-i-change-tab-size-in-vim
# Why are tabs different lengths? https://vi.stackexchange.com/questions/3973/why-are-tab-characters-variable-width

print("-".center(50, "-"))
aaa_string = 'aamaaazing prograaaaming'
print(aaa_string)
print('\'a{3}\':', re.findall('a{3}', aaa_string))
print('\'a{2,3}\':', re.findall('a{2,3}', aaa_string))
print('\'a{2,}\':', re.findall('a{2,}', aaa_string))

# Note the difference:
print("-".center(50, "-"))
xyz_string = 'xz, xyz, xyyz, xyyyz, xyyyyz'
print(xyz_string)
print('\'xy{2}z\':', re.findall('xy{2}z', xyz_string))
print('\'xy{2,3}z\':', re.findall('xy{2,3}z', xyz_string))
print('\'xy{2,}z\':', re.findall('xy{2,}z', xyz_string))

print('\'xy{1,}z\':', re.findall('xy{1,}z', xyz_string))
print('\'xy+z\':', re.findall('xy+z', xyz_string))  # Same thing

print('\'xy{0,}z\':', re.findall('xy{0,}z', xyz_string))
print('\'xy*z\':', re.findall('xy*z', xyz_string))  # Same thing

print('\'xy{0,1}z\':', re.findall('xy{0,1}z', xyz_string))
print('\'xy?z\':', re.findall('xy?z', xyz_string))  # Same thing

print("-".center(50, "-"))
"""
Flags:
re.I = re.IGNORECASE - case-insensitive
re.M = re.MULTILINE - ^/$ will match at the beginning/end of each line, not just the beginning/end of a string
"""
new_string = 'this is the first This line\nThis is the second line.\nthis is the third line.'
print(new_string)

print('\'This\' :', re.findall('This', new_string))  # all matches
print('\'This\' with re.I:', re.findall('this', new_string, re.I))  # case insensitive
print('\'^This\':', re.findall('^This', new_string))  # matches only on at the start of the string
print('\'^This\' with re.M:', re.findall('^This', new_string, re.M))  # matches at the start of each line
print('\'^This\' with re.I and re.M:', re.findall('^This', new_string, re.I | re.M))  # combine two flags

print("-".center(50, "-"))
# Search looks through the entire string and returns only the first match
print(new_string)
match_ob = re.search('This', new_string)
print('match:', match_ob)  # search returns only the first match
print('match type:', type(match_ob))  # special type
print('group:', match_ob.group())  # matched pattern
print('re:', match_ob.re)  # passed regex
print('string:', match_ob.string)  # passed string
print('span:', match_ob.span())  # index span
print('start:', match_ob.start())  # start index
print('end:', match_ob.end())  # end pattern

print("-".center(50, "-"))
# Match looks for the pattern only at the start of the string
print(new_string)
match_ob = re.match('This', new_string)
print('match:', match_ob)  # search returns only the first match
new_string = 'This is the first This line\nThis is the second line.\nthis is the third line.'
print(new_string)
match_ob = re.match('This', new_string)
print('match:', match_ob)  # search returns only the first match
print(type(match_ob))  # special type
print(match_ob.group())  # return the matched pattern
print(match_ob.start())  # return the start index
print(match_ob.end())  # return the end pattern

print("-".center(50, "-"))
# Note that re.findall does not return any information about the matches, only the matches themselves
# If we want to extract the information as well, we can use re.finditer.
# findall returns a list, finditer returns an iterator(match objects)
print(new_string)

matches = re.finditer('tHiS', new_string, re.I)
print('matches of finditer():', matches)

for match in matches:
	print(match)

print("-".center(50, "-"))
split_string = re.split(r'\bis\b', new_string, maxsplit=2)  # maxsplit sets the number of times the string is split
print('split_string:', split_string)

sub_string = re.sub(r'\bis\b', 'XXX', new_string, count=2)  # count sets the number of times the string is replaced
print('sub_string:', sub_string)

subn_string = re.subn(r'\bis\b', 'XXX', new_string, count=2)  # returns a tuple (new string, #substitutions made)
print('subn_string:', subn_string)

print("-".center(50, "-"))
pattern = re.compile(r'\bis\b', flags=0)  # Compiles a pattern object on which re operations can be performed
print('pattern:', pattern)
print(pattern.split(new_string, maxsplit=2))
# re.findall(pattern, new_string) == re.compile(pattern).findall(new_string)
