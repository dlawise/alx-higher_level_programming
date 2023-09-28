#!/bin/bash
#sends a GET request to a URL and displays body of the response for a 200 status code
curl -s -o /dev/null -w "%{http_code}\n" "$1" | grep -q 200 && curl -s "$1"
