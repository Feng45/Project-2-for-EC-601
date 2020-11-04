# !/usr/bin/env python
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import json
import sys
import csv # write the program to a cvs file
import codecs
import datetime
import xlsxwriter
from datetime import datetime
import os


# Twitter API credentials
consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_key = os.environ.get("TWITTER_ACCESS_KEY")
access_secret = os.environ.get("TWITTER_ACCESS_SECRET")

# get the tweets from this specific tweeter user
# the account has to be public
# This code is worked based on the code in the two links below
# https://gist.github.com/alexdeloy/fdb36ad251f70855d5d6
# https://stackoverflow.com/questions/49731259/tweepy-get-tweets-between-two-dates
def tweeter_time(screen_name):

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)


    # reference to https://stackoverflow.com/questions/15232465/how-to-repeat-try-except-block
    # catch error when the user input is not valid and ask user to re-enter until correct input date
    date_entry = input('Enter a date in the form (i.e. 2017,7,1)')
    while True:
        try:
            year, month, day = map(int, date_entry.split(','))
            break  # Only triggered if input is valid...
        except ValueError:
            print("Error: Invalid number")
            date_entry = input('Enter a date in the form (i.e. 2017,7,1)')
    startDate = datetime(year, month, day)

    tweets = []
    # retrieve all tweets
    try:
        new_tweets = api.user_timeline(screen_name=screen_name)
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

    for tweet in new_tweets:
        if tweet.created_at > startDate:
            tweets.append(tweet)

    try:
        while (new_tweets[-1].created_at > startDate):
            # give user a prompt, showing that the function is loading tweets successfully
            print("Last Tweet @", new_tweets[-1].created_at, " keep loading")
            # catch error if the user input time is too early,
            # exceeding system capacity

            new_tweets = api.user_timeline(screen_name=screen_name, max_id=new_tweets[-1].id)
            for tweet in new_tweets:
                if tweet.created_at > startDate:
                            tweets.append(tweet)

    except:
        # catch any additional error
        # reference to: https://stackoverflow.com/questions/4990718/about-catching-any-exception
        print("The date enter is too old, tweepy only able to retrieve 3200 tweets ")
        sys.exit(1)

    # print the tweets to an excel file
    workbook = xlsxwriter.Workbook(screen_name + ".xlsx")
    worksheet = workbook.add_worksheet()
    row = 0
    for tweet in tweets:
        worksheet.write_string(row, 0, str(tweet.id))
        worksheet.write_string(row, 1, str(tweet.created_at))
        worksheet.write(row, 2, tweet.text)
        worksheet.write_string(row, 3, str(tweet.in_reply_to_status_id))
        row += 1

    workbook.close()
    print("Excel file ready")

    # write tweet objects to JSON
    # this is unselected input, which gives you all the information of the tweets in a JSON file
    file = open('tweet.json', 'w')
    print("Writing tweet objects to JSON please wait...")
    for status in tweets:
        json.dump(status._json, file, sort_keys=True, indent=4)
    # close the file
    print("Done")
    file.close()

    # write the output to a cvs file
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in tweets]
    # write the csv
    with open('%s_tweets.csv' % screen_name, mode='w', encoding='utf-8') as f:
        print("Writing tweet objects to csv please wait...")
        writer = csv.writer(f)
        # title of the tweets
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(outtweets)
        print("Done")
    pass


if __name__ == '__main__':
    # pass in the username of th e account you want to download
    tweeter_time("@TheDailyShow")