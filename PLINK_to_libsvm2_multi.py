#!/usr/bin/python

import sys

class_file=open(sys.argv[1],'r')
file=open(sys.argv[2],'r')
out=open(sys.argv[3],'w')
class_to_num={}
for line in class_file.xreadlines():
        line=line[:-1]
        element=line.split('\t')
        class_to_num[element[0]]=element[1]

for line in file.xreadlines():
	line=line[:-1]
	element=line.split(' ')
	if element[5] == '-9':
		continue
	out.write(class_to_num[element[0][:-6]])
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
