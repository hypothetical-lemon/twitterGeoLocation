#!/bin/bash
scp -P 62226 Dockerfile dlemon@dereklemon.com:~/heatherpi
scp -P 62226 *.py dlemon@dereklemon.com:~/heatherpi/
scp -P 62226 requirements.txt dlemon@dereklemon.com:~/heatherpi/
ssh dlemon@dereklemon.com -p 62226 "cd ~/heatherpi;docker build -t htown/twitteringest ."
