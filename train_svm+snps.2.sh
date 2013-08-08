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

NCASE=`(grep ^$CASE $DIR/svm+snps/snps.$i.tfam | grep -v [-][9] | wc -l | gawk '{print $1}')`
NCONTROL=`(grep -v ^$CASE $DIR/svm+snps/snps.$i.tfam | grep -v [-][9] | wc -l | gawk '{print $1}')`

rm $DIR/svm+snps/l$l/snps.$i.tmp* $DIR/svm+snps/l$l/snps+count.$i.*
for name in $(cat $DIR/svm+snps/snps.$i.tfam | grep -v [-][9] | grep ^$CASE | gawk '{print $1}');
do
	~/bin/profile_snps.py fasta/$name.fasta $l >> $DIR/svm+snps/l$l/snps.$i.cases.tmp
done
sort $DIR/svm+snps/l$l/snps.$i.cases.tmp | uniq -c | gawk '{print $1 "\t" $2}' | sed '1d' > $DIR/svm+snps/l$l/snps+count.$i.cases.tmp

for name in $(cat $DIR/svm+snps/snps.$i.tfam | grep -v [-][9] | grep -v ^$CASE | gawk '{print $1}');
do
	~/bin/profile_snps.py fasta/$name.fasta $l >> $DIR/svm+snps/l$l/snps.$i.controls.tmp
done
sort $DIR/svm+snps/l$l/snps.$i.controls.tmp | uniq -c | gawk '{print $1 "\t" $2}' | sed '1d' > $DIR/svm+snps/l$l/snps+count.$i.controls.tmp

~/bin/svm+snps_pvalue2.py $DIR/svm+snps/l$l/snps+count.$i.cases.tmp $DIR/svm+snps/l$l/snps+count.$i.controls.tmp $NCASE $NCONTROL $DIR/svm+snps/l$l/snps.$i.tmp1
~/bin/svm+snps_pvalue2.py $DIR/svm+snps/l$l/snps+count.$i.controls.tmp $DIR/svm+snps/l$l/snps+count.$i.cases.tmp $NCASE $NCONTROL $DIR/svm+snps/l$l/snps.$i.tmp2
cp $DIR/svm+snps/l$l/snps.$i.tmp1 $DIR/svm+snps/l$l/snps.$i.tmp3
cat $DIR/svm+snps/l$l/snps.$i.tmp2 >> $DIR/svm+snps/l$l/snps.$i.tmp3
sort $DIR/svm+snps/l$l/snps.$i.tmp3 | uniq -c | gawk '{print $2 "\t" $3}' > $DIR/svm+snps/l$l/snps.$i.list
rm $DIR/svm+snps/l$l/snps.$i.tmp* $DIR/svm+snps/l$l/snps+count.$i.*.tmp

#for p1 in 10 50 100 200 400 800 1600;
#do
#        mkdir -p $DIR/svm+snps/l$l/${p1}
#        sort -k 2 -g $DIR/svm+snps/l$l/snps.$i.list | gawk '{ if ($2 > 0) print $0}' | head -n ${p1} | gawk '{print $1}' > $DIR/svm+snps/l$l/${p1}/snps.$i.list
#done
