#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = line.strip()
    Id = ''.join(re.findall(r"row\ Id=\"(.*?)\"",line)) # get the question IDs
    view_count = ''.join(re.findall(r"ViewCount=\"(.*?)\"",line))  # get the view count of each question
    if Id and view_count:
        Id = int(Id)
        view_count = int(view_count)
        print('{0}\t{1}'.format(view_count,Id))

