#Editing Files using Substrings

#findJane.sh file
////////////////
#!/bin/bash

>oldFiles.txt

files=$(grep " jane " ../data/list.txt | cut -d" " -f3)

for i in $files;do
if test -e $HOME$i;then
echo $HOME$i >> oldFiles.txt
fi
done


/////////////
# changeJane.py file

#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1]) as file:
 line_list = file.readlines()
 for line in line_list:
  old_name = line.strip()
  new_name = old_name.replace("jane", "jdoe")
  subprocess.run(["mv", old_name, new_name])
