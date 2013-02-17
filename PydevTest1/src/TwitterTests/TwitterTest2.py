'''
Created on Feb 16, 2013

@author: gagamama
'''
import twitter
import time

class TwitterTest2:
    isDebug = True
    
    api = twitter.Api(consumer_key='lgRiaJUULMnpTlGWzzoIg', 
                      consumer_secret='5ieV4bhABeP7YvZqnjWlZXNrdJpviqwIwezpdEIPqE', 
                      access_token_key='379568699-aihyWm8UT65OKPl4MIj3awTRMvJGFTY3O9xuw6dX', 
                      access_token_secret='gbq4uG7ofgN0NbQt62HHBM7PIU1YmPS1bH70b7tQ')
    
    smrtWords = ["#smrt", "@smrt"]
    breakdownWords = ["down", "stuck", "jam", "moving", "slow", "breakdown"]
#    searchResults = []
#    breakdownTweets = []
#    isBreakdownDetected = False
#    lastPollTime = 0
        
    def getCurrentTime(self):
        return time.time()
    
    def isTweetRelevant(self, tweet, list):
        for item in list:
            if (tweet.text.find(item) != -1):
                return True
        return False
        
    def main(self):
        print self.getCurrentTime()
    
if __name__ == '__main__':
    TwitterTest2().main()