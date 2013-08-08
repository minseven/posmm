#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y
#$ -V

DIR=$1
LIST=$2
l=$3
p1=$4
i=$5
m=$6
n=$7

M_LABEL=`(gawk '{ if ($2 == $m) print $1}' $DIR/svm+snps/snps.class_num)`
N_LABEL=`(gawk '{ if ($2 == $n) print $1}' $DIR/svm+snps/snps.class_num)`

rm $DIR/svm+snps/l$l/${p1}/snps.$i.c$m$n.matrix.tmp
for name in $(cat $DIR/$LIST | egrep '$M_LABEL|$N_LABEL');
do
	~/bin/profile_selected_snps_unnormalize.py $DIR/svm+snps/l$l/${p1}/snps.$i.c$m$n.list fasta/$name.fasta $l $DIR/svm+snps/l$l/${p1}/snps.$name.$i.c$m$n.matrix.tmp
done
name=`(head -n $i $DIR/$LIST | tail -n 1)`
~/bin/profile_selected_snps_unnormalize.py $DIR/svm+snps/l$l/${p1}/snps.$i.c$m$n.list fasta/$name.fasta $l $DIR/svm+snps/l$l/${p1}/snps.$name.$i.c$m$n.matrix.tmp
