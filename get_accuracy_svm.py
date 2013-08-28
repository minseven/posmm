#!/usr/bin/python

import sys
import os
import math

case=0
control=0
tp=0
tn=0
fp=0
fn=0
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
                        tp=tp+1
                else:
                        fn=fn+1
        else:
                control=control+1
                if predict_line == '1':
                        tn=tn+1
                else:
                        fp=fp+1
mcc=0
if tp+fp != 0 and tp+fn != 0 and tn+fp != 0 and tn+fn != 0:
        mcc=(tp*tn-fp*fn)/math.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))
p_m0c0=float(tp)/float(tp+tn+fp+fn)
p_m0c1=float(fp)/float(tp+tn+fp+fn)
p_m1c0=float(fn)/float(tp+tn+fp+fn)
p_m1c1=float(tn)/float(tp+tn+fp+fn)

p_m0=p_m0c0+p_m0c1
p_m1=p_m1c0+p_m1c1
p_c0=p_m0c0+p_m1c0
p_c1=p_m0c1+p_m1c1

m0c0=0
m0c1=0
m1c0=0
m1c1=0
if p_m0c0 != 0 and p_m0 != 0 and p_c0 != 0:
	m0c0=p_m0c0*math.log(p_m0c0/(p_m0*p_c0),2)
if p_m0c1 != 0 and p_m0 != 0 and p_c1 != 0:
	m0c1=p_m0c1*math.log(p_m0c1/(p_m0*p_c1),2)
if p_m1c0 != 0 and p_m1 != 0 and p_c0 != 0:
	m1c0=p_m1c0*math.log(p_m1c0/(p_m1*p_c0),2)
if p_m1c1 != 0 and p_m1 != 0 and p_c1 != 0:
	m1c1=p_m1c1*math.log(p_m1c1/(p_m1*p_c1),2)
mi=m0c0+m0c1+m1c0+m1c1

print str(tp)+'\t'+str(tn)+'\t'+str(fp)+'\t'+str(fn)+'\t'+str(mcc)
#print str(tp)+'\t'+str(tn)+'\t'+str(fp)+'\t'+str(fn)+'\t'+str(mi)
