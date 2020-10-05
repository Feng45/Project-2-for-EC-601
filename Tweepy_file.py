# !/usr/bin/env python
# encoding: utf-8


import tweepy  # https://github.com/tweepy/tweepy
import json
import sys
import csv # write the program to a cvs file
import codecs

# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


# get the tweets from this specific tweeter user
# the account has to be public
# It is developed on top of the sample code which is given in class
# https://drive.google.com/file/d/1dNahyZnwgqwUUdbV5I0u68b8pQADBiWi/view
def get_all_tweets(screen_name):

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all tweets from this user
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    # catch invalid inputs
    try:
        new_tweets = api.user_timeline(screen_name=screen_name, count=10)
    except tweepy.error.TweepError:
        print("The input contain unauthorized content, try another input")
        sys.exit(1)
        # save most recent tweets, use extend to save the files
    # catch any unexpected errors, such as twitter not responding
    except:
        # catch any additional error
        # reference to: https://stackoverflow.com/questions/4990718/about-catching-any-exception
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit(1)

    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        # printing reference https://stackoverflow.com/questions/30588792/python-3-tweepy-csv-encode/30715420
        print('getting tweets before %s' % (oldest))

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=10, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        # allow the program to give quick feedback
        # this will return the first 20 tweets of the user
        oldest = alltweets[-1].id - 1
        print("...%s tweets downloaded so far" % (len(alltweets)))
        if (len(alltweets) > 15):
            break
        print
        # code section 1
        # uncomment this to grab large quantity of tweets
        # this will run longer
        # reference http://pythonfiddle.com/twitter-scraper/
        '''
        if len(alltweets) > 0:
            oldest = alltweets[-1].id - 1
        else:
            pass
        print("...%s tweets downloaded so far" % (len(alltweets)))
        '''

    # write tweet objects to JSON
    # this is unselected input, which gives you all the information of the tweets in a JSON file
    file = open('tweet.json', 'w')
    print("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json, file, sort_keys=True, indent=4)
    # close the file
    print("Done")
    file.close()

    # code section 2
    # write to a csv file with selected information from tweeters
    # reference https://stackoverflow.com/questions/38881314/twitter-data-to-csv-getting-error-when-trying-to-add-to-csv-file
    '''
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]
    # write the csv
    with open('%s_tweets.csv' % screen_name, mode='w', encoding='utf-8') as f:
        print("Writing tweet objects to csv please wait...")
        writer = csv.writer(f)
        # title of the tweets
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(outtweets)
        print("Done")
    pass
    '''

if __name__ == '__main__':
    # pass in the username of th e account you want to download
    get_all_tweets("@TheDailyShow")