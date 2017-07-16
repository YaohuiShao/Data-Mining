#!/usr/bin/python

import sys

list = []

for line in sys.stdin:
    line = line.strip().split()
    studentID = line[1]
    if line[0] == "student":
        list = [line[2],",",","]
    else:
        list = [",",line[2],line[3]]

    print ("{0}\t{1}".format(line[1]," ".join(list)))
