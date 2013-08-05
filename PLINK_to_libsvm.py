#!/usr/bin/python

import sys

file=open(sys.argv[1],'r')
train=open(sys.argv[2]+'.train','w')
test=open(sys.argv[2]+'.test','w')
c=1
for line in file.xreadlines():
	line=line[:-1]
	element=line.split(' ')
	if int(sys.argv[3]) == c:
                if element[0].startswith(sys.argv[4]) == True:
                        test.write('2')
                else:
                        test.write('1')
		j=1
        	for i in range(6,len(element)-1,2):
                	if element[i]+element[i+1] == '11':
                        	test.write('\t'+str(j)+':0')
                	elif element[i]+element[i+1] == '12' or element[i]+element[i+1] == '21':
                        	test.write('\t'+str(j)+':1')
                	else:
                        	test.write('\t'+str(j)+':2')
                	j=j+1
        	test.write('\n')
		c=c+1
		continue
	elif element[5] != '1' and element[5] != '2':
		c=c+1
		continue
	else:
		c=c+1
		train.write(element[5])
	j=1
	for i in range(6,len(element)-1,2):
		if element[i]+element[i+1] == '11':
			train.write('\t'+str(j)+':0')
		elif element[i]+element[i+1] == '12' or element[i]+element[i+1] == '21':
			train.write('\t'+str(j)+':1')
		else:
			train.write('\t'+str(j)+':2')
		j=j+1
	train.write('\n')
