import twitter_grabber as tg
import storage_mangement as sm
import time 
def main():
    t1 = time.perf_counter()
    grabber = tg.grabber(tg.BEARERTOKEN)
    grabber.initialize_Client()
    tweets = grabber.search_Recent_Tweets("(elon musk) lang:en -is:retweet -is:reply",None,None,None,['public_metrics','created_at'],None,10,1)
    storage = sm.storage()
    print(storage.baseDataFrame)
    t2 = time.perf_counter()
    print(t2-t1)
    
if __name__ == "__main__":
    main()