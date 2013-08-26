#!/bin/bash

FILE=$1

while read f1 f2 f3 f4 f5 f6 f7
do
	echo $f1 $f2
	~/bin/test_knn+snps.1.sh r$f1 lqt+conA.$f1.test.list $f2 $f3
done < $FILE
