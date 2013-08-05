#!/usr/bin/python

import sys

file=open(sys.argv[1],'r')
lines=[]
names=[]
for line in file.xreadlines():
	line=line[:-1]
	lines.append(line)	
	if line[:-6] not in names:
		names.append(line[:-6])
#names=['BRCA','COAD','HNSC','KIRC','LGG','OV','READ','UCEC','NA']
a=1
class_out=open(sys.argv[2]+'.class_num','w')
for name in names:
	class_out.write(name+'\t'+str(a)+'\n')	
	a=a+1
classsize=len(lines)/len(names)
for c in range(1,len(lines)+1):
	a_order=c%classsize
	if a_order == 0:
		a_order=classsize
	a_trait=(c-1)/classsize # trait of simulated individual
	for i in range(0,len(names)):
		for j in range(i+1,len(names)):
			out=open(sys.argv[2]+'.'+str(c)+'.c'+str(i+1)+str(j+1)+'.tfam','w')
			for k in range(0,len(lines)): 
				element=lines[k].split(' ')
				b_order=(k+1)%classsize
        			if b_order == 0: 
                			b_order=classsize
        			b_trait=k/classsize # trait of current individual
				#if k+1 == c:
				if (i == a_trait or j == a_trait) and a_order == b_order:
					out.write(element[0]+' '+element[1]+' '+element[2]+' '+element[3]+' 1 -9\n')
				elif lines[k].startswith(names[i]) == True:
					out.write(element[0]+' '+element[1]+' '+element[2]+' '+element[3]+' 1 1\n')
				elif lines[k].startswith(names[j]) == True:
					out.write(element[0]+' '+element[1]+' '+element[2]+' '+element[3]+' 1 2\n')
				else:
					out.write(element[0]+' '+element[1]+' '+element[2]+' '+element[3]+' 1 -9\n')

	
