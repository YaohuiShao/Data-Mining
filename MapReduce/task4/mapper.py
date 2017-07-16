#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    prev_1 = ""
    prev_2 = ""
    tokens = line.split()

    for token in tokens:
        if prev_1 and prev_2:
	    words = [prev_1, prev_2, token]
            seq = " ".join(words)
            print("{0},{1}".format(seq, 1))
        prev_1 = prev_2
        prev_2 = token
