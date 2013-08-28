#!/bin/bash

ARG=$1
DATA=$2
CASE_LABEL=$3
FILE=$4

#l=`(sort -k 8 -g -r $FILE | head -n 1 | gawk '{print $2}')`
#p=`(sort -k 8 -g -r $FILE | head -n 1 | gawk '{print $3}')`

#for i in $(seq 1 1 10); 
#do
#	if [ $ARG == 'step1'  ];
#	then 
#        	echo $i $l $p
#		qsub ~/bin/test_svm+snps.1.sh r$i $DATA.$i.train.list $DATA.$i.test.list $CASE_LABEL $l $p
#	elif [ $ARG == 'step2' ];
#      	then
#        	qsub ~/bin/test_svm+snps.2.sh r$i $DATA.$i.train.list $DATA.$i.test.list $CASE_LABEL $l $p 
#       	elif [ $ARG == 'result' ];
#       	then
#        	a=`(~/bin/get_accuracy_svm_test.py r$i/$DATA.$i.train.list r$i/svm+snps/l$l/$p/test_snps.libsvm r$i/svm+snps/l$l/$p/train_snps.libsvm.predict $CASE_LABEL)`;
#        	echo $i $l $p $a;
#       	fi
#done

while read f1 f2 f3 f4 f5 f6 f7 f8;
do
	if [ $ARG == 'step1'  ];
	then 
		#echo $f1 $f2 $f3
		qsub ~/bin/test_svm+snps.1.sh r$f1 $DATA.$f1.train.list $DATA.$f1.test.list $CASE_LABEL $f2 $f3 
	elif [ $ARG == 'step2' ];
	then
		qsub ~/bin/test_svm+snps.2.sh r$f1 $DATA.$f1.train.list $DATA.$f1.test.list $CASE_LABEL $f2 $f3 
	elif [ $ARG == 'result' ];
	then
		a=`(~/bin/get_accuracy_svm_test.py r$f1/$DATA.$f1.train.list r$f1/svm+snps/l$f2/$f3/test_snps.libsvm r$f1/svm+snps/l$f2/$f3/train_snps.libsvm.predict $CASE_LABEL)`;
   		echo $f1 $f2 $f3 $a;
	fi
done < $FILE
