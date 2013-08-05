#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y

DIR=$1
LIST=$2
l=$3

SIZE=`(wc -l ${DIR}/${LIST} | gawk '{print $1}')`

mkdir -p $DIR/knn+snps/l$l
rm $DIR/knn+snps/l$l/snps.tmp
for name in $(cat $DIR/$LIST);
do
	~/bin/profile_snps.py fasta/$name.fasta $l >> $DIR/knn+snps/l$l/snps.tmp
done
sort $DIR/knn+snps/l$l/snps.tmp | uniq -c | gawk '{print $1 "\t" $2}' > $DIR/knn+snps/l$l/snps+count.tmp
