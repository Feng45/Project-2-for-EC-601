import os
import unittest

from tweepy import Status

import Tweepy_file
import Tweeter_time
import google1
import utils


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)


class TweepyFileTestCase(unittest.TestCase):

    def test_get_new_tweets(self):
        res = Tweepy_file.get_new_tweets("@TheDailyShow")
        self.assertEqual(isinstance(res[0], Status), True)
        self.assertEqual(len(res), 10)


class TestGooleJsonFile(unittest.TestCase):

    def test_google_json_file(self):
        tmp = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        with open("google.json", "w") as f:
            f.write(tmp)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google.json"
        text_content = "Google, headquartered in Mountain."
        google1.analyze_entity_sentiment(text_content)

class TweepyTimeTestCase(unittest.TestCase):

    def test_get_new_tweets_time(self):
        res = Tweeter_time.tweeter_time("@TheDailyShow")
        self.assertEqual(isinstance(res[0], Status), True)
        self.assertEqual(len(res), 10)
