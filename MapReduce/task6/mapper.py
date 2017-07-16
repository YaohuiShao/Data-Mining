#!/usr/bin/python

import sys

prev_c = ""
count_list = []

for line in sys.stdin:
    line = line.strip()
    line = line.split()
    c = line[:2]
    count = line[3]

    if prev_c == c:
        count_list.append(count)
    else:
        if prev_c:
            print("{0},{1}".format(" ".join(prev_c)," ".join(count_list)))
        
        prev_c = c
        count_list = []
        count_list.append(count)

if prev_c == c:
    print("{0},{1}".format(" ".join(prev_c)," ".join(count_list)))
