"""
Shutil provides high-level commands on files or dirs
https://www.programiz.com/python-programming/examples/copy-file
"""

import shutil

print(dir(shutil))
# print(help(shutil))

src = '/home/jkrys/Desktop/Programming/Python for Automation/Exercises/newfile.txt'
dst = '/home/jkrys/Desktop/Programming/Python for Automation/Exercises/newfile_backup.txt'

shutil.copyfile(src, dst)  # copy data from src to dst in the most efficient way possible
shutil.copy(src, dst)  # copy data and permission modes - equivalent to cp src dst (same permissions)
shutil.copy2(src, dst)  # above + copy metadata (creation/modification time, etc)

shutil.copymode(src, dst)  # copy permissions, but not the actual file
shutil.copystat(src, dst)  # above + copy metadata (but not the actual file)

file1 = open(src, 'r')
file2 = open(dst, 'w')
shutil.copyfileobj(file1, file2)  # copy file-like object to a file-like object (does not copy permissions or metadata)
file1.close()
file2.close()

srcdir = '/home/jkrys/Desktop/Programming/Python for Automation/Exercises/walkdirectory'
dstdir = '/home/jkrys/Desktop/Programming/Python for Automation/Exercises/walkdirectory_backup'

shutil.copytree(srcdir, dstdir)  # copy a directory tree recursively
shutil.rmtree(dstdir)  # remove a directory tree
