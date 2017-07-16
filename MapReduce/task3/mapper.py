#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    print("{0},{1}".format(len(line),line))

