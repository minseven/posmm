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
print str(tp)+'\t'+str(tn)+'\t'+str(fp)+'\t'+str(fn)+'\t'+str(mcc)
