#!/usr/bin/python

import sys

file=open(sys.argv[1],'r')
lines=[]
for line in file.xreadlines():
	line=line[:-1]
	lines.append(line)	
for c in range(1,len(lines)+1):
	out=open(sys.argv[2]+'.'+str(c)+'.tfam','w')
	tmp=lines[c-1].split(' ')
	case=False
	if tmp[0].startswith(sys.argv[3]) == True:
		case=True
	first=True
	for i in range(1,len(lines)+1):
		element=lines[i-1].split(' ')
		if first == True and case == True and element[0].startswith(sys.argv[3]) == False:
			out.write(element[0]+' '+element[1]+' '+element[2]+' '+element[3]+' '+element[4]+' -9\n')
			first=False
		elif first == True and case == False and element[0].startswith(sys.argv[3]) == True:
                        out.write(element[0]+' '+element[1]+' '+element[2]+' '+element[3]+' '+element[4]+' -9\n')
                        first=False
		elif i == c:
			out.write(element[0]+' '+element[1]+' '+element[2]+' '+element[3]+' '+element[4]+' -9\n')
		elif element[0].startswith(sys.argv[3]) == True:
			out.write(element[0]+' '+element[1]+' '+element[2]+' '+element[3]+' '+element[4]+' 2\n')
		else:
			out.write(element[0]+' '+element[1]+' '+element[2]+' '+element[3]+' '+element[4]+' 1\n')
			
