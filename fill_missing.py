#!/usr/bin/python

import sys

file=open(sys.argv[1],'r')
out=open(sys.argv[2],'w')
for line in file.xreadlines():
	line=line[:-1]
	element=line.split(' ')
	geno={}
	for i in range(4,len(element)-1,2):
		g=element[i]+' '+element[i+1]
		if g == '0 0':
			continue
		try:
			tmp=geno[g]
			geno[g]=tmp+1
		except:
			geno[g]=1
	c=0
	m=''
	for g in geno:
		if c < geno[g]:
			c=geno[g]
			m=g
	nline=element[0]+' '+element[1]+' '+element[2]+' '+element[3]
	if m == '':
		continue
	for i in range(4,len(element)-1,2):
		g=element[i]+' '+element[i+1]
		if g == '0 0':
			nline=nline+' '+m
		else:
			nline=nline+' '+g
	out.write(nline+'\n')
