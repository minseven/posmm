#!/usr/bin/python

import sys
import os

case_total=0
predicted_case_total=0
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
	if predict_line == '2':
		case_total=case_total+1
	if element[0] == '2':
		predicted_case_total=predicted_case_total+1	
	if predict_line == '2' and element[0] == predict_line:
		correct_case=correct_case+1


precision=float(correct_case)/float(case_total)
recall=float(correct_case)/float(predicted_case_total)
#print str(correct_case)+'\t'+str(case_total)+'\t'+str(predicted_case_total)
f1measure=0
if precision == 0 or recall == 0:
        f1measure=0
else:
        f1measure=float(2*(precision*recall)/(precision+recall))
print str(precision)+'\t'+str(recall)+'\t'+str(f1measure)
