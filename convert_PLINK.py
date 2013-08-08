#!/usr/bin/python

import sys
import os

list=[]
annot_file=open(sys.argv[1],'r')
for line in annot_file.xreadlines():
	line=line[:-1]
	list.append(line)
count=0
ped_file=open(sys.argv[3]+'.ped','w')
map_file=open(sys.argv[3]+'.map','w')
for filename in os.listdir(sys.argv[2]):
	raw_file=open(sys.argv[2]+'/'+filename,'r')
	SNP_to_line={}
	for line in raw_file.xreadlines():
		line=line[:-1]
		element=line.split('\t')
		SNP_to_line[element[0]]=element[1]
	fields=filename.split('.')
	print str(count)+' '+fields[0]
	ped_file.write(fields[0]+' '+fields[0]+' 0 0 0 -9')
	for i in range(0,len(list)):
		element=list[i].split('\t')
		if element[0] not in SNP_to_line:
			continue
		elif count == 0:
			map_file.write(element[2]+' '+element[1]+' 0 '+element[3]+'\n')
		if SNP_to_line[element[0]] == '0':
			ped_file.write(' '+element[5]+' '+element[5])
		elif SNP_to_line[element[0]] == '1':
			ped_file.write(' '+element[5]+' '+element[6])
		elif SNP_to_line[element[0]] == '2':
			ped_file.write(' '+element[6]+' '+element[6])
		else:
			ped_file.write(' 0 0')	
	ped_file.write('\n')
	count=count+1
