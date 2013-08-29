#!/usr/local/bin/python2.7

import sys
import random
import math
import operator

knn_snp={}
knn_snps={}
svm_snp={}
svm_snps={}

knn_snp['CASE']=[0,0]
knn_snp['CONT']=[0,0]

knn_snps['CASE']=[0,0]
knn_snps['CONT']=[0,0]

svm_snp['CASE']=[0,0]
svm_snp['CONT']=[0,0]

svm_snps['CASE']=[0,0]
svm_snps['CONT']=[0,0]

knn_snp_file=open('knn+snp.train.result','r')
knn_snps_file=open('knn+snps.train.result','r')
svm_snp_file=open('svm+snp.train.result','r')
svm_snps_file=open('svm+snps.train.result','r')
file=open(sys.argv[1],'r')
names=['CASE','CONT']
c=1
num=0
for line in knn_snp_file.xreadlines():
	line=line[:-1]
	if c == int(sys.argv[2]):
		element=line.split(' ')
		tp=float(element[3])
		tn=float(element[4])
		fp=float(element[5])
		fn=float(element[6])
		num=tp+fn
		knn_snp['CASE']=[tp/(tp+fn),fn/(tp+fn)]		
		knn_snp['CONT']=[tn/(tn+fp),fp/(tn+fp)]		
		break	
	c=c+1
c=1
for line in knn_snps_file.xreadlines():
        line=line[:-1]
        if c == int(sys.argv[2]):
                element=line.split(' ')
                tp=float(element[4])
                tn=float(element[5])
                fp=float(element[6])
                fn=float(element[7])
                knn_snps['CASE']=[tp/(tp+fn),fn/(tp+fn)]     
                knn_snps['CONT']=[tn/(tn+fp),fp/(tn+fp)]
                break
        c=c+1	
c=1
for line in svm_snp_file.xreadlines():
        line=line[:-1]
        if c == int(sys.argv[2]):
                element=line.split(' ')
                tp=float(element[2])
                tn=float(element[3])
                fp=float(element[4])
                fn=float(element[5])
                svm_snp['CASE']=[tp/(tp+fn),fn/(tp+fn)]     
                svm_snp['CONT']=[tn/(tn+fp),fp/(tn+fp)]
                break
        c=c+1
c=1
for line in svm_snps_file.xreadlines():
        line=line[:-1]
        if c == int(sys.argv[2]):
                element=line.split(' ')
                tp=float(element[3])
                tn=float(element[4])
                fp=float(element[5])
                fn=float(element[6])
                svm_snps['CASE']=[tp/(tp+fn),fn/(tp+fn)]     
                svm_snps['CONT']=[tn/(tn+fp),fp/(tn+fp)]
                break
        c=c+1
case=0
control=0
tp=0
tn=0
fp=0
fn=0
print knn_snp
print knn_snps
print svm_snp
print svm_snps
for line in file.xreadlines():
	line=line[:-1]
	element=line.split('\t')
	vector=[]
	total=0
	prob={}
	for name in names:
		#print name+'\t'+element[1]+'\t'+str(fip_snp[name][names.index(element[1])])
		#print name+'\t'+element[2]+'\t'+str(fip_snps[name][names.index(element[2])])
		#print name+'\t'+element[3]+'\t'+str(svm_snp[name][names.index(element[3])])
		#print name+'\t'+element[4]+'\t'+str(svm_snps[name][names.index(element[4])])
	
		if element[1] == '2':
			a1=knn_snp[name][0]
		else:
			a1=knn_snp[name][1]
		if element[2] == '2':
			a2=knn_snps[name][0]
		else:
			a2=knn_snps[name][1]
		if element[3] == '2':
			a3=svm_snp[name][0]
		else:
			a3=svm_snp[name][1]
		if element[4] == '2':
			a4=svm_snps[name][0]
		else:
			a4=svm_snps[name][1]
	
		z=float(1)/float(num)
		p=0
		if a1 != 0:
			p=a1
		else:
			p=z
		if a2 != 0:
			p=p*a2
		else:
			p=p*z
		if a3 != 0:
			p=p*a3
		else:
			p=p*z
		if a4 != 0:
			p=p*a4
		else:
			p=p*z
		total=total+p
		prob[name]=p
	for name in names:
		p=prob[name]
		vector.append((name,float(p)/total))
	vector.sort(key=operator.itemgetter(1))
	if vector[1][0] == 'CASE':
		print line+'\t2\t'+str(vector[1][1])
	else:
		print line+'\t1\t'+str(vector[1][1])

	if element[0].startswith(sys.argv[3]) == True:
                case=case+1
                if vector[1][0] == 'CASE':
                        tp=tp+1
                else:
                        fn=fn+1
        else:
                control=control+1
                if vector[1][0] == 'CONT':
                        tn=tn+1
                else:
                        fp=fp+1
        c=c+1
mcc=0
if tp+fp != 0 and tp+fn != 0 and tn+fp != 0 and tn+fn != 0:
        mcc=(tp*tn-fp*fn)/math.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))
print str(tp)+'\t'+str(tn)+'\t'+str(fp)+'\t'+str(fn)+'\t'+str(mcc)

	#nline=element[0][:-4]
	#for i in range(0,len(vector)):
	#	nline=nline+'\t'+str(vector[2-i][0])+'\t'+str(vector[2-i][1])
	#print nline

