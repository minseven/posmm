#!/usr/bin/python

import sys
import operator

list_file2=open(sys.argv[1],'r')
file=open(sys.argv[2],'r')
train=open(sys.argv[3]+'.train','w')
test=open(sys.argv[3]+'.test','w')
list=[]
dict={}
for line in list_file2.xreadlines():
	line=line[:-1]
	element=line.split(' ')
	list.append(element[0])
	dict[element[0]]=element[5]
c=1
for line in file.xreadlines():
	line=line[:-1]
	element=line.split('\t')
	vector=[]
	#for i in range(0,len(element)-1,2):
	for i in range(0,len(element)):
		vector.append((int(element[i])+1,1))
	vector.sort(key=operator.itemgetter(0))
	if int(sys.argv[4]) == c:
		if list[c-1].startswith(sys.argv[5]) == True:
                        test.write('2')
                else:
                        test.write('1')	
		for i in range(0,len(vector)):     
                	test.write('\t'+str(vector[i][0])+':'+str(vector[i][1]))
		test.write('\n')
		c=c+1
	elif dict[list[c-1]] == '-9':
                c=c+1
                continue
	else:
		if list[c-1].startswith(sys.argv[5]) == True:
                        train.write('2')
                else:
                        train.write('1')
		for i in range(0,len(vector)):     
        		train.write('\t'+str(vector[i][0])+':'+str(vector[i][1]))
		train.write('\n')
		c=c+1	
