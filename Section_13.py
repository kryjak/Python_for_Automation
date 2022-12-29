"""
subprocess module
"""

import subprocess
import os

# print(help(subprocess))

# Note the behaviour:
out = os.system("ls -lthr")  # prints the command output, but returns the exit code!
print(f"out: {out}")

"""
The store the output as a variable, we use the 'subprocess' module

sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
or
sp = subprocess.Popen(cmd.split(), shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
cmd should be given as a string if shell=True (will make the OS open a new shell), e.g. 'ls -lthr'
cmd should be given as a list   if shell=False, e.g. ['ls', '-lthr']
Whenever cmd depends on an environmental variable, e.g. $HOME, $PATH, etc. we need to use shell=True.
Otherwise, we can use shell=False, which is quicker because it doesn't have to open an extra shell.
(On Windows, we should always take shell=True, otherwise most commands won't work)

universal_newlines=True separates the output into new lines and gets rid of the b (bit) output
"""

print("-".center(50, "-"))
sp = subprocess.Popen('ls -lthr', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
rc = sp.wait()  # Wait for this process to finish
out, err = sp.communicate()  # A tuple of two value
print(f'The return code is {rc}')
print(f'The output is:\n{out}')
print(f'The error is {err}')  # No error because the process has executed successfully
print(f'\nThe output as a list:\n{out.splitlines()}')  # The output will be converted to a list

print("PRACTICE".center(50, "-"))
# Find the bash version using the subprocess module
bash_pr = subprocess.Popen(['bash', '--version'], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           universal_newlines=True)
rc = bash_pr.wait()  # Wait for this process to finish
out = bash_pr.communicate()[0].splitlines()

if rc == 0:
    for string in out:
        if 'version' in string:
            pos = string.find('version')
            pos2 = string.find('(', pos)
            print(string[pos + len(' version'):pos2])
            break
else:
    print('The command has failed')

print("PRACTICE 2".center(50, "-"))
# Find the bash version using the subprocess module
java_pr = subprocess.Popen(['java', '-version'], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           universal_newlines=True)
rc = java_pr.wait()  # Wait for this process to finish
out = java_pr.communicate()[1].splitlines()  # Note java -version is returned as stderr, not stdout

if rc == 0:
    for string in out:
        if 'version' in string:
            out_list = string.split()
            pos = out_list.index('version')
            print(out_list[pos + 1].strip('"'))
            break
else:
    print('The command has failed')
