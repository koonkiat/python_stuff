'''
Created on Feb 16, 2013

@author: gagamama
'''
import twitter
class TwitterTest1:
    isDebug = True
    
    api = twitter.Api(consumer_key='lgRiaJUULMnpTlGWzzoIg', 
                      consumer_secret='5ieV4bhABeP7YvZqnjWlZXNrdJpviqwIwezpdEIPqE', 
                      access_token_key='379568699-aihyWm8UT65OKPl4MIj3awTRMvJGFTY3O9xuw6dX', 
                      access_token_secret='gbq4uG7ofgN0NbQt62HHBM7PIU1YmPS1bH70b7tQ')
    
    breakdownWords = ["down", "stuck", "jam", "moving", "slow"]
    searchResults = []
    breakdownTweets = []
    isBreakdownDetected = False
    lastPollTime = 0
        
    def search(self, searchStr):
        self.searchResults = self.api.GetSearch(searchStr, per_page=30)
        if self.isDebug:
            print 'Found %s searchResults.' % (len(self.searchResults))
    #        for status in searchResults:
    #            print status.text
    
    def collectBreakdownTweets(self):
        breakdownTweets = []
        for status in self.searchResults:
    #        print status.text
            for item in self.breakdownWords:
    #            if (status.GetCreatedAtInSeconds() > lastPollTime):
                if (status.text.find(item) != -1):
                    breakdownTweets.append(status)
                    if self.isDebug:
                        print "** Found \"", item, "\" in:\n", status.text
    
    def confirmBreakdown(self):
        self.isBreakdownDetected = False
        
    def main(self):
        self.search("#smrt")
#        @smrt
        self.collectBreakdownTweets()
        self.confirmBreakdown()
    
if __name__ == '__main__':
    TwitterTest1().main()