import twitter_grabber as tg
import storage_mangement as sm
import grapher as g

# main method 
def main():
    
    # perform an analysis on a query 
    grabber = tg.grabber(tg.BEARERTOKEN)
    grabber.initialize_Client()
    response = grabber.search_Recent_Tweets("query",None,["created_at","public_metrics"],None,100,100)
    storage = sm.storage()
    storage.add_Twitter_Data(response)
    graph = g.graph(storage.baseDataFrame)
    graph.calc_Polarity_Percentages()
    graph.create_Pi_Chart()
    graph.create_Word_Cloud()
    graph.create_Time_vs_Polarity()
    graph.create_Likes_vs_Polarity()
    graph.create_EngagementScore_vs_Polarity()
    storage.export_to_CSV("filename")
    storage.save_figs_to_PDF("filename",graph.figs)
   
if __name__ == "__main__":
    main()