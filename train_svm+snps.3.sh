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

mkdir -p $DIR/svm+snps/l$l/${p1}
sort -k 2 -g $DIR/svm+snps/l$l/snps.$i.list | gawk '{ if ($2 > 0) print $0}' | head -n ${p1} | gawk '{print $1}' > $DIR/svm+snps/l$l/${p1}/snps.$i.list

rm $DIR/svm+snps/l$l/${p1}/snps.$i.matrix.tmp
for name in $(cat $DIR/$LIST);
do
	~/bin/profile_selected_snps_unnormalize.py $DIR/svm+snps/l$l/${p1}/snps.$i.list fasta/$name.fasta $l $DIR/svm+snps/l$l/${p1}/snps.$name.$i.matrix.tmp
done
