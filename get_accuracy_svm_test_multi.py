#!/usr/local/bin/python2.7

import sys
import operator
import random

def get_result(k,list):
	count={}
	for i in range(0,len(list)):
                for j in range(i+1,len(list)):
                        try:
        			file=open(sys.argv[3]+'.c'+str(list[i])+str(list[j])+'.train.predict','r')
                                line=file.read()
                                line=line[:-1]
				#print str(list[i])+'\t'+str(list[j])+'\t'+str(k)
                                if int(line) in count:
                                        tmp=count[int(line)]
                                        count[int(line)]=tmp+1
                                else:
                                        count[int(line)]=1

                        except:
				#print str(list[i])+'\t'+str(list[j])+'\t'+str(k)
                                t=[list[i],list[j]]
                                r=random.choice(t)
                                if r in count:
                                        tmp=count[r]
                                        count[r]=tmp+1
                                else:
                                        count[r]=1

        best_label=0
        best_count=0
        total_count=0
	#print count
        for i in range(1,nclass+1):
                try:
                        #print str(i)+'\t'+str(count[i])
                        total_count=total_count+count[i]
                        if count[i] > best_count:
                                best_label = i
                                best_count = count[i]
                except:
                        continue
        bests=[]
        for i in range(1,nclass+1):
                try:
                        if count[i] == best_count:
                                bests.append(i)
		except:
                        continue
	if len(list) == nclass:
		global last_count
		last_count=best_count
	#print str(k)+'\t'+str(count)
	if len(bests) == len(list):
		t=random.choice(bests)
		global random_count
		random_count=random_count+1
		return [t]
	else:
        	return bests

random_count=0
last_count=0
c=0
total=0
class_file=open(sys.argv[1],'r')
test_file=open(sys.argv[2],'r')
nclass=0
for line in class_file.xreadlines():
	line=line[:-1]
	nclass=nclass+1
for line in test_file.xreadlines():
	line=line[:-1]
	element=line.split(' ')
	list=[j for j in range(1,nclass+1)]
	while len(list) > 1:
		a=get_result(i,list)	
		#print str(i)+':\t'+str(a)
		list=a
	#print traits[int(sys.argv[3])]+'\t'+traits[list[0]]+'\t'+str(float(last_count)/float(9))
	if element[0] == list[0]:
		c=c+1
	total=total+1
print str(float(c)/float(total))
