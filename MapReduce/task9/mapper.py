#!/usr/bin/python

import sys
import os

for line in sys.stdin:
    line = line.strip()	
    tokens = line.split(" ")	
    file_path = os.environ["mapreduce_map_input_file"]	
    temp = file_path.split("/")	
    file_name = temp[-1]	#get the file name
    for token in tokens:
        print("{0}^{1}\t{2}".format(token, file_name, 1))	
