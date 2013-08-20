#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y
#$ -V

DIR=$1
LIST=$2
SIZE=`(wc -l $DIR/$LIST | gawk '{print $1}')`
CASE=$3
l=$4
i=$5

NCASE=`(grep ^$CASE $DIR/$LIST.train$i | wc -l | gawk '{print $1}')`
NCONTROL=`(grep -v ^$CASE $DIR/$LIST.train$i | wc -l | gawk '{print $1}')`

rm $DIR/svm+snps/l$l/snps.$i.cases.tmp $DIR/svm+snps/l$l/snps.$i.controls.tmp $DIR/svm+snps/l$l/snps+count.$i.*
for name in $(cat $DIR/$LIST.train$i | grep ^$CASE);
do
	~/bin/profile_snps.py fasta/$name.fasta $l >> $DIR/svm+snps/l$l/snps.$i.cases.tmp
done
sort $DIR/svm+snps/l$l/snps.$i.cases.tmp | uniq -c | gawk '{print $1 "\t" $2}' | sed '1d' > $DIR/svm+snps/l$l/snps+count.$i.cases.tmp

for name in $(cat $DIR/$LIST.train$i | grep -v ^$CASE); 
do
	~/bin/profile_snps.py fasta/$name.fasta $l >> $DIR/svm+snps/l$l/snps.$i.controls.tmp
done
sort $DIR/svm+snps/l$l/snps.$i.controls.tmp | uniq -c | gawk '{print $1 "\t" $2}' | sed '1d' > $DIR/svm+snps/l$l/snps+count.$i.controls.tmp

~/bin/svm+snps_pvalue2.py $DIR/svm+snps/l$l/snps+count.$i.cases.tmp $DIR/svm+snps/l$l/snps+count.$i.controls.tmp $NCASE $NCONTROL $DIR/svm+snps/l$l/snps.$i.tmp1
~/bin/svm+snps_pvalue2.py $DIR/svm+snps/l$l/snps+count.$i.controls.tmp $DIR/svm+snps/l$l/snps+count.$i.cases.tmp $NCONTROL $NCASE $DIR/svm+snps/l$l/snps.$i.tmp2
cp $DIR/svm+snps/l$l/snps.$i.tmp1 $DIR/svm+snps/l$l/snps.$i.tmp3
cat $DIR/svm+snps/l$l/snps.$i.tmp2 >> $DIR/svm+snps/l$l/snps.$i.tmp3
sort $DIR/svm+snps/l$l/snps.$i.tmp3 | uniq -c | gawk '{print $2 "\t" $3}' > $DIR/svm+snps/l$l/snps.$i.list
#rm $DIR/svm+snps/l$l/snps.$i.tmp* $DIR/svm+snps/l$l/snps+count.$i.*.tmp
