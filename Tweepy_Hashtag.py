# !/usr/bin/env python
# encoding: utf-8

import tweepy
import csv
import sys
# reference https://gist.github.com/vickyqian/f70e9ab3910c7c290d9d715491cde44c
# Twitter API credentials
import os


# Twitter API credentials
consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_key = os.environ.get("TWITTER_ACCESS_KEY")
access_secret = os.environ.get("TWITTER_ACCESS_SECRET")

def get_hashtag_tweets(hashtag, number):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    # Open/Create a file to append data
    if number > 2000:
        print("too many tweets retrieved, API will freeze")
        sys.exit(1)

    try:
        tweepy.Cursor(api.search, q=hashtag).items()
    except:
        # catch any additional error
        # reference to: https://stackoverflow.com/questions/4990718/about-catching-any-exception
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit(1)

    csvFile = open('%s_tweets1.csv' % hashtag, 'w')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["created_at", "text"])

    for tweet in tweepy.Cursor(api.search, q=hashtag,tweet_mode='extended').items(number):
        print(tweet.created_at, tweet.full_text)
        csvWriter.writerow([tweet.created_at, tweet.full_text.encode('utf-8')])
    
    return tweepy.Cursor(api.search, q=hashtag,tweet_mode='extended').items(number)

if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_hashtag_tweets("#VOTE",100)