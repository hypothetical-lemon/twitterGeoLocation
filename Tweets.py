#!/usr/bin/python3.7

import twitter
import json
from twitterConfig import TwitterConfig
from Sink import Sink

class Tweets(): 

    def __init__(self): 
        self.config = TwitterConfig() 
        self.api = twitter.Api(consumer_key=self.config.consumer_key, consumer_secret=self.config.consumer_secret,
                      access_token_key=self.config.access_key, access_token_secret=self.config.access_secret,
                      input_encoding=None)
        self.sink = Sink(host="redis", port="6357")

    def getTweets(self):
        stream = self.api.GetStreamFilter(track=['@realDonaldTrump'])
        try:
            for line in stream:
                print(json.dumps(line))
                self.sink.write(json.dumps(line))
        finally:
            stream.close()
        
def main():
    tweet = Tweets()
    tweet.getTweets()

if __name__ == "__main__":
    main()