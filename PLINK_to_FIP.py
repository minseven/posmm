#!/usr/bin/python

import sys

file=open(sys.argv[1],'r')
out=open(sys.argv[2],'w')
for line in file.xreadlines():
	line=line[:-1]
	element=line.split(' ')
	list=[]
	total=0
	for i in range(6,len(element),2):
		if element[i] == '1' and element[i+1] == '1':
			list.append(1)
			total=total+1
		elif element[i] == '2' and element[i+1] == '2':
			list.append(0)
		else:
			list.append(0.5)
			total=total+0.5
	out.write(str(0)+'\t'+str(float(list[0])/float(total)))
	for i in range(1,len(list)):
		out.write('\t'+str(i)+'\t'+str(float(list[i])/float(total)))
	out.write('\n')
