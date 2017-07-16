#!/usr/bin/python
import sys

prev_line = ""
value_total = 0
line = ""

for line in sys.stdin:
    line = line.strip()
    line, value = line.split("\t", 1)
    value = int(value)

    if prev_line == line:
        value_total += value
    else:
        if prev_line and value_total == 1:
            print(prev_line)

        value_total = value
        prev_line = line

if value_total == 1 and prev_line:
    print(prev_line)
