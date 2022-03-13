''' regular expressions are powerful and flexible feature to extract the desired string pattern or format from a string and much more'''
import re # re - regular expression

'''grep is the linux command line tool help to implement regex, grep l.st file_loc (. is the wildcard) [re.findall(l.st, text)]
, grep ^fruit file_loc ( *line begin with fruit), grep cat$ file_loc (*line ends with cat)
The circumflex [^] and the dollar sign [$] are anchor characters.
'''
print(re.search(r"i.g", "bringing"))
print(re.search(r"^br", "bringing"))
print(re.search(r"ing$", "bringing"))
print(re.search(r"^br", "Bringing", re.IGNORECASE))
print(re.search(r"[!@a-zA-Z0-9]", "anystring"))
''' [] chracter class'''
print(re.search(r"[^a-zA-z]", "This is a complete sentence")) #returns first ' ' circumflex inside[] provides a way to find that aren't match with specifie
print(re.search(r"cats|dogs", "i like cats and dogs")) # | pipe allow to either or search 
print(re.search(r"py.*n", "python programming")) # repeatation qualifier * includes any number of character including 0 in it. output "python programmin"
print(re.search(r"py[a-z]*n", "python programming"))
print(re.search(r"o+l+", "goldfish")) # repeatation qualifier + includes the one or more occurence of character mentioned before
print(re.search(r"p?each", "i like each of you")) # repeatation qualifer ? includes the one or 0 occurence of character mention before
print(re.search(r"\.com", "github.com")) # \ backslash espace character to string utilise the special character .*+?^$[]
print(re.search(r"\w*", "thi3_ jkll")) # output thi3 \w matches the sequence of alphanumeric character including _

###############capturing groups - the portion of pattern inside parentheses
re.search(r"^(\w*), (\w*)","alexis adamas")





