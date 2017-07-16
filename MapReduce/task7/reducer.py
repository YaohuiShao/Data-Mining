#!/usr/bin/python
import sys

string = ""
prev_key = ""
mark = []
name = ""
list = []

for line in sys.stdin:
    line = line.strip()
    key, string = line.split("\t",1)
    list = string.strip().split()

    if prev_key == key:
        if list[0] == ",":
            mark.append(("("+list[1]+","+list[2]+")"))   
        else:
            name = list[0]
    else:
        if prev_key:
            print(name + "-->" +" ".join(mark))

        prev_key = key
	mark = []
        if list[0] == ",":
            mark.append(("("+list[1]+","+list[2]+")"))   
        else:
            name = list[0]

print(name + "-->" +" ".join(mark))
