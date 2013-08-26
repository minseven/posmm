#!/bin/bash

FILE=$1

while read f1 f2 f3 f4 f5
do
	echo $f1 $f2
	qsub ~/bin/test_svm+snp.1.sh r$f1 lqt+conA.$f1.test.list  ~/dataset/other_disease/LQTS/diLQTS.qc.inf LQTS $f2
done < $FILE
