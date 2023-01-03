import pandas as pd
import sentiment_analysis as sa
import tweet_cleaner as tc
import os

class storage:
    
    DIR = os.path.dirname(__file__)
    EXPORTSDIR = os.path.join(DIR,"exports")

    def __init__ (self):
        self.baseDataFrame = None
    
    def add_Twitter_Data (self,twitterResponse):
        print("***Porting Tweets***")
        self.baseDataFrame = pd.concat([pd.DataFrame(page.data) for page in twitterResponse])
        self.baseDataFrame["cleaned_text"] = self.baseDataFrame["text"].apply(tc.cleaner.clean_Tweet_Simple)
        self.baseDataFrame["polarity"] = self.baseDataFrame["cleaned_text"].apply(sa.sentimentAnalyzer.get_Polarity)
        self.baseDataFrame["engagement_score"] = self.baseDataFrame["public_metrics"].apply(lambda x: sum(dict.values(x)))
        self.baseDataFrame["created_at"] = self.baseDataFrame["created_at"].dt.tz_localize(None)
        self.baseDataFrame.set_index('id',drop=False,inplace=True)
        print("***Port Completed***")
    
    def export_to_CSV (self,tittle):
        self.baseDataFrame.to_csv(os.path.join(storage.EXPORTSDIR,tittle + ".csv"))
        print("data exported to csv")
    
    def export_to_Excel (self,tittle):
        self.baseDataFrame.to_excel(os.path.join(storage.EXPORTSDIR,tittle + ".xlsx"))
        print("data exported to excel file")

    def export_to_JSON (self,tittle):
        self.baseDataFrame.to_json(os.path.join(storage.EXPORTSDIR,tittle + ".json"))
        print("data exported to JSON")