#!/usr/bin/python3.7

import json

from twitter import Twitter, OAuth

from twitterConfig import TwitterConfig


# from Sink import Sink
# Search for the latest tweets about #pycon
# t.search.tweets(q="#pycon")

class Tweets:

    def __init__(self):
        self.config = TwitterConfig()
        self.twitter_api = Twitter(auth=OAuth(token=self.config.token_key, token_secret=self.config.token_secret,
                                              consumer_key=self.config.consumer_key,
                                              consumer_secret=self.config.consumer_secret))

    def getTweets(self):
        # atream = self.twitter_api.users.lookup(screen_name="heather_lemon0")
        stream = self.twitter_api.users.lookup(screen_name="realDonaldTrump")
        # stream = self.twitter_api.stream('statuses/filter',  track=['@realDonaldTrump'])
        # stream = self.twitter_api.GetStreamFilter(track=['@realDonaldTrump'])
        try:
            for line in stream:
                print(json.dumps(line))
                # self.sink.write(json.dumps(line))
        except:
            print("error")


if __name__ == "__main__":
    tweet = Tweets()
    tweet.getTweets()
