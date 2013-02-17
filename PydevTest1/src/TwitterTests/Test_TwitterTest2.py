'''
Created on Feb 18, 2013

@author: gagamama
'''
import unittest
import twitter
from TwitterTest2 import TwitterTest2


class Test(unittest.TestCase):


    def setUp(self):
        self.cls = TwitterTest2()
        self.tweet = twitter.Status()

    def tearDown(self):
        pass


    def test_isTweetRelevant_False_smrt(self):
        self.tweet.text = "smrt"
        self.assertFalse(self.cls.isTweetRelevant(self.tweet, self.cls.smrtWords))
        
    def test_isTweetRelevant_False_empty(self):
        self.tweet.text = ""
        self.assertFalse(self.cls.isTweetRelevant(self.tweet, self.cls.smrtWords))
        
    def test_isTweetRelevant_True_atsmrt(self):
        self.tweet.text = "@smrt"
        self.assertTrue(self.cls.isTweetRelevant(self.tweet, self.cls.smrtWords))
        
    def test_isTweetRelevant_True_hashsmrt(self):
        self.tweet.text = "#smrt"
        self.assertTrue(self.cls.isTweetRelevant(self.tweet, self.cls.smrtWords))

    def test_isTweetRelevant_True_down(self):
        self.tweet.text = "train break down today"
        self.assertTrue(self.cls.isTweetRelevant(self.tweet, self.cls.breakdownWords))
        
    def test_isTweetRelevant_True_breakdown(self):
        self.tweet.text = "train breakdown today"
        self.assertTrue(self.cls.isTweetRelevant(self.tweet, self.cls.breakdownWords))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()