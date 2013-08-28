#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y
#$ -V

DIR=$1
LIST=$2
CASE=$3
l=$4
p1=$5
i=$6

mkdir -p $DIR/svm+snps/l$l/${p1}
#sort -k 2 -g $DIR/svm+snps/l$l/snps.$i.list | gawk '{ if ($2 > 0) print $0}' | head -n ${p1} | gawk '{print $1}' > $DIR/svm+snps/l$l/${p1}/snps.$i.list

#rm $DIR/svm+snps/l$l/${p1}/snps.$i.matrix.tmp
#for name in $(cat $DIR/$LIST);
#do
#	~/bin/profile_selected_snps_unnormalize.py $DIR/svm+snps/l$l/${p1}/snps.$i.list fasta/$name.fasta $l $DIR/svm+snps/l$l/${p1}/snps.$name.$i.matrix.tmp
#done

#for name in $(cat $DIR/$LIST.train$i);
#do
#        a=`(gawk '{print NF}' $DIR/svm+snps/l$l/${p1}/snps.$name.$i.matrix.tmp)`
#        if [ $a -eq 0 ];
#        then
#                echo "1" > $DIR/svm+snps/l$l/${p1}/snps.$name.$i.matrix.tmp
#        fi
#        cat $DIR/svm+snps/l$l/${p1}/snps.$name.$i.matrix.tmp >> $DIR/svm+snps/l$l/${p1}/snps.train$i.matrix.tmp
#done

#for name in $(cat $DIR/$LIST.test$i);
#do
#        a=`(gawk '{print NF}' $DIR/svm+snps/l$l/${p1}/snps.$name.$i.matrix.tmp)`
#        if [ $a -eq 0 ];
#        then
#                echo "1" > $DIR/svm+snps/l$l/${p1}/snps.$name.$i.matrix.tmp
#        fi
#        cat $DIR/svm+snps/l$l/${p1}/snps.$name.$i.matrix.tmp >> $DIR/svm+snps/l$l/${p1}/snps.test$i.matrix.tmp
#done


#~/bin/FIP_to_libsvm.py $DIR/$LIST.train$i $DIR/svm+snps/l$l/${p1}/snps.$i.matrix.tmp $DIR/svm+snps/l$l/${p1}/snps.libsvm.$i $i $CASE
~/bin/FIP_to_libsvm2.py $DIR/$LIST.train$i $DIR/svm+snps/l$l/${p1}/snps.train$i.matrix.tmp $DIR/svm+snps/l$l/${p1}/snps.libsvm.$i.train $CASE
~/bin/FIP_to_libsvm2.py $DIR/$LIST.test$i $DIR/svm+snps/l$l/${p1}/snps.test$i.matrix.tmp $DIR/svm+snps/l$l/${p1}/snps.libsvm.$i.test $CASE
~/bin/easy_svm.py $DIR/svm+snps/l$l/${p1}/snps.libsvm.$i.train $DIR/svm+snps/l$l/${p1}/snps.libsvm.$i.test
