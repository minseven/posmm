#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y

DIR=$1
LIST=$2
l=$3
f=$4

SIZE=`(wc -l ${DIR}/${LIST} | gawk '{print $1}')`

mkdir -p $DIR/knn+snps/l$l/f$f
gawk -v t=$f -v s=$SIZE '{ if ($1 < t/100*s) print $2 }' $DIR/knn+snps/l$l/snps+count.tmp > $DIR/knn+snps/l$l/f$f/snps.list
rm $DIR/knn+snps/l$l/f$f/snps.matrix.tmp
rm $DIR/knn+snps/l$l/f$f/snps.jsd.tmp
for name in $(cat $DIR/$LIST);
do
	~/bin/profile_selected_snps.py $DIR/knn+snps/l$l/f$f/snps.list fasta/$name.fasta $l $DIR/knn+snps/l$l/f$f/snps.$name.matrix.tmp    
done
