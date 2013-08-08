#!/usr/bin/python

import sys

class_file=open(sys.argv[1],'r')
file=open(sys.argv[2],'r')
out=open(sys.argv[3],'w')
num_to_class={}
for line in class_file.xreadlines():
	line=line[:-1]
	element=line.spilt('\t')
	num_to_class[element[1]]=element[0]
for line in file.xreadlines():
	line=line[:-1]
	element=line.split(' ')
	if element[0].startswith(num_to_class(sys.argv[4])) == True:
		out.write(element[0]+' '+element[1]+' '+element[2]+' '+element[3]+' 1 1\n')
	elif element[0].startswith(num_to_class(sys.argv[5])) == True: 
		out.write(element[0]+' '+element[1]+' '+element[2]+' '+element[3]+' 1 2\n')
	else:
		out.write(element[0]+' '+element[1]+' '+element[2]+' '+element[3]+' 1 -9\n')

	
