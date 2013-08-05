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

NCASE=`(grep ^$CASE $DIR/svm+snps/snps.tfam |  wc -l | gawk '{print $1}')`
NCONTROL=`(grep -v ^$CASE $DIR/svm+snps/snps.tfam | wc -l | gawk '{print $1}')`

rm $DIR/svm+snps.l$l/test_snps.*.tmp
for name in $(cat $DIR/svm+snps/snps.tfam | grep ^$CASE | gawk '{print $1}');
do
        ~/bin/profile_snps.py fasta/$name.fasta $l >> $DIR/svm+snps/l$l/test_snps.cases.tmp
done
sort $DIR/svm+snps/l$l/test_snps.cases.tmp | uniq -c | gawk '{print $1 "\t" $2}' | sed '1d' > $DIR/svm+snps/l$l/test_snps.count.cases.tmp

for name in $(cat $DIR/svm+snps/snps.tfam | grep -v ^$CASE | gawk '{print $1}');
do
        ~/bin/profile_snps.py fasta/$name.fasta $l >> $DIR/svm+snps/l$l/test_snps.controls.tmp
done
sort $DIR/svm+snps/l$l/test_snps.controls.tmp | uniq -c | gawk '{print $1 "\t" $2}' | sed '1d' > $DIR/svm+snps/l$l/test_snps.count.controls.tmp

~/bin/svm+snps_pvalue2.py $DIR/svm+snps/l$l/test_snps.count.cases.tmp $DIR/svm+snps/l$l/test_snps.count.controls.tmp $NCASE $NCONTROL $DIR/svm+snps/l$l/test_snps.tmp1
~/bin/svm+snps_pvalue2.py $DIR/svm+snps/l$l/test_snps.count.controls.tmp $DIR/svm+snps/l$l/test_snps.count.cases.tmp $NCASE $NCONTROL $DIR/svm+snps/l$l/test_snps.tmp2
cp $DIR/svm+snps/l$l/test_snps.tmp1 $DIR/svm+snps/l$l/test_snps.tmp3
cat $DIR/svm+snps/l$l/test_snps.tmp2 >> $DIR/svm+snps/l$l/test_snps.tmp3
sort $DIR/svm+snps/l$l/test_snps.tmp3 | uniq -c | gawk '{print $2 "\t" $3}' > $DIR/svm+snps/l$l/test_snps.list

for name in $(cat $DIR/$TRAIN_LIST $DIR/$TEST_LIST);
do
	~/bin/run.sh ~/bin/profile_selected_snps_unnormalize.py $DIR/svm+snps/l$l/${p1}/test_snps.list fasta/$name.fasta $l $DIR/svm+snps/l$l/${p1}/test_snps.$name.matrix.tmp
done
