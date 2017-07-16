#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = line.strip()
    PostTypeId = ''.join(re.findall(r"PostTypeId=\"(.*?)\"",line))

    if PostTypeId == '2': # find all questions records
        ParentId = ''.join(re.findall(r"ParentId=\"(.*?)\"",line))
        OwnerUserId = ''.join(re.findall(r"OwnerUserId=\"(.*?)\"",line)) 

        ParentId = int(ParentId)
        OwnerUserId = int(OwnerUserId)
        print('{0} {1} {2}'.format(OwnerUserId,ParentId,1))

