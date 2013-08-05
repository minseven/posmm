#!/bin/bash

FILE=$1

while read f1 f2 f3 f4 f5 f6
do
	~/bin/test_svm+snps.1.sh r$f1 lqt+conA.$f1.train.list lqt+conA.$f1.test.list LQTS $f2 $f3 
done < $FILE
