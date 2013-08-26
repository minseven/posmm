#!/usr/bin/python

import sys
import operator

list_file=open(sys.argv[1],'r')
file=open(sys.argv[2],'r')
out=open(sys.argv[3],'w')
list=[]
for line in list_file.xreadlines():
	line=line[:-1]
	list.append(line)	
c=1
for line in file.xreadlines():
	line=line[:-1]
	element=line.split('\t')
	vector=[]
	#for i in range(0,len(element)-1,2):
	for i in range(0,len(element)):
		vector.append((int(element[i])+1,1))
	vector.sort(key=operator.itemgetter(0))
	if list[c-1].startswith(sys.argv[4]) == True:
        	out.write('2')
        else:
        	out.write('1')
	for i in range(0,len(vector)):     
        	out.write('\t'+str(vector[i][0])+':'+str(vector[i][1]))
	out.write('\n')
	c=c+1	
