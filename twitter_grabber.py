import tweepy

# Twitter API authentication keys
BEARERTOKEN = ""
APIKEY = ""
APIKEYSECRET = ""
ACCESSTOKEN = ""
ACCESSTOKENSECRET = ""
# class for grabbing tweets from twitter
class grabber:

    def __init__ (self,bearerToken,apiKey=None,apiSecrt=None,accToken=None,accSecret=None):
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
    

    def search_Recent_Tweets (self,query,startTime,endTime,sortOrder,tweetFields,expansions,maxResults,numpages):
        """
        ***pre condition: initialize_Client has been called***
        (self,str,int,str,str,str,list,list,int) -> response
        search twitter for tweets matching query up to specfied max results per page
        """
        try:
            response = tweepy.Paginator(self.client.search_recent_tweets,query,start_time=startTime,end_time=endTime,sort_order=sortOrder,tweet_fields=tweetFields,expansions=expansions,max_results=maxResults,limit=numpages)
            return response

        except Exception as e:
            print("an error occurred")
            print(e)

    