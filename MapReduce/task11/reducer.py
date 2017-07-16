#!/usr/bin/python
import sys

prev_oid = ''
prev_qid = ''
count_total = 0
qlist = []
max_oid =''
max_list = []
result = []

for line in sys.stdin:
    line = line.strip()
    oid, qid, count = line.split(' ',2)
    
    if prev_oid == oid:
        if prev_qid != qid:
            qlist.append(qid)
    else:
        if prev_oid:
            if len(qlist) > len(max_list):  
                max_list = qlist   # get the list which contains the most questions
                max_oid = prev_oid   # get the user who answered the most questions
        prev_oid = oid
        prev_qid = qid
        qlist = []
        qlist.append(qid)

if prev_oid:
    if len(qlist) > len(max_list):
        max_oid = prev_oid
        max_list = qlist

for qid in max_list:   # de-duplicate the qid in max_list
    if qid not in result:
        result.append(qid)     
print('{0} -> {1}'.format(max_oid,', '.join(result)))
  
