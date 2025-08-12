#!/bin/bash

status_code=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080)

if [[ "$status_code" -eq 200 ]]; then
    exit 0
else
    exit 1
fi