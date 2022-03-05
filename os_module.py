import os
path = ""
os.remove(path) # delete the leaf path
os.rename("old_name", "new_anme")

# do verify/check the file exists
os.path.exists(path) # returns boolean T/F

os.path.getsize(path) # size in bytes
tedi_sec = os.path.getmtime(path) # terminology get modified unix time. 1 jan 1970s
import datatime
datetime.datetime.fromtimestamp(teid_sec) # year, month, date, 24 time

# to get absolute path from relative path
os.path.abspath(relative_path)

# to get current working directory cwd/pwd
os.getcwd()

# create dir/ remove dir/ change dir
os.mkdir("name_file")
os.rmdir("name_file") # throws an error if file isn't empty
os.chdir("name_dir") # change current working directory

# to list out the sub dir and files in a dir
os.listdir("dir")

dir = 'dir'
def list_dir_file:
  for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
       print("{} is a dir".format(fullname))
    else:
       print("{} is a file".format(fullname))
                         
                         

                         



