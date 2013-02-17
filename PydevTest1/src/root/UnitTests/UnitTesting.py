'''
Created on Feb 17, 2013

@author: gagamama
'''
import unittest
from UnitTextTarget import UnitTextTarget

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testMultiply_straight_simple(self):
        a = 4
        b = 7 
        actual = UnitTextTarget().Multiply_straight(a,b)
        expected = UnitTextTarget().Multiply(a,b)
        self.assertEqual(actual, expected) 

    def testMultiply_straight_zero(self):
        a = 0
        b = 7 
        actual = UnitTextTarget().Multiply_straight(a,b)
        expected = UnitTextTarget().Multiply(a,b)
        self.assertEqual(actual, expected) 


    def testMultiply_branch_simple(self):
        a = 4
        b = 7 
        actual = UnitTextTarget().Multiply_branch(a,b)
        expected = UnitTextTarget().Multiply(a,b)
        self.assertEqual(actual, expected) 

    def testMultiply_branch_zero(self):
        a = 0
        b = 7 
        actual = UnitTextTarget().Multiply_branch(a,b)
        expected = UnitTextTarget().Multiply(a,b)
        self.assertEqual(actual, expected) 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()