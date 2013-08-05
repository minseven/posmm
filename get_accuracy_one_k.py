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
pcase_rcase=0
pcontrol_rcontrol=0
pcase_rcontrol=0
pcontrol_rcase=0
correct_case=0
test_file=open(sys.argv[2],'r')
for line in test_file.xreadlines():
	line=line[:-1]
	predicted=predict(sys.argv[3]+'.'+str(c)+'.jsd.tmp')
	if line.startswith(sys.argv[4]) == True:
                case=case+1
                if sys.argv[4] == predicted:
                        pcase_rcase=pcase_rcase+1
                else:
                        pcontrol_rcase=pcontrol_rcase+1
        else:
                control=control+1
                if line.startswith(predicted) == True:
                        pcontrol_rcontrol=pcontrol_rcontrol+1
                else:
                        pcase_rcontrol=pcase_rcontrol+1
	c=c+1
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
