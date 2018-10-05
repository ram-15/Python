#pip install tweepy
#pip install textblob

import tweepy
from textblob import TextBlob
import csv


# Step 1 - Authenticate
consumer_key= 'aO2x6w4faG2iTPC63ljN6ipfV'
consumer_secret= 'IADL4LNi3WdyvY28n5nkvBTv5zZQRjBLyd1FtIAPSA3Tud1RRJ'

access_token='171892894-h22DvIMvheDfxiePYYOdPhM4lbKPSdPd1XKb0NhI'
access_token_secret='vmELNvfOe3ckhch5AbJHXUx1ucoHmGc23XzvjWUs5Yv1v'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('trump')

#Opening the dataset.csv filefor writinh the tweets in it
with open('tweets_file.csv', mode='w', encoding='utf-8') as tweets_file:
    tweet_writer = csv.writer(tweets_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    
    tweet_writer.writerow(['Tweet', 'Author', 'Date', 'Sentiment Polarity', 'label'])
    
    #Analyzing each tweet from the tweets list and storing it in a csv file
    for tweet in public_tweets:
        tweet_text = tweet.text
        tweet_user = tweet.user.name
        tweet_created_at = tweet.created_at
        tweet_sentiment = TextBlob(tweet_text).sentiment.polarity
        if tweet_sentiment > 0:
         label = 'positive'
        elif tweet_sentiment < 0:
         label = 'negative'
        else: 
         label = 'neutral'
        
        print(tweet_text, tweet_user, tweet_created_at)
        print("Sentiment is %f" % tweet_sentiment)
        tweet_writer.writerow([tweet_text, tweet_user, tweet_created_at, tweet_sentiment, label])
