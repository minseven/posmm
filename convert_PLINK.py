#!/usr/bin/python

import sys

ped_file=open(sys.argv[1],'r')
Index_to_SNP={}
list=[]
c=0
for line in ped_file.xreadlines():
	line=line[:-1]
	element=line.split(' ')
	print c
	c=c+1
	out=open(sys.argv[2]+'/'+element[1]+'.ind','w')
	for i in range(6,len(element),2):
		if element[i]+element[i+1] == 'AA':
			out.write('0')
		elif element[i]+element[i+1] == 'CC':
			out.write('1')
		elif element[i]+element[i+1] == 'GG':
			out.write('2')
		elif element[i]+element[i+1] == 'TT':
			out.write('3')
		elif element[i]+element[i+1] == 'AC' or element[i]+element[i+1] == 'CA':
			out.write('4')
		elif element[i]+element[i+1] == 'AG' or element[i]+element[i+1] == 'GA':
			out.write('5')
		elif element[i]+element[i+1] == 'AT' or element[i]+element[i+1] == 'TA':
			out.write('6')
		elif element[i]+element[i+1] == 'CG' or element[i]+element[i+1] == 'GC':
			out.write('7')
		elif element[i]+element[i+1] == 'CT' or element[i]+element[i+1] == 'TC':
			out.write('8')
		elif element[i]+element[i+1] == 'GT' or element[i]+element[i+1] == 'TG':
			out.write('9')
		else:
			print 'Error: unrecognizable code found'
			break
	out.write('\n')
