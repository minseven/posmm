#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y
#$ -V

DIR=$1
TRAIN_LIST=$2
TEST_LIST=$3
CASE=$4
l=$5
p1=$6

rm $DIR/svm+snps/l$l/${p1}/test_snps.matrix.tmp
rm $DIR/svm+snps/l$l/${p1}/train_snps.matrix.tmp
for name in $(cat $DIR/$TEST_LIST);
do
	a=`(gawk '{print NF}' $DIR/svm+snps/l$l/${p1}/test_snps.$name.matrix.tmp)`
        if [ $a -eq 0 ];
        then
                echo "1" > $DIR/svm+snps/l$l/${p1}/test_snps.$name.matrix.tmp
        fi
	cat $DIR/svm+snps/l$l/${p1}/test_snps.$name.matrix.tmp >> $DIR/svm+snps/l$l/${p1}/test_snps.matrix.tmp
done

for name in $(cat $DIR/$TRAIN_LIST);
do
        a=`(gawk '{print NF}' $DIR/svm+snps/l$l/${p1}/test_snps.$name.matrix.tmp)`
        if [ $a -eq 0 ];
        then
                echo "1" > $DIR/svm+snps/l$l/${p1}/train_snps.$name.matrix.tmp
        fi
        cat $DIR/svm+snps/l$l/${p1}/test_snps.$name.matrix.tmp >> $DIR/svm+snps/l$l/${p1}/train_snps.matrix.tmp
done


~/bin/FIP_to_libsvm2.py $DIR/$TEST_LIST $DIR/svm+snps/l$l/${p1}/test_snps.matrix.tmp $DIR/svm+snps/l$l/${p1}/test_snps.libsvm $CASE
~/bin/FIP_to_libsvm2.py $DIR/$TRAIN_LIST $DIR/svm+snps/l$l/${p1}/train_snps.matrix.tmp $DIR/svm+snps/l$l/${p1}/train_snps.libsvm $CASE
~/bin/easy_svm.py $DIR/svm+snps/l$l/${p1}/train_snps.libsvm $DIR/svm+snps/l$l/${p1}/test_snps.libsvm
