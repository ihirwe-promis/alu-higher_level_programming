#!/bin/bash

curl -s "$1" -o /tmp/body
wc -c /tmp/body | awk '{print $1}'