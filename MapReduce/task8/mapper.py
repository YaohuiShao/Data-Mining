#!/usr/bin/python

import sys

name = ""
mark = ""
list_mark = []

for line in sys.stdin:
    name, mark = line.strip().split("-->")
    list_mark = mark.split()
    if len(list_mark) > 3:
        print("{0}\t{1}".format(name,list_mark))
