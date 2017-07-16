#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    count, seq = line.split(",", 1)
    print("{0}\t{1}".format(count,seq))
