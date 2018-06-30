#!/usr.bin.python

class ISource():

    def read(self): 
        raise NotImplementedError

    def readAll(self): 
        raise NotImplementedError

    