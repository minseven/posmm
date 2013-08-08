#!/usr/bin/python

import sys
import math

file1=open(sys.argv[1],'r')
file2=open(sys.argv[2],'r')
file3=open(sys.argv[3],'r')
list=[]
name=[]
for line in file1.xreadlines():
	line=line[:-1]
	element=line.split(' ')
	name.append(element[0])
for line in file2.xreadlines():
	line=line[:-1]
	element=line.split('\t')
	list.append(element[0])
count=0
case=0
control=0
tp=0
tn=0
fp=0
fn=0
t=0
for line in file3.xreadlines():
	line=line[:-1]
	if name[t].startswith(sys.argv[4]) == True:
                case=case+1
                if list[t] == line:
                        tp=tp+1
                else:
                        fn=fn+1
        else:
                control=control+1
                if list[t] == line:
                        tn=tn+1
                else:
                        fp=fp+1
	t=t+1

mcc=0
if tp+fp != 0 and tp+fn != 0 and tn+fp != 0 and tn+fn != 0:
        mcc=(tp*tn-fp*fn)/math.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))
print str(tp)+'\t'+str(tn)+'\t'+str(fp)+'\t'+str(fn)+'\t'+str(mcc)
