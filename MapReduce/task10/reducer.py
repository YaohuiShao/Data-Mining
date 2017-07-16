#!/usr/bin/python

import sys

i = 0
for line in sys.stdin:
    if i < 10: 
        view_count, Id = line.strip().split()
        print('{0} {1}'.format(view_count,Id)) # print the 10 most popular questions
  	i += 1
