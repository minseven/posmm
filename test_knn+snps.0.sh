#!/bin/bash

ARG=$1
DATA=$2
CASE_LABEL=$3
FILE=$4

while read f1 f2 f3 f4 f5 f6 f7 f8 f9;
do
	if [ $ARG == 'step1' ];
	then
		~/bin/test_knn+snps.1.sh r$f1 $DATA.$f1.test.list $f2 $f3
	elif [ $ARG == 'step2' ];
	then
		~/bin/test_knn+snps.2.sh r$f1 $DATA.$f1.test.list $f2 $f3
	elif [ $ARG == 'result' ];
	then
		a=`(~/bin/get_accuracy_one_k.py r$f1/$DATA.$f1.train.list r$f1/$DATA.$f1.test.list r$f1/knn+snps/l$f2/f$f3/test_snps $CASE_LABEL $f4)`; 
    		echo $f1 $f2 $f3 $f4 $a;
	fi

done < $FILE
