#!/usr/bin/python

import sys

file=open(sys.argv[1],'r')
out=open(sys.argv[2],'w')
for line in file.xreadlines():
	line=line[:-1]
	element=line.split(' ')
	out.write(element[5])
	j=1
	for i in range(6,len(element)-1,2):
		if element[i]+element[i+1] == '11':
			out.write('\t'+str(j)+':0')
		elif element[i]+element[i+1] == '12' or element[i]+element[i+1] == '21':
			out.write('\t'+str(j)+':1')
		else:
			out.write('\t'+str(j)+':2')
		j=j+1
	out.write('\n')
