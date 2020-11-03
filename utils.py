# Twitter API credentials
import os

import tweepy

consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_key = os.environ.get("TWITTER_ACCESS_KEY")
access_secret = os.environ.get("TWITTER_ACCESS_SECRET")


def get_user_timeline(screen_name, count, max_id):
    # test2
    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    new_tweets = api.user_timeline(screen_name=screen_name, count=count, max_id=max_id)
    return new_tweets
