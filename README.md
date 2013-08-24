pyClientServer
==============

Client-Server communication based on compressed JSON over TCP. Server returns compressed JSON data to the client for effective bandwidth usage.


How to setup it
===============

Client and Server instances read their parameters from 'src/settings.py'. Therefore, whatever special configuration is needed, put it there.


How to run it
=============

To run a test scenarion, proceed as follows:

1. Open a terminal and launch the server

	> python src/startserver.py

2. Open a new terminal window/tab and launch the client

	> python src/startclient.py


Versions
========

	1.0 First release: working scenario, ok compression.
