#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y
#$ -V

DIR=$1
LIST=$2
DATASET=$3
SIZE=`(wc -l $DIR/$LIST | gawk '{print $1}')`
f=$4

mkdir -p $DIR/knn+snp
gawk '{ print $1 " " $1}' $DIR/$LIST > $DIR/$LIST.plink
~/bin/plink --noweb --file $DATASET.code --keep $DIR/$LIST.plink --recode --out $DIR/knn+snp/test_snp

~/bin/plink --noweb --file $DIR/knn+snp/test_snp --extract $DIR/knn+snp/f$f/snp.list --recode --out $DIR/knn+snp/f$f/test_snp
~/bin/PLINK_to_FIP.py $DIR/knn+snp/f$f/test_snp.ped $DIR/knn+snp/f$f/test_snp.matrix.tmp

NCOL=`(wc -l $DIR/knn+snp/f$f/snp.list | gawk '{print $1}')`
rm $DIR/knn+snp/f$f/test_snp.jsd.tmp
for i in $(seq 1 1 $SIZE);
do
	head -n $i $DIR/knn+snp/f$f/test_snp.matrix.tmp | tail -n 1 > $DIR/knn+snp/f$f/test_snp.$i.matrix.tmp
	cat $DIR/knn+snp/f$f/snp.matrix.tmp >> $DIR/knn+snp/f$f/test_snp.$i.matrix.tmp
	NROW=`(wc -l $DIR/knn+snp/f$f/test_snp.$i.matrix.tmp | gawk '{print $1}')`
	~/bin/ffpjsd -j --nrow $SIZE --ncol $NCOL -r 1 $DIR/knn+snp/f$f/test_snp.$i.matrix.tmp > $DIR/knn+snp/f$f/test_snp.$i.jsd.tmp
done
