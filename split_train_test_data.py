#!/usr/bin/python

import sys
import random

file=open(sys.argv[1],'r')
case_list=[]
control_list=[]
NUM_FOLD=10
for line in file.xreadlines():
	line=line[:-1]
	if line.startswith(sys.argv[2]) == True:
		case_list.append(line)
	else:
		control_list.append(line)
case_size=len(case_list)/NUM_FOLD
control_size=len(control_list)/NUM_FOLD
for i in range(0,NUM_FOLD):
	print 'i: '+str(i)
	case_bin=random.sample(case_list,case_size)
        control_bin=random.sample(control_list,control_size)
	if i == NUM_FOLD-1:
		case_bin=random.sample(case_list,len(case_list))
		control_bin=random.sample(control_list,len(control_list))
	print len(case_bin)
	print len(control_bin)
	out=open(sys.argv[3]+str(i+1),'w')
	for name in case_bin:
		out.write(name+'\n')
	for name in control_bin:
		out.write(name+'\n')
	tmp_case_list=[]
	tmp_control_list=[]
	for name in case_list:
		if name not in case_bin:
			tmp_case_list.append(name)
	for name in control_list:
		if name not in control_bin:
			tmp_control_list.append(name)
	case_list=tmp_case_list	
	control_list=tmp_control_list
	print len(case_list)
	print len(control_list)

