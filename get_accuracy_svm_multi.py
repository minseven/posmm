#!/usr/local/bin/python2.7

import sys
import random

def get_result(k,list):
	count={}
	for i in range(0,len(list)):
                for j in range(i+1,len(list)):
                        try:
                                file=open(sys.argv[2]+'.'+str(k)+'.c'+str(list[i])+str(list[j])+'.test.predict','r')
                                c=1
                                line=file.read()
                                line=line[:-1]
                                if int(line) in count:
                                        tmp=count[int(line)]
                                        count[int(line)]=tmp+1
                                else:
                                        count[int(line)]=1

                        except IOError:
				t=[i,j]
				r=random.choice(t)
				if r in count:
					tmp=count[r]
					count[r]=tmp+1
				else:
					count[r]=1

	best_label=0
	best_count=0
	total_count=0
	for i in range(1,nclass+1):
		try:
			#print str(i)+'\t'+str(count[i])
			total_count=total_count+count[i]
			if count[i] > best_count:
				best_label = i
				best_count = count[i]
		except:
			continue
	if len(list) == nclass:
		global last_count
		last_count=best_count
	bests=[]
	for i in range(1,nclass+1):
		try:
			if count[i] == best_count:
				bests.append(i)
		except:
			continue
	if len(bests) == len(list):
		t=random.choice(bests)
		global random_count
		random_count=random_count+1
		return [t]
	else:
		return bests	
file=open(sys.argv[1],'r')
names=[]
nsize=0
for line in file.xreadlines():
	line=line[:-1]
	if line[:-6] not in names:
		names.append(line[:-6])
	nsize=nsize+1
nclass=len(names)
nclasssize=nsize/len(names)
random_count=0
count=0
#last_count
for i in range(1,nsize+1):
	#print i
	c=(i-1)/nclasssize+1
	list=[j for j in range(1,nclass+1)]
	while len(list) > 1:
		a=get_result(i,list)
		list=a	
	#print str(c)+'\t'+str(list[0])+'\t'+str(last_count)
	if c == list[0]:
		count=count+1
print str(float(count)/float(nsize))
