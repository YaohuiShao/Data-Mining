#!/usr/bin/python

import sys

list = []
sum = 0
average_max = 0
student =""

for line in sys.stdin:
    line = line.strip()
    name, list = line.split("\t")
    mark_list = list.split()
    for each in mark_list:
        course, mark = each.split(",",1) 
        mark = mark.split(")")
        mark[0] = float(mark[0])   
        sum += mark[0]
    average = sum/float(len(mark_list))
    if average > average_max:
        average_max = average
        student = name
    sum = 0  
print(student,average_max)

   
