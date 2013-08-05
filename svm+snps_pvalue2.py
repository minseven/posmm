#!/usr/bin/python

import fisher
import sys

file1=open(sys.argv[1],'r')
file2=open(sys.argv[2],'r')
out=open(sys.argv[5],'w')
feature_to_count={}
for line in file1.xreadlines():
	line=line[:-1]
	element=line.split('\t')
	try:
		feature_to_count[int(element[1])]=int(element[0])
	except:
		continue
total1=int(sys.argv[3])
total2=int(sys.argv[4])
for line in file2.xreadlines():
	line=line[:-1]
	element=line.split('\t')
	try:
		a11=0
		a12=0
		b11=int(element[0])
		b12=total2-b11
		try:
			a11=feature_to_count[int(element[1])]
		except:
			a11=0
		a12=total1-a11
		p=fisher.pvalue(a11,a12,b11,b12)
		#if float(p.two_tail) < float(sys.argv[6]):
			#print str(element[1])+' '+str(p.two_tail)+' '+str(a11)+' '+str(a12)+' '+str(b11)+' '+str(b12)
		#out.write(element[1]+'\n')
		out.write(str(element[1])+' '+str(p.two_tail)+'\n')
	#print p.two_tail
	except:
		continue	
