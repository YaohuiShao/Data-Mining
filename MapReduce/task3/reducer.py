#!/usr/bin/python
import sys

max_len_ln = 0
max_len_tk = 0

for line in sys.stdin:
    line = line.strip()
    len_ln,line= line.split(",", 1)
    len_ln = int(len_ln)
    if max_len_ln < len_ln:
        max_len_ln = len_ln
    for token in line.split():
        if max_len_tk < len(token):
            max_len_tk = len(token)

print(max_len_tk)
print(max_len_ln)


