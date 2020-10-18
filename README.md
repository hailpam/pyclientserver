 # pyClientServer [![Build Status](https://travis-ci.org/hailpam/pyclientserver.svg?branch=master)](https://travis-ci.org/hailpam/pyclientserver)
Client-Server communication based on compressed JSON over TCP. Server returns compressed JSON data to the client for effective bandwidth usage.

## How to setup it
Client and Server instances read their parameters from 'src/settings.py'. Therefore, whatever special configuration is needed, put it there.


## How to run it
To run a test scenarion, proceed as follows:

1. Open a terminal and launch the server

	```bash
	> python src/startserver.py
	```

2. Open a new terminal window/tab and launch the client

	```bash
	> python src/startclient.py
	```


# Versions
- 0.1 First release: working scenario, ok compression.