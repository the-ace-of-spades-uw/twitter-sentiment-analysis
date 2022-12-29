import tweepy

# Twitter API authentication keys
APIKEY = "1Oz4DqoCRZGBCzzL7pGFXqMRS"
APIKEYSECRET = "SKeKP9HhLDY4aElmT2XQwqWy581W9vi93PJOZyAs2wV0mlW6za"
BEARERTOKEN = "AAAAAAAAAAAAAAAAAAAAAIURkAEAAAAAlAOjxJ0i7N0TupV1XWuhuUesqUc%3DrvqvEgIQ31ByFgfZKieAa4pBzoBXY0c5rVUblKJSTtyxRyVsuh"
ACCESSTOKEN = "1599073221298487296-lHYnaoZLeZPzrrwy9M1TB2Q3jtRjRm"
ACCESSTOKENSECRET = "vDtppi5DfQ1l72tQ45AzW3VS0pMcuWXnqLLSRMUsxHarX"
# class for grabbing tweets from twitter
class grabber:

    def __init__ (self,apiKey,apiSecrt,bearerToken,accToken=None,accSecret=None):
        self.apiKey = apiKey
        self.apiSecrt = apiSecrt
        self.bearerToken = bearerToken
        self.accToken = accToken
        self.accSecret = accSecret
        self.client = None
    
    def initialize_Client (self):
        """
        (self) -> None
        initialize tweepy client object
        """
        try:
            self.client = tweepy.Client(self.bearerToken,self.apiKey,self.apiSecrt,self.accToken,self.accSecret)

        except Exception as e:
            print("an error occurred")
            print(e)
    

    def search_Recent_Tweets (self,query,numTweets,startTime,endTime,sortOrder,tweetFields,expansions,maxResults):
        """
        ***pre condition: initialize_Client has been called***
        (self,str,int,str,str,str,list,list,int) -> response
        search twitter for tweets matching query up to numTweets
        """
        try:
            response = tweepy.Paginator(self.client.search_recent_tweets,query,start_time=startTime,end_time=endTime,sort_order=sortOrder,tweet_fields=tweetFields,expansions=expansions,max_results=maxResults).flatten(limit=numTweets)
            return response

        except Exception as e:
            print("an error occurred")
            print(e)

    