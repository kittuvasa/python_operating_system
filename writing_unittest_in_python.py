'''unit test are py file with name with isolated function or method name following _test suffix to it.
'''

# rearrange.py file
###############
import re
import sys

def rearrange_func(name):
 raw = "([\w .]*), ([\w .]*)"
 result = re.search(raw, name)
 return f"{result[2]} {result[1]}"
########################
# rearrange_test.py file
#################
from rearrange import rearrange_func
import unittest
'''The package unittest supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections,
and independence of the tests from the reporting framework. This module also provides classes that make it simple to support these qualities for a set of tests. '''

class TestRearrange(unittest.TestCase):
 def test_basic(self):
  testcase = "brooklyn, chase"
  expected = "chase brooklyn"
  self.assertEqual(rearrange_func(testcase), expected)

unittest.main()
#########################

# when dealing with edge cases, sometimes it pays tp be pessimist - a person who tends to see the worst aspect of things or believe that the worst will happen.

#black box/ opaque code test
'''the unit test code for a program is developed before the actual code is developed based on the specifications and requirements of the program '''
# white box/ transparent code test
'''the unit test code for a program is developed alogon side or after the actual code is developed the test cases are made with the knowledge of how software works'''

# Error and Exceptions
'''Let's dive into how try/except blocks work:

First, we execute the try clause.
If no exception occurs, the except clause is ignored.
If an exception occurs during the execution of the try clause, the rest of the try clause is then skipped.
It then attempts to match the type with the exception named after the except keyword. If this matches, the except clause is executed. If it doesn't, the control
is passed on to outer try statements. If no handler is found, it's an unhandled exception and the execution stops with an error message.
A try statement may have more than one except clause to specify handlers for different exceptions. In our case, the exception error we need to handle is IndexError. '''
# RAISE ERROR

def validate_username(name, minlen):
 assert type(name) == str, "invalid data type of name, str expected"
 if minlen<1:
  raise ValueError("minimum length of username atleast 1")
 if not name.isalnum():
  return False
 return True

# unit test for raise and assert error exceptino:
import unittest
from validations import valid_username

class TestvalidateUser(unittest.TestCase):
 def test_invalid_username(self):
  self.assertRaises(ValueError, valid_username, "name", -1)
  
  
  
  
 


