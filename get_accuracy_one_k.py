#!/usr/local/bin/python2.7

import sys
import operator
import random
import math

def predict(file):
	dist_file=open(file,'r')
	line=dist_file.read()
	line=line[:-1]
	element=line.split(' ')
	vector=[]
	for i in range(1,len(element)):
        	try:
                	vector.append((list[i-1],float(element[i])))
        	except:
                	continue
	vector.sort(key=operator.itemgetter(1))
	traits={}
	traits_size={}
	traits_mean={}
	#print vector[:10]
	for i in range(0,int(sys.argv[5])):
        	try:
                	total=traits[vector[i][0][:-4]]
                	traits[vector[i][0][:-4]]=total+vector[i][1]

               		size=traits_size[vector[i][0][:-4]]
                	traits_size[vector[i][0][:-4]]=size+1
        	except:
                	traits[vector[i][0][:-4]]=vector[i][1]
                	traits_size[vector[i][0][:-4]]=1
	for name in traits:
        	total=traits[name]
        	size=traits_size[name]
        	traits_mean[name]=float(total)/float(size)
	high_trait=[]
	high_num=0
	for name in traits:
        	if high_num < traits_size[name]:
                	high_num=traits_size[name]
                	high_trait.append(name)
	high_traits=[]
	for name in traits:
        	if high_num == traits_size[name]:
                	high_traits.append(name)
	most_high=''
	high_mean=0
	if len(high_traits) == 1:
        	most_high=high_traits[0]
	else:
        	for name in high_traits:
                	if high_mean < traits_mean[name]:
                        	high_mean=traits_mean[name]
                        	most_high=name
	return most_high

list_file=open(sys.argv[1],'r')
list=[]
for line in list_file.xreadlines():
	line=line[:-1]
	element=line.split(' ')
	list.append(element[0])	

c=1
count=0
case=0
control=0
tp=0
tn=0
fp=0
fn=0
test_file=open(sys.argv[2],'r')
out=open(sys.argv[6],'w')
for line in test_file.xreadlines():
	line=line[:-1]
	element=line.split(' ')
	predicted=predict(sys.argv[3]+'.'+str(c)+'.jsd.tmp')
	if predicted == sys.argv[4]:
		out.write(element[0]+'\t2\n')	
	else:
		out.write(element[0]+'\t1\n')
	if element[0].startswith(sys.argv[4]) == True:
                case=case+1
                if sys.argv[4] == predicted:
                        tp=tp+1
                else:
                        fn=fn+1
        else:
                control=control+1
                if line.startswith(predicted) == True:
                        tn=tn+1
                else:
                        fp=fp+1
	c=c+1
mcc=0
if tp+fp != 0 and tp+fn != 0 and tn+fp != 0 and tn+fn != 0:
        mcc=(tp*tn-fp*fn)/math.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))
print str(tp)+'\t'+str(tn)+'\t'+str(fp)+'\t'+str(fn)+'\t'+str(mcc)
