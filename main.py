import twitter_grabber as tg
import storage_mangement as sm

def main():
    
    grabber = tg.grabber(tg.APIKEY,tg.APIKEYSECRET,tg.BEARERTOKEN)
    grabber.initialize_Client()
    tweets = grabber.search_Recent_Tweets("(elon musk) lang:en -is:retweet -is:reply",100,None,None,None,['public_metrics','created_at'],None,None)
    store = sm.storage()
    store.add_Twitter_Data(tweets)
    print(store.baseDataFrame)
    
    
if __name__ == "__main__":
    main()