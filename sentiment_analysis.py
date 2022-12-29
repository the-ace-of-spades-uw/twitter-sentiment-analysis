from textblob import TextBlob

class sentimentAnalyzer:

    @staticmethod
    def get_Polarity (tweetText):
        tweetBlob = TextBlob(tweetText)
        polarity = tweetBlob.polarity
        return polarity
    
    @staticmethod
    def get_Subjectivity (tweetText):
        tweetBlob = TextBlob(tweetText)
        subjectivity = tweetBlob.subjectivity
        return subjectivity
    