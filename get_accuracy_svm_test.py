#!/usr/bin/python

import sys
import math

file1=open(sys.argv[1],'r')
file2=open(sys.argv[2],'r')
file3=open(sys.argv[3],'r')
out=open(sys.argv[5],'w')
list=[]
name=[]
for line in file1.xreadlines():
	line=line[:-1]
	element=line.split(' ')
	name.append(element[0])
for line in file2.xreadlines():
	line=line[:-1]
	element=line.split('\t')
	list.append(element[0])
count=0
case=0
control=0
tp=0
tn=0
fp=0
fn=0
t=0
for line in file3.xreadlines():
	line=line[:-1]
	out.write(name[t]+'\t'+line+'\n')
	if list[t] == '2':
                case=case+1
                if list[t] == line:
                        tp=tp+1
                else:
                        fn=fn+1
        else:
                control=control+1
                if list[t] == line:
                        tn=tn+1
                else:
                        fp=fp+1
	t=t+1
mcc=0
if tp+fp != 0 and tp+fn != 0 and tn+fp != 0 and tn+fn != 0:
        mcc=(tp*tn-fp*fn)/math.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))
#print str(tp)+'\t'+str(tn)+'\t'+str(fp)+'\t'+str(fn)+'\t'+str(mcc)
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
