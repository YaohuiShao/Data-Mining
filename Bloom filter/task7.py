#!/usr/bin/python

import sys,mmh3
from bitarray import bitarray

n_line = int(sys.argv[1]) # get the number of lines in the file
bit_size = n_line*10
n_hash = 7                # the number of hash functions
bit_array = bitarray(bit_size)
bit_array.setall(0)


file = file('/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt')
lines = file.readlines()
out = open('output.out', 'w')

for line in lines:
    line = line.strip()
    in_bitarray = True
    for seed in xrange(n_hash):
        index = mmh3.hash(line, seed) % bit_size
        if bit_array[index] == 0:
            in_bitarray = False
            bit_array[index] = 1
    if in_bitarray == False:
        out.write(line+'\n')
out.close()
file.close()


