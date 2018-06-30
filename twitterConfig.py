#!/usr.bin.python

class TwitterConfig():

    def __init__(self):
         self.access_key = "Access Key"
        self.access_secret = "Access Secret"
        self.consumer_key='Consumer Key'
        self.consumer_secret='Consumer Secret'
        

    def verifyTwitter(self): 
        print(self.twitter.VerifyCredentials())
