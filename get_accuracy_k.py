#!/usr/local/bin/python2.7

import sys
import operator
import random
import math

list_file=open(sys.argv[1],'r')
dist_file=open(sys.argv[2],'r')
list=[]
for line in list_file.xreadlines():
	line=line[:-1]
	element=line.split(' ')
	list.append(element[0])	
k=0
count=0
case=0
control=0
tp=0
tn=0
fp=0
fn=0
for line in dist_file.xreadlines():
	line=line[:-1]
	#element=line.split('\t')
	element=line.split(' ')
	vector=[]
	for i in range(0,len(element)):
		try:
			vector.append((list[i],float(element[i])))
		except:
			continue
	vector.sort(key=operator.itemgetter(1))
	#nline=list[k]
	traits={}
	traits_size={}
	traits_mean={}
	for i in range(1,int(sys.argv[3])+1):
		try:
			total=traits[vector[i][0][:-4]]
			size=traits[vector[i][0][:-4]]
			traits[vector[i][0][:-4]]=total+vector[i][1]
			traits_size[vector[i][0][:-4]]=size+1
		except:
			traits[vector[i][0][:-4]]=vector[i][1]
			traits_size[vector[i][0][:-4]]=1
	for name in traits:
		size=traits_size[name]
		total=traits[name]
		traits_mean[name]=float(total)/float(size)
	high_trait=[]
	high_num=float("0")
	for name in traits:
		if high_num < traits_size[name]:
			high_num=traits_size[name]
			high_trait.append(name)
	high_traits=[]
	for name in traits:
		if high_num == traits_size[name]:
			high_traits.append(name)
	#t=random.choice(high_traits)	
		#nline=nline+' '+str(vector[i][0])+' '+str(vector[i][1])
	high_num=0
	most_high=''
	for name in traits:
		if high_num < traits_mean[name]:
			high_num=traits_mean[name]
			most_high=name 
	
	if list[k][:-4].startswith(sys.argv[4]) == True:
		case=case+1
		if sys.argv[4] == most_high:
			tp=tp+1
		else:
			fn=fn+1
	else:
		control=control+1
		if list[k][:-4] == most_high:
			tn=tn+1
		else:
			fp=fp+1
	k=k+1

mcc=0
if tp+fp != 0 and tp+fn != 0 and tn+fp != 0 and tn+fn != 0:
	mcc=(tp*tn-fp*fn)/math.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))
print str(tp)+'\t'+str(tn)+'\t'+str(fp)+'\t'+str(fn)+'\t'+str(mcc)
