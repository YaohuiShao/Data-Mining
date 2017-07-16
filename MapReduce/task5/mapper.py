#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split()
    seq = " ".join(line[:3])
    print("{0},{1}".format(line[3],seq))	
