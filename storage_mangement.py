import pandas as pd
import sentiment_analysis as sa
import tweet_cleaner as tc
import os

class storage:
    
    DIR = os.path.dirname(__file__)
    EXPORTSDIR = os.path.join(DIR,"exports")

    def __init__ (self):
        #id refers to tweet id, will be stroed as index for easy tweet look up
        #engangment score is a crude measurement of a tweets engangement, sum of number of likes, replies, retweets, and quotes
        self.baseDataFrame = pd.DataFrame({"timeCreated":[],"text":[], "cleanText":[], "polarity": [], "likeCount":[],"replyCount":[],"retweetCount":[],"quoteCount":[],"engagementScore":[]})
    
    def add_Twitter_Data (self,twitterResponse):
        print("***Porting Tweets***")
        for tweet in twitterResponse:
            time = tweet.created_at
            text = tweet.text
            cleanText = tc.cleaner.clean_Tweet_Simple(text)
            polarity = sa.sentimentAnalyzer.get_Polarity(cleanText)
            likes = tweet.public_metrics["like_count"]
            replies = tweet.public_metrics["reply_count"]
            retweets = tweet.public_metrics["retweet_count"]
            quotes = tweet.public_metrics["quote_count"]
            engagementScore = likes + replies + retweets + quotes 
            
            self.baseDataFrame.loc[tweet.id] = [time,text,cleanText,polarity,likes,replies,retweets,quotes,engagementScore]
        print("***Port Completed***")
    
    def export_to_CSV (self):
        pass
