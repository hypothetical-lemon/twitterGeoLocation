#!/usr.bin.python

class TwitterConfig():

    def __init__(self):
        # Read in from file?  or take in additional params for constructions
        self.access_key = "572118432-qBMhyhE48biyzrRHvYn8kjt6LvTKTvFt00hTnAHx"
        self.access_secret = "5JlEPxwTYunT0wF4aoGLJE40j8v67Gwx6BixjRt8FGQO1"
        self.consumer_key='NcWE9P5UP9UlhVJibPh3cVKxh'
        self.consumer_secret='xdSYoNZ2n9iaXXwiag5OFzQS74cTCYPUKwaulqENjVvs6BE5ec'
        

    def verifyTwitter(self): 
        print(self.twitter.VerifyCredentials())