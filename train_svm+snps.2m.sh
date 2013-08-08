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
m=$6
n=$7

M_LABEL=`(gawk '{ if ($2 == $m) print $1}' $DIR/svm+snps/snps.class_num)`
N_LABEL=`(gawk '{ if ($2 == $n) print $1}' $DIR/svm+snps/snps.class_num)`

M_SIZE=`(grep ^$M_LABEL $DIR/svm+snps/snps.$i.c$m$n.tfam | grep -v [-][9] | wc -l | gawk '{print $1}')`
N_SIZE=`(grep ^$N_LABEL $DIR/svm+snps/snps.$i.c$m$n.tfam | grep -v [-][9] | wc -l | gawk '{print $1}')`

rm $DIR/svm+snps/l$l/snps.$i.c$m$n.tmp* $DIR/svm+snps/l$l/snps+count.$i.c$m$n.*
for name in $(cat $DIR/svm+snps/snps.$i.c$m$n.tfam | grep -v [-][9] | grep ^$M_LABEL | gawk '{print $1}');
do
	~/bin/profile_snps.py fasta/$name.fasta $l >> $DIR/svm+snps/l$l/snps.$i.c$m$n.cases.tmp
done
sort $DIR/svm+snps/l$l/snps.$i.c$m$n.cases.tmp | uniq -c | gawk '{print $1 "\t" $2}' | sed '1d' > $DIR/svm+snps/l$l/snps+count.$i.c$m$n.cases.tmp

for name in $(cat $DIR/svm+snps/snps.$i.c$m$n.tfam | grep -v [-][9] | grep ^$N_LABEL | gawk '{print $1}');
do
	~/bin/profile_snps.py fasta/$name.fasta $l >> $DIR/svm+snps/l$l/snps.$i.c$m$n.controls.tmp
done
sort $DIR/svm+snps/l$l/snps.$i.c$m$n.controls.tmp | uniq -c | gawk '{print $1 "\t" $2}' | sed '1d' > $DIR/svm+snps/l$l/snps+count.$i.c$m$n.controls.tmp

~/bin/svm+snps_pvalue2.py $DIR/svm+snps/l$l/snps+count.$i.c$m$n.cases.tmp $DIR/svm+snps/l$l/snps+count.$i.c$m$n.controls.tmp $M_SIZE $N_SIZE $DIR/svm+snps/l$l/snps.$i.c$m$n.tmp1
~/bin/svm+snps_pvalue2.py $DIR/svm+snps/l$l/snps+count.$i.c$m$n.controls.tmp $DIR/svm+snps/l$l/snps+count.$i.c$m$n.cases.tmp $N_SIZE $M_SIZE $DIR/svm+snps/l$l/snps.$i.c$m$n.tmp2
cp $DIR/svm+snps/l$l/snps.$i.c$m$n.tmp1 $DIR/svm+snps/l$l/snps.$i.c$m$n.tmp3
cat $DIR/svm+snps/l$l/snps.$i.c$m$n.tmp2 >> $DIR/svm+snps/l$l/snps.$i.c$m$n.tmp3
sort $DIR/svm+snps/l$l/snps.$i.c$m$n.tmp3 | uniq -c | gawk '{print $2 "\t" $3}' > $DIR/svm+snps/l$l/snps.$i.c$m$n.list
rm $DIR/svm+snps/l$l/snps.$i.c$m$n.tmp* $DIR/svm+snps/l$l/snps+count.$i.c$m$n.*.tmp

for p1 in 10 50 100 500 1000;
do
        mkdir -p $DIR/svm+snps/l$l/${p1}
        sort -k 2 -g $DIR/svm+snps/l$l/snps.$i.c$m$n.list | head -n ${p1} | gawk '{print $1}' > $DIR/svm+snps/l$l/${p1}/snps.$i.c$m$n.list
done
