
from textblob import TextBlob, WordList
from nltk.corpus import stopwords
import contractions
import emoji
import string
import re

# class for processing tweet data
class cleaner:

    stopwords = stopwords.words('english')

    @staticmethod
    def make_Lower (tweetText):
        """
        (str) - > str
        make tweet lower case
        """
        return str.lower(tweetText)
    
    @staticmethod
    def remove_Numbers (tweetText):
        """
        (str) -> str
        remove numbers from tweet
        """
        text = re.sub("[0-9]+","",tweetText)
        return text
    
    @staticmethod
    def remove_emojis (tweetText):
        """
        (str) -> str
        remove emojis from the tweet
        """
        text = emoji.replace_emoji(tweetText)
        return text

    @staticmethod
    def remove_contractions (tweetText):
        """
        (str) -> str
        remove contractions from the tweet
        """
        text = re.sub(u"(\u2018|\u2019)", "'", tweetText)
        text = contractions.fix(tweetText)
        return text

    @staticmethod
    def remove_Hashtag_And_Mentions (tweetText):
        """
        (str) -> str
        remove any hastags or mentions from the tweet
        """
        text = re.sub("#[A-Za-z0-9_]+","",tweetText)
        text = re.sub("@[A-Za-z0-9_]+","",text)
        return text
    
    @staticmethod
    def remove_Links (tweetText):
        """
        (str) -> str
        remove any typical links from the tweet
        """
        text = re.sub(r"http\S+","",tweetText)
        text = re.sub(r"www.\S+","",text)
        return text
    
    @staticmethod 
    def remove_Punctuation (tweetText):
        """
        (str) -> str
        remove punctuation from the tweet
        """
        text ="".join([char for char in tweetText if char not in string.punctuation])
        return text

    @staticmethod
    def tokenize (tweetText):
        """
        (str) -> TextBlob
        tokenzie the tweet
        """
        return TextBlob(tweetText).words
    
    @staticmethod
    def remove_Stop_Words (tweetTextTokenized):
        """
        (TextBlob) -> list
        remove stop words from tokens defined from a list of stop words
        """
        text = [token for token in tweetTextTokenized if not token in cleaner.stopwords]
        return text
    
    @staticmethod
    def lemmatize (textList):
        """
        (list) -> WordList
        take tokens down to there lemma
        """
        text = WordList(textList).lemmatize()
        return text
    
    @staticmethod
    def make_Sentence (wordList):
        """
        (WordList) -> str
        rejoin tokenized words back into sentences
        """
        Sentence = [token + " " for token in wordList]
        Sentence = "".join(Sentence)
        return Sentence
    
    @staticmethod
    def clean_Tweet_Simple (tweetText):
        """
        (str) -> str
        pefrom a simple clean of a tweet removing basic noise
        """
        text = cleaner.make_Lower (tweetText)
        text = cleaner.remove_Numbers (text)
        text = cleaner.remove_emojis (text)
        text = cleaner.remove_contractions (text)
        text = cleaner.remove_Hashtag_And_Mentions(text)
        text = cleaner.remove_Links(text)
        text = cleaner.remove_Punctuation(text)
        return text
    
    @staticmethod
    def clean_Tweet_Full (tweetText):
        """
        (str) -> str
        pefrom a more rigorous clean of a tweet 
        """
        text = cleaner.clean_Tweet_Simple(tweetText)
        text = cleaner.tokenize(text)
        text = cleaner.remove_Stop_Words(text)
        text = cleaner.lemmatize(text)
        text = cleaner.make_Sentence(text)
        return text