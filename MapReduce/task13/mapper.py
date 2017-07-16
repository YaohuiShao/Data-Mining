#!/usr/bin/env python

import sys
import random

line_number = 0

for line in sys.stdin:
    if random.randint(0, line_number) == 0:
        resevoir = line.strip()
        line_number += 1
print('{0}\t{1}'.format(resevoir,line_number))
