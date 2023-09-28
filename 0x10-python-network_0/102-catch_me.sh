#!/bin/bash
#makes a request to 0.0.0.0:5000/catch_me causing server to respond with "You got me!"
curl -s -X PUT -H "User-Agent: You got me!" 0.0.0.0:5000/catch_me -d "status=evil"
