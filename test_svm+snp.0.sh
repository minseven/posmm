#!/bin/bash

ARG=$1
DATA=$2
DATASET=$3
CASE_LABEL=$4
FILE=$5

while read f1 f2 f3 f4 f5 f6 f7
do
	if [ $ARG == 'step1'  ];
	then
		qsub ~/bin/test_svm+snp.1.sh r$f1 $DATA.$f1.test.list $DATASET $CASE_LABEL $f2
	elif [ $ARG = 'result' ];
	then
		a=`(~/bin/get_accuracy_svm_test.py r$f1/svm+snp/$f2/test_snp.ped r$f1/svm+snp/$f2/test_snp.test r$f1/svm+snp/$f2/test_snp.train.predict $CASE_LABEL r$f1/svm+snp.test.result.list)`;
    		echo $f1 $f2 $a;	
	fi
done < $FILE
