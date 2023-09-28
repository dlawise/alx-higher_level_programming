#!/bin/bash
#sends a JSON POST request with file contents in the body and displays the response body
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
