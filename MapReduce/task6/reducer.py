#!/usr/bin/python

import sys
import math

for line in sys.stdin:
    line = line.strip()
    c, count_list = line.split(",",1)
    count_list = count_list.strip().split()
    i = 0
    sum = 0
    while i < len(count_list):
        sum += int(count_list[i])
        i += 1
    H = 0
    for each in count_list:
        p = float(each)/float(sum)
        h = math.log(p,2)
        H += (-p*h)
    print("{0}\t{1}".format("".join(c),H))


