"""
---------------------------------------- OS MODULE ---------------------------------------
The OS module is used to work/interact with operating system to automate tasks such as:
creating/removing directories, identifying current directories, listing files, etc.
"""
import os
import platform
import sys

# print(help(os))
print(os.sep)  # path separator used by the system

cwd = os.getcwd()
print(cwd)  # current working directory
os.chdir("/home/jkrys")
print(os.getcwd())  # new working directory
os.chdir(cwd)  # back to original working directory

print(f'ls: {os.listdir()}')  # List directories and files
print(f'ls in /home/jkrys/: {os.listdir("/home/jkrys")}')  # specify a path

os.mkdir("my_new_directory")
# To create a directory recursively, this does not work:
# os.mkdir("my_new_directory2/new/dirs/folder/")
os.makedirs("my_new_directory_rec/new/dirs/folder/")  # same as mkdir, but can create dirs recursively
print(f'ls again: {os.listdir()}')

os.rename("my_new_directory", "test_directory")
# print(f'List directories again: {os.listdir()}')

os.removedirs("my_new_directory_rec/new/dirs/folder/")  # same as rmdir, but can remove dirs recursively
os.rmdir("test_directory")

# print(os.environ)  # Environment variables
print(os.getpid())  # Get process id

# ---------------------------------------- OS.PATH -----------------------------------------
# os.path is a submodule of os. It is used to work on paths.
# print(help(os.path))
print("os.path()".center(120, "-"))

print(os.path.sep)
my_path = "/home/jkrys/gitrepos/myfiniteflowexamples/helicityamplitudes"
# basename returns last folder:
print("path.basename:", os.path.basename(my_path))
# dirname returns path to folder:
print("path.dirname:", os.path.dirname(my_path))
# split the path into head and tail:
print("path.split:", os.path.split(my_path))
# join two (or more) paths:
# Note no slash!!! Python automatically adds the path separator.
print("path.join:", os.path.join("/home/jkrys/gitrepos", "myfiniteflowexamples/helicityamplitudes"))
# getsize of a directory:
print("path.getsize:", os.path.getsize(my_path))
# Does a directory exist?:
print("path.exists:", os.path.exists(my_path))
# isfile?
print("path.isfile:", os.path.isfile(my_path))
# isdir?
print("path.isdir:", os.path.isdir(my_path))
# Links point to a file (soft link) or to an 'inode' (hard links). See the explanation:
# https://stackoverflow.com/questions/185899/what-is-the-difference-between-a-symbolic-link-and-a-hard-link
# Here, I created a link to a file in mfe. We can also create links to full directories.
# islink?
print("path.islink:", os.path.islink("crtmisids_link.m"))

# ------------------------------------- OS SYSTEM -------------------------------------
# os.system(command) allows us to execute OS commands in a subshell
print("os.system()".center(120, "-"))
print(os.system("pwd"))
print(os.system("cd"))  # 0 means command has executed successfully
# Note if we assign a variable to the command, e.g.: my_ls = os.system("ls"), print(my_ls) will just return 0,
# not the actual list of directories and files

"""
# ------------------------------------- PRACTICE -------------------------------------
# Write an OS-independent script to clear the terminal

# import platform  # Already imported above
# import os

my_OS = platform.system()

if my_OS == "Linux":
    os.system("clear")
elif my_OS == "Windows":
    os.system("cls")
else:
    print("The operating system is not recognised.")
"""

# ------------------------------------- OS WALK -------------------------------------
# os.walk(path) is used to generate directory and file names in a directory tree by 'walking'
print("os.walk(path)".center(120, "-"))

walk_path = "walkdirectory"
if os.path.exists(walk_path):
    os.system(f"rm -r {walk_path}")  # the point here is to remove the subdirectories as well
    os.mkdir(walk_path)

print(os.walk(walk_path))
print("Walk as a list:\n", list(os.walk(walk_path)))
# The output is a tuple consisting of [dir we provided, dirs inside, files inside]

# Now watch what happens when we create a directory inside:
if not os.path.exists(os.path.join(walk_path, "walksubdir")):
    os.mkdir(os.path.join(walk_path, "walksubdir"))

print("Updated list:\n", list(os.walk(walk_path)))  # The tree is constructed recursively
print("Different type of output:")  # Each line is a tuple
for pathh, dirs, files in os.walk(walk_path):
    if len(dirs) != 0 or len(files) != 0:
        print(pathh, dirs, files)  # When can assign a,b,c = (1, 2, 3) etc., just like in Mathematica

# ------------------------------------- PRACTICE -------------------------------------
# Write a script to do a system-wide search for a file

req_file = input("Enter the file name to search: ")
start_dir = input("Starting directory: ")

for pathh, dirs, files in os.walk(start_dir):
    for file in files:
        if req_file in file:
            print(os.path.join(pathh, file))
