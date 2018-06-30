#!/usr.bin.python

import ISink 
import redis

class Sink: 

    def __init__(self, host='redis', port='6379'): 
        try:
            self.r = redis.Redis(
                host=host,
                port=port, 
                password='')
        finally:
            pass

    def write(self, data=""): 
        self.r.lpush("realDonaldTrump", data)

def main():
    sink = Sink(host="192.168.1.6", port="31536")
    sink.write() 

if __name__ == "__main__":
    main()
    