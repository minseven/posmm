#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y
#$ -V

DIR=$1
# LIST=$2
f=$2
i=$3

NCOL=`(wc -l $DIR/knn+snp/f$f/snp.list | gawk '{print $1}')`
rm $DIR/knn+snp/f$f/test_snp.jsd.tmp
head -n $i $DIR/knn+snp/f$f/test_snp.matrix.tmp | tail -n 1 > $DIR/knn+snp/f$f/test_snp.$i.matrix.tmp
cat $DIR/knn+snp/f$f/snp.matrix.tmp >> $DIR/knn+snp/f$f/test_snp.$i.matrix.tmp
SIZE=`(wc -l $DIR/knn+snp/f$f/test_snp.$i.matrix.tmp | gawk '{print $1}')`
~/bin/ffpjsd -j --nrow $SIZE --ncol $NCOL -r 1 $DIR/knn+snp/f$f/test_snp.$i.matrix.tmp > $DIR/knn+snp/f$f/test_snp.$i.jsd.tmp
