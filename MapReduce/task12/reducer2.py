#!/usr/bin/python

import sys

alist = []
prev_owner = ''
max_list = []

for line in sys.stdin:
    line = line.strip()
    owner, aid = line.split(' ',1)

    if prev_owner == owner:
        alist.append(aid)
    else:
        if prev_owner:
            if len(alist) > len(max_list):
                max_list = alist
                max_count = len(max_list)
                max_owner = prev_owner
        prev_owner = owner
        alist = []
        alist.append(aid)
if prev_owner:
    if len(alist) > len(max_list):
        max_list = alist
        max_count = len(max_list)
        max_owner = prev_owner
print('{0} -> {1},{2}'.format(max_owner,max_count,', '.join(max_list)))

