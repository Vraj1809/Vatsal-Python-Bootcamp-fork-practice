'''
Write a Python unit test program to check if a function correctly parses and validates input data. 
'''
import unittest

def valid_string(data):
    if type(data) ==str:
        return True
    return False

def is_palindrome(data):
    temp = data[::-1]
    if temp==data:
        return 1
    return -1

class TestValidate (unittest.TestCase):
    def test_fun1(self):
        data = "vatsal"
        self.assertTrue(valid_string(data))
    def test_fun2(self):
        data = "crest"
        self.assertTrue(valid_string(data))
    def test_fun3(self):
        data = "lol"
        self.assertEqual(is_palindrome(data),1)
    

if __name__=="__main__":
    unittest.main()