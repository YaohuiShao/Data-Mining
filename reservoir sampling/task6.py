#!/usr/bin/env python

import sys, random

resevoir = []
file = file('/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt')
lines = file.readlines()

for index, line in enumerate(lines):
    if index < 100:
        resevoir.append(line.strip())
    else:
        n = random.randint(0,index)
        if n < 100:
            resevoir[n] = line.strip()

out = open('output.out', 'w')
for i in range(100):
    out.write(resevoir[i]+'\n')
out.close()
file.close()
