#!/usr/bin/python

import sys
import os
import math

count=0
case=0
control=0
pcase_rcase=0
pcontrol_rcontrol=0
pcase_rcontrol=0
pcontrol_rcase=0
correct_case=0
t=0
for i in range(1,int(sys.argv[2])+1):
	predict_file=open(sys.argv[1]+'.'+str(i)+'.train.predict','r')
	answer_file=open(sys.argv[1]+'.'+str(i)+'.test','r')
	predict_line=predict_file.read()
	predict_line=predict_line[:-1]
	
	answer_line=answer_file.read()
	answer_line=answer_line[:-1]
	element=answer_line.split('\t')
	#print predict_line+'\t'+element[0]
	if element[0] == '2':
                case=case+1
                if predict_line == '2':
                        pcase_rcase=pcase_rcase+1
                else:
                        pcontrol_rcase=pcontrol_rcase+1
        else:
                control=control+1
                if predict_line == '1':
                        pcontrol_rcontrol=pcontrol_rcontrol+1
                else:
                        pcase_rcontrol=pcase_rcontrol+1

total=case+control
p_pcase_rcase=float(pcase_rcase)/float(total)
p_pcase_rcontrol=float(pcase_rcontrol)/float(total)
p_pcontrol_rcontrol=float(pcontrol_rcontrol)/float(total)
p_pcontrol_rcase=float(pcontrol_rcase)/float(total)
p_pcase=float(pcase_rcase+pcase_rcontrol)/float(total)
p_pcontrol=float(pcontrol_rcase+pcontrol_rcontrol)/float(total)
p_rcase=float(pcase_rcase+pcontrol_rcase)/float(total)
p_rcontrol=float(pcase_rcontrol+pcontrol_rcontrol)/float(total)
#print str(total)+'\t'+str(pcase_rcase)+'\t'+str(pcase_rcontrol)+'\t'+str(pcontrol_rcontrol)+'\t'+str(pcontrol_rcase)
#print str(p_pcase_rcase)+'\t'+str(p_pcase_rcontrol)+'\t'+str(p_pcontrol_rcontrol)+'\t'+str(p_pcontrol_rcase)+'\t'+str(p_pcase)+'\t'+str(p_pcontrol)+'\t'+str(p_rcase)+'\t'+str(p_rcontrol)
a=0
if p_pcase_rcase != 0 and p_pcase != 0 and p_rcase != 0:
        a=p_pcase_rcase*math.log(p_pcase_rcase/(p_pcase*p_rcase),2)
b=0
if p_pcase_rcontrol != 0 and p_pcase != 0 and p_rcontrol != 0:
        b=p_pcase_rcontrol*math.log(p_pcase_rcontrol/(p_pcase*p_rcontrol),2)
c=0
if p_pcontrol_rcase != 0 and p_pcontrol != 0 and p_rcase != 0:
        c=p_pcontrol_rcase*math.log(p_pcontrol_rcase/(p_pcontrol*p_rcase),2)
d=0
if p_pcontrol_rcontrol != 0 and p_pcontrol != 0 and p_rcontrol != 0:
        d=p_pcontrol_rcontrol*math.log(p_pcontrol_rcontrol/(p_pcontrol*p_rcontrol),2)
mi=a+b+c+d
print str(total)+'\t'+str(pcase_rcase)+'\t'+str(pcase_rcontrol)+'\t'+str(pcontrol_rcontrol)+'\t'+str(pcontrol_rcase)+'\t'+str(mi)
