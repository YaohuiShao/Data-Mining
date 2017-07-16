#!/usr/bin/python

import sys
import re

prev_id = ''
prev_owner = ''
alist = []

for line in sys.stdin:
    line = line.strip().split()
            
    if prev_id == line[0]:
        if line[1] == 'x':
            print('{0} {1}'.format(prev_owner,prev_id))
        else:
            print('{0} {1}'.format(line[1],line[0]))
    else:
        prev_id = line[0]
        prev_owner = line[1]
