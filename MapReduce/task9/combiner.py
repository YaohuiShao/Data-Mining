#!/usr/bin/python

import sys

prev_token = ""
value_total = 0
token = ""

for line in sys.stdin:
    line = line.strip()
    token,value = line.split("\t") # token is the combination of the term and file name
    value = int(value)

    if prev_token == token:
        value_total += value

    else:
        if prev_token:
            print("{0}\t{1}".format(prev_token,value_total))  
        value_total = value
        prev_token = token

if prev_token == token:
    print("{0}\t{1}".format(prev_token,value_total))
