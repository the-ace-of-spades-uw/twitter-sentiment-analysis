import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from wordcloud import WordCloud
import pandas as pd
from ast import literal_eval
import numpy as np

# class for visualizing data through graphs 
class graph:
    def __init__ (self,tweetDataFrame):
        self.df = tweetDataFrame
        plt.style.use("seaborn")
        self.polarites = self.df["polarity"].to_numpy()
        self.times = pd.to_datetime(self.df["created_at"], format="%Y-%m-%d %H:%M:%S")
        self.cleanedText = self.df["cleaned_text"]
        self.likes = self.df["public_metrics"].apply(lambda x: literal_eval(str(x))["like_count"])
        self.engagementScore = self.df["engagement_score"]
        self.polarityPercents = None
        self.numRows = len(self.df.index)
        self.figs = []
        
    def calc_Polarity_Percentages (self):
        """
        (self) -> None
        calculate the fraction of the total amount of tweeets that are positive, negative, and neutral 
        """
        pct_pos = np.sum(self.polarites > 0) / self.numRows
        pct_neg = np.sum(self.polarites < 0) / self.numRows
        pct_neut = np.sum(self.polarites == 0) / self.numRows
        self.polarityPercents = np.array([pct_pos,pct_neg,pct_neut])
    
    def create_Pi_Chart (self):
        """
        ***pre condition: calc_Polarity_Percentages has been called***
        (self) -> None
        create a pi chart displaying the polarity percentages, fig stored in fig list for easy export 
        """
        fig, ax = plt.subplots()
        labels = ["Positive","Negative","Neutral"]
        colors = ["g","r","y"]
        explode = (0,0,0)
        ax.pie(self.polarityPercents,labels=labels,colors=colors,autopct='%1.1f%%',explode=explode,startangle=90,shadow=True)
        ax.set_title("Overall Percentage Sentiment")
        ax.legend(title="Sentiment Polarity",loc='upper right',bbox_to_anchor=(1.2,0.95))
        self.figs.append(fig)
    
    
    def create_Word_Cloud (self):
        """
        (self) -> None
        create a wordcloud which displays a visualization of the most used words in the tweets, fig stored in fig list for easy export 
        """
        text = "".join(text for text in self.cleanedText)
        wordCloud = WordCloud(width = 1200, height = 800,background_color="white").generate(text)
        fig, ax = plt.subplots()
        ax.imshow(wordCloud)
        ax.set_title("Word Cloud of Query")
        ax.axis("off")
        self.figs.append(fig)
    
    def create_Time_vs_Polarity (self):
        """
        (self) -> None
        create a time vs tweet sentiment graph, fig stored in fig list for easy export 
        """
        fig, ax = plt.subplots()
        date_form = DateFormatter("%Y-%m-%d %H:%M:%S")
        ax.xaxis.set_major_formatter(date_form)
        ax.xaxis.set_major_locator(plt.MaxNLocator(3))
        ax.plot(self.times,self.polarites,"bo")
        ax.set(xlabel = "Time",ylabel = "Tweet Polarity",title = "Tweet Polarity vs Time",ybound=(-4,4))
        self.figs.append(fig)
    
    def create_Likes_vs_Polarity (self):
        """
        (self) -> None
        create a likes vs tweet sentiment graph, fig stored in fig list for easy export 
        """
        fig, ax = plt.subplots()
        ax.plot(self.likes,self.polarites,"bo")
        ax.set(xlabel = "Likes",ylabel = "Tweet Polarity",title = "Tweet Polarity vs Likes",ybound=(-1.1,1.1))
        self.figs.append(fig)
    
    def create_EngagementScore_vs_Polarity (self):
        """
        (self) -> None
        *** engagement score is defiend to be the sum of twitter public metrics e.g likes, retweets, replies ***
        create a engagement score vs tweet sentiment graph, fig stored in fig list for easy export 
        """
        fig, ax = plt.subplots()
        ax.plot(self.engagementScore,self.polarites,"bo")
        ax.set(xlabel = "Engagement Score",ylabel = "Tweet Polarity",title = "Tweet Polarity vs Engagement Score",ybound=(-1.1,1.1))
        self.figs.append(fig)

    def show(self):
        """
        (self) -> None
        show figures in interactive mode 
        """
        plt.show()




        
