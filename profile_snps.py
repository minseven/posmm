#!/usr/bin/python

import sys
import os

def padding(s):
        n=''
        for i in range(0,6-len(s)):
                n=n+'0'
        return n+s

file=open(sys.argv[1],'r')
length=int(sys.argv[2])
content=file.read()
for i in range(0,len(content)-length+1):
	print padding(str(i))+content[i:i+length]
