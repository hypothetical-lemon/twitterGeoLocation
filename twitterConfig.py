#!/usr.bin.python
import json


class TwitterConfig():

    def __init__(self):
        # Read in from file?  or take in additional params for constructions
        try:
            with open('config.json', 'r') as json_data_file:
                config = json.load(json_data_file)

                self.access_key = config['twitter_key']['access_key']
                self.access_secret = config['twitter_key']['access_secret']
                self.consumer_key = config['twitter_key']['consumer_key']
                self.consumer_secret = config['twitter_key']['consumer_secret']
        finally:
            json_data_file.close() 
        
def main():
    twitterConfig = TwitterConfig()

if __name__ == "__main__":
    main()