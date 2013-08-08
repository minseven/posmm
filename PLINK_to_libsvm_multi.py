#!/usr/bin/python

import sys

class_file=open(sys.argv[1],'r')
file=open(sys.argv[2],'r')
train=open(sys.argv[3]+'.train','w')
test=open(sys.argv[3]+'.test','w')
class_to_num={}
for line in class_file.xreadlines():
	line=line[:-1]
	element=line.split('\t')
	class_to_num[element[0]]=element[1]
c=1
for line in file.xreadlines():
	line=line[:-1]
	element=line.split(' ')
	if int(sys.argv[3]) == c:
		test.write(class_to_num[element[0][:-6]])
                #if element[0].startswith(sys.argv[4]) == True:
                #        test.write('2')
                #else:
                #        test.write('1')
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
		train.write(class_to_num[element[0][:-6]])
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
