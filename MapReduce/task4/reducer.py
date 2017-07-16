#!/usr/bin/python
import sys

prev_seq = ""
count_total = 0
seq = ""

for line in sys.stdin:
    line = line.strip()
    seq, count = line.split(",", 1)
    count = int(count)

    if prev_seq == seq:
        count_total += count
    else:
        if prev_seq:
            print("{0}\t{1}".format(prev_seq, count_total))

        count_total = count
        prev_seq = seq

if prev_seq == seq:
    print("{0}\t{1}".format(prev_seq, count_total))

