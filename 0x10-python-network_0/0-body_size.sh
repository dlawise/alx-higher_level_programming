#!/bin/bash
#sends a request to a URL and displays size of the response body in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}' 
