import pandas as pd
import sentiment_analysis as sa
import tweet_cleaner as tc
import matplotlib.backends.backend_pdf
import os

# class for storgae of data and file I/O
class storage:
    
    # relative paths to folders
    DIR = os.path.dirname(__file__)
    EXPORTSDIR = os.path.join(DIR,"exports")
    IMPORTSDIR = os.path.join(DIR,"imports")

    def __init__ (self):
        self.baseDataFrame = None
    
    def add_Twitter_Data (self,twitterResponse):
        """
        (self,generator) -> None
        port paginated twitter response into twitter data frame 
        """
        print("***Porting Tweets***")
        self.baseDataFrame = pd.concat([pd.DataFrame(page.data) for page in twitterResponse])
        self.baseDataFrame["cleaned_text"] = self.baseDataFrame["text"].apply(tc.cleaner.clean_Tweet_Simple)
        self.baseDataFrame["polarity"] = self.baseDataFrame["cleaned_text"].apply(sa.sentimentAnalyzer.get_Polarity)
        self.baseDataFrame["engagement_score"] = self.baseDataFrame["public_metrics"].apply(lambda x: sum(dict.values(x)))
        self.baseDataFrame["created_at"] = self.baseDataFrame["created_at"].dt.tz_localize(None)
        print("***Port Completed***")
    
    def export_to_CSV (self,title):
        """
        (self,str) -> None
        export the stored data to a CSV file
        """
        self.baseDataFrame.to_csv(os.path.join(storage.EXPORTSDIR,title + ".csv"),index=False)
        print("data exported to CSV")
    
    def export_to_Excel (self,title):
        """
        (self,str) -> None
        export the stored data to a excel file
        """
        self.baseDataFrame.to_excel(os.path.join(storage.EXPORTSDIR,title + ".xlsx"),index=False)
        print("data exported to excel file")

    def export_to_JSON (self,title):
        """
        (self,str) -> None
        export the stored data to a JSON file, stored in table format
        """
        self.baseDataFrame.to_json(os.path.join(storage.EXPORTSDIR,title + ".json"),orient="table",index=False)
        print("data exported to JSON")
    
    def import_from_CSV(self,title):
        """
        (self,str) -> None
        import data from a CSV file into the data frame
        """
        self.baseDataFrame = pd.read_csv(os.path.join(storage.IMPORTSDIR,title + ".csv"))
        print("data imported from CSV")
    
    def import_from_Excel (self,title):
        """
        (self,str) -> None
        import data from a Excel file into the data frame
        """
        self.baseDataFrame = pd.read_excel(os.path.join(storage.IMPORTSDIR,title + ".xlsx"))
        print("data imported from excel file")
    
    def import_from_JSON (self,title):
        """
        (self,str) -> None
        import data from a JSON file into the data frame, must be in table format
        """
        self.baseDataFrame = pd.read_json(os.path.join(storage.IMPORTSDIR,title + ".json"), orient="table")
        print("data imported from JSON")
    
    def save_figs_to_PDF (self, title, figslist):
        """
        (self,str, list) -> None
        store a list of matplotlib figures to a single PDF
        """
        pdf = matplotlib.backends.backend_pdf.PdfPages(os.path.join(storage.EXPORTSDIR,title + ".pdf"))
        for fig in figslist:
            pdf.savefig(fig)
        pdf.close()
        print("figures saved to PDF")