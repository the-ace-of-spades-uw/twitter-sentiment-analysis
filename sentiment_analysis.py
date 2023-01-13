from textblob import TextBlob

# Class for getting the sentiment of a tweet
class sentimentAnalyzer:

    @staticmethod
    def get_Polarity (tweetText):
        """
        (str) -> float
        return the sentiment of a tweet between -1 and 1
        """
        tweetBlob = TextBlob(tweetText)
        polarity = tweetBlob.polarity
        return polarity
    
    @staticmethod
    def get_Subjectivity (tweetText):
        """
        (str) -> float
        return the subjectivity score of a tweet's text
        """
        tweetBlob = TextBlob(tweetText)
        subjectivity = tweetBlob.subjectivity
        return subjectivity
    