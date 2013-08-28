#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y

DIR=$1
LIST=$2
l=$3
f=$4

for name in $(cat $DIR/$LIST);
do
	#ls -hl $DIR/knn+snps/l$l/f$f/snps.$name.matrix.tmp
	qsub ~/bin/run.sh ~/bin/profile_selected_snps.py $DIR/knn+snps/l$l/f$f/snps.list fasta/$name.fasta $l $DIR/knn+snps/l$l/f$f/snps.$name.matrix.tmp    
	#~/bin/profile_selected_snps.py $DIR/knn+snps/l$l/f$f/snps.list fasta/$name.fasta $l $DIR/knn+snps/l$l/f$f/snps.$name.matrix.tmp    
done
