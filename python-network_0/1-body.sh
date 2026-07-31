#!/bin/bash
# Displays the body of a 200 status code response
curl -s -o /tmp/body -w "%{http_code}" "$1" | grep -q "200" && cat /tmp/body
