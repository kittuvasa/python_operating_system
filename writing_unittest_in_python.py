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

class TestRearrange(unittest.TestCase):
 def test_basic(self):
  testcase = "brooklyn, chase"
  expected = "chase brooklyn"
  self.assertEqual(rearrange_func(testcase), expected)

unittest.main()
#########################

# when dealing with edge cases, sometimes it pays tp be pessimist - a person who tends to see the worst aspect of things or believe that the worst will happen.


