FROM ubuntu:18.04
LABEL HEATHER LEMON mcmillenh90@gmail.com 

ADD Tweets.py /
ADD requirements.txt /

RUN apt-get update && apt-get install -y python3.6 \
    python-pip python-redis

RUN pip install -r requirements.txt 
   
CMD /usr/bin/python3 twitterGeoLocation/Tweets.py