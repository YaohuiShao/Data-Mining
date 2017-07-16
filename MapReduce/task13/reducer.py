#!/usr/bin/env python

import sys
import random

resevoir = ''

line_number = 0
sum = 0

for line in sys.stdin:
    line,value = line.split('\t',1)
    sum += int(value)
    if random.randint(0, sum-1) < value:
        resevoir = line.strip()
print(resevoir)
