#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    owner, aaid = line.split(' ',1)
    print('{0} {1}'.format(owner,aaid))
