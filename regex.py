''' regular expressions are powerful and flexible feature to extract the desired string pattern or format from a string and much more'''
import re # re - regular expression

'''grep is the linux command line tool help to implement regex, grep l.st file_loc (. is the wildcard) [re.findall(l.st, text)]
, grep ^fruit file_loc ( *line begin with fruit), grep cat$ file_loc (*line ends with cat)
The circumflex [^] and the dollar sign [$] are anchor characters.
'''
print(re.search(r"i.g", "bringing"))
print(re.search(r"^br", "bringing"))
print(re.search(r"$ing", "bringing"))
print(re.search(r"^br", "Bringing", re.IGNORECASE))
print(re.search(r"[!@a-zA-Z0-9]", "anystring"))
''' [] chracter class'''
print(re.search(r"[^a-zA-z]", "This is a complete sentence")) #returns first ' ' circumflex inside[] provides a way to find that aren't match with specifie
print(re.search(r"cats|dogs", "i like cats and dogs")) # | pipe allow to either or search 


