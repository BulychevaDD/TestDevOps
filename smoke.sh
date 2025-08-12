#!/bin/bash

set -e 

sleep 10

status_code=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/posts)

if [[ "$status_code" -eq 200 ]]; then
    exit 0
else
    exit 1
fi