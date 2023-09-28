#!/bin/bash
#sends a GET request to a URL with X-School-User-Id header and displays body of the response
curl -s -H "X-School-User-Id: 98" "$1"
