# environment variables relate to os. hence we use os module
# source of input of our program can be user input, env and command line arguments even exit status.
import os
#The os module provides a portable way of using operating system dependent functionality with Python.


# we can get content of environment variables using environ dict present in os module
print("PATH:", os.environ.get("PATH","")) # windows cmd echo %variable_name%

# LINUX command to create env - export FRUIT=PINEAPPLE

#######################
# command line arg, parameters taht are passes to a program when it's started
# file.py
import sys
#The sys module provides information about the Python interpreter's constants, functions, and methods.
print(sys.argv)

# run file.py one two three
# output- ["one", "two", "three"]

#########subprocess
import subprocess
print(subprocess.run(["date"]))
print(subprocess.run(["sleep","2"])) # here the interpreter is unvailabel for 2 second until the child process complete
x = subprocess.run(["ls","file_not_exist"])# return object contain "returncode" attribute value 2. error
x.returncode # 2 erro!
#Obtaining the Output of a System Command
result = subprocess.run(["host",'8.8.8.8'],capture_output = True)
print(result.returncode)
print(result.stdout) #output is in form of byte array. a byte can represent only 256 character but thousands of character out there. so we use several specification techique called
# encoding (UTF-8)indicates which sequence of bytes represent which characters.
print(result.stdout.decode())





