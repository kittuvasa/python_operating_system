# environment variables relate to os. hence we use os module
# source of input of our program can be user input, env and command line arguments even exit status.
import os

# we can get content of environment variables using environ dict present in os module
print("PATH:", os.environ.get("PATH","")) # windows cmd echo %variable_name%

# LINUX command to create env - export FRUIT=PINEAPPLE

#######################
# command line arg, parameters taht are passes to a program when it's started
# file.py
import sys
print(sys.argv)

# run file.py one two three
# output- ["one", "two", "three"]





