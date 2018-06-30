#!/usr.bin.python

import json
import ISource
import sys
class FileSource(ISource.ISource):  
    
    def read(self, arg):
        filename = arg
        file = open(filename, 'r')
        try: 
            str = file.read()
            print(str)
        finally: 
            file.close()


    def readAll(self, arg, arg2):
        pass

def main(arg):
    source = FileSource()
    source.read(arg)

if __name__ == "__main__":
    main(sys.argv[1])