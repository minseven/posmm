#!/usr/bin/python

import sys

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
correct_case=0
predicted_case=0
real_case=0
t=0
for line in file3.xreadlines():
	line=line[:-1]
	if name[t].startswith(sys.argv[4]) == True and list[t] == line:
		correct_case=correct_case+1	
	if line == '2':
		predicted_case=predicted_case+1
	if list[t] == '2':
		real_case=real_case+1
	t=t+1
#print str(correct_case)+'\t'+str(predicted_case)+'\t'+str(real_case)
precision=float(correct_case)/float(predicted_case)
recall=float(correct_case)/float(real_case)
print str(precision)+'\t'+str(recall)+'\t'+str(2*(precision*recall)/(precision+recall))
