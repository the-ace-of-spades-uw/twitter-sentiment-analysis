
from textblob import TextBlob, WordList
from nltk.corpus import stopwords
import contractions
import emoji
import string
import re

"""test tweet: @mrslorijg New name for @LeCingola.  I’m going to Post.  But want to be here.  They made me get a new Twittter.
Its real!! I i got my ethereum!! @And23569173 @k_unsolved @yvonnea1220 @OregonMichael1 @DemirovicRafet @DINKA2025 @EmreKacar00 @jewel_lly @milodibartolo @presi_twittter @ZaheerA98644811 @whiskey_420_ @Nicknameyoungk3 @Bexto404 https://t.co/3KYartQcoW
@obiiwys as I no get money, make I just come twittter dey vex😭😭🤣😡😡
Woow unprecedented generosity! Dont waste time! @HouseFromCrypto @StylinMotives @HorsesHeadz @DeWinnersClub @MehediH85779411 @MihaiSe49347902 @Dreasy81 @Yusuf001ys @jto2223 @AbraHamAlABid2 @CryptoD36082724 @Chochelafarm @presi_twittter @Selcuk_CSLife https://t.co/6in4lGSkVy
@mikeduncan I love magic Twittter juxtaposition. https://t.co/8T1ntXav0I
"""
class cleaner:

    stopwords = stopwords.words('english')

    @staticmethod
    def make_Lower (tweetText):
        return str.lower(tweetText)
    
    @staticmethod
    def remove_Numbers (tweetText):
        text = re.sub("[0-9]+","",tweetText)
        return text
    
    @staticmethod
    def remove_emojis (tweetText):
        text = emoji.replace_emoji(tweetText)
        return text

    @staticmethod
    def remove_contractions (tweetText):
        text = re.sub(u"(\u2018|\u2019)", "'", tweetText)
        text = contractions.fix(tweetText)
        return text

    @staticmethod
    def remove_Hashtag_And_Mentions (tweetText):
        text = re.sub("#[A-Za-z0-9_]+","",tweetText)
        text = re.sub("@[A-Za-z0-9_]+","",text)
        return text
    
    @staticmethod
    def remove_Links (tweetText):
        text = re.sub(r"http\S+","",tweetText)
        text = re.sub(r"www.\S+","",text)
        return text
    
    @staticmethod #maybe just clean up to here
    def remove_Punctuation (tweetText):
        text ="".join([char for char in tweetText if char not in string.punctuation])
        return text
    
    @staticmethod
    def tokenize (tweetText):
        return TextBlob(tweetText).words
    
    @staticmethod
    def remove_Stop_Words (tweetTextTokenized):
        text = [token for token in tweetTextTokenized if not token in cleaner.stopwords]
        return text
    
    @staticmethod
    def lemmatize (textList):
        text = WordList(textList).lemmatize()
        return text
    
    @staticmethod
    def make_Sentence (wordList):
        Sentence = [token + " " for token in wordList]
        Sentence = "".join(Sentence)
        return Sentence
    
    @staticmethod
    def clean_Tweet_Simple (tweetText):
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
        text = cleaner.clean_Tweet_Simple(tweetText)
        text = cleaner.tokenize(text)
        text = cleaner.remove_Stop_Words(text)
        text = cleaner.lemmatize(text)
        text = cleaner.make_Sentence(text)
        return text