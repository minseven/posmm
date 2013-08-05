#!/usr/bin/python

import sys
import os

def padding(s):
        n=''
        for i in range(0,6-len(s)):
                n=n+'0'
        return n+s

list_file=open(sys.argv[1],'r')
file=open(sys.argv[2],'r')
length=int(sys.argv[3])
out=open(sys.argv[4],'w')
list={}
index=0
features=[]
for line in list_file.xreadlines():
	line=line[:-1]
	list[line]=index
	index=index+1	
content=file.read()
total=0
nline=''
for i in range(0,len(content)-length+1):
	try:
		if len(content[i:i+length]) != length:
			continue
		f=padding(str(i))+content[i:i+length]
		tmp=list[f]
		features.append(tmp)
		total=total+1
	except:
		continue
for i in range(0,len(features)):
	nline=nline+str(features[i])+'\t'+str(float(1)/float(total))+'\t'
out.write(nline[:-1]+'\n')
