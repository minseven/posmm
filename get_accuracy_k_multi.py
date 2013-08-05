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
	list.append(line)	
k=0
count=0
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
			total=traits[vector[i][0][:-6]]
			size=traits[vector[i][0][:-6]]
			traits[vector[i][0][:-6]]=total+vector[i][1]
			traits_size[vector[i][0][:-6]]=size+1
		except:
			traits[vector[i][0][:-6]]=vector[i][1]
			traits_size[vector[i][0][:-6]]=1
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
	
	#print nline
	#print list[k]+'\t'+most_high
	#if str(most_high) == 'NA':
	#	print list[k][:-6]+'\tNA'
	#else:
	#	print list[k][:-6]+'\t'+str(most_high)
	if list[k][:-6] == most_high:
		count=count+1
	k=k+1
print str(float(count)/float(len(list)))
