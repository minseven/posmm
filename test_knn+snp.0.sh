#!/bin/bash

ARG=$1
DATA=$2
DATASET=$3
CASE_LABEL=$4
FILE=$5

while read f1 f2 f3 f4 f5 f6 f7 f8
do
	if [ $ARG == 'step1' ];
	then
		~/bin/test_knn+snp.1.sh r$f1 $DATA.$f1.test.list $DATASET $f2
	elif [ $ARG == 'result' ];
	then
		a=`(~/bin/get_accuracy_one_k.py r$f1/knn+snp/f$f2/snp.ped r$f1/knn+snp/f$f2/test_snp.ped r$f1/knn+snp/f$f2/test_snp $CASE_LABEL $f3 r$f1/knn+snp.test.result.list)`;
		echo $f1 $f2 $f3 $a;
	fi
done < $FILE
