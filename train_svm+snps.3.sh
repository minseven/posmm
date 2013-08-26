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

rm $DIR/svm+snps/l$l/${p1}/snps.$i.matrix.tmp
for name in $(cat $DIR/$LIST);
do
	~/bin/profile_selected_snps_unnormalize.py $DIR/svm+snps/l$l/${p1}/snps.$i.list fasta/$name.fasta $l $DIR/svm+snps/l$l/${p1}/snps.$name.$i.matrix.tmp
done
