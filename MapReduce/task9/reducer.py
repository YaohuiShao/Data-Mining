#!/usr/bin/python
import sys

pre_word=""
count = 0
word = ""
filename = ""
flist = []
printer = ""


for line in sys.stdin:
    line = line.strip()
    tokens, count = line.split("\t",1)
    word, filename = tokens.split("^",1) # split the term and filename

    if pre_word == word:				
        count = str(count)
        flist.append("("+filename+","+count+")")

    else:						
        if pre_word:				
            if len(flist)==1:
                printer = flist[0]
            else:
		printer = ','.join(flist) # join the list using ',' if there are more than 1 items in the list.
            print ("{0}:  {1}:  {2}{3}{4}".format(pre_word,len(flist),'{',printer,'}'))
        printer = ""
        flist = []
        flist.append("("+filename+","+count+")")  # append current file name and its count to the list.
	pre_word = word

if pre_word: 				
    count = str(count)
    if len(flist)==1:
        printer = flist[0]
    else:
        printer = ','.join(flist)
    print ("{0}:  {1}:   {2}{3}{4}".format(pre_word,len(flist),'{',printer,'}'))
