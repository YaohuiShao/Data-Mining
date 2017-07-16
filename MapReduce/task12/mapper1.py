#!/usr/bin/python

import sys
import re

list_aaid = []

for line in sys.stdin:
    line = line.strip()
    PostTypeId = ''.join(re.findall(r"PostTypeId=\"(.*?)\"",line))

    if PostTypeId == '1': # find all questions records
        aaid = ''.join(re.findall(r"AcceptedAnswerId=\"(.*?)\"",line)) #get the accepted answers Ids of each question 
        if aaid:
            print('{0} {1}'.format(aaid,'x'))

    if PostTypeId == '2': # find all anwsers records
        Id = ''.join(re.findall(r"row\ Id=\"(.*?)\"",line)) # get the anwsers Ids
        oid = ''.join(re.findall(r"OwnerUserId=\"(.*?)\"",line)) # get the owners of the anwsers
        if Id and oid:
            print('{0} {1}'.format(Id,oid))

