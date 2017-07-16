#!/usr/bin/python

collect_list = {}
window_label = {}

N = 0
e = 1e-3
frequency = 1e-2
window_number = 1
window_size = int(1./ e)

file = file('/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part4/queriesLarge.txt')
lines = file.readlines()
out = open('output.out','w')

for line in lines:
    N += 1
    if line in collect_list:
        collect_list[line] += 1
    else:
        collect_list[line] = 1
        window_label[line] = window_number - 1

    if N % window_size == 0:
        for line in collect_list.keys():
            if collect_list[line] <= window_number - window_label[line]:
                del collect_list[line]
                del window_label[line]
        window_number += 1

for line in collect_list.keys():
    if collect_list[line] <= window_number - window_label[line]:
        del collect_list[line]
        del window_label[line]
        
for line in collect_list:
    if collect_list[line] >= (frequency - e) * N:
        out.write(line)

out.close()
