#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y
#$ -V

DIR=$1
LIST=$2
f=$3
SIZE=`(wc -l $DIR/$LIST | gawk '{print $1}')`

echo $f
mkdir -p $DIR/knn+snp/f$f
gawk -v t=$f '{ if ($5 < t/100) print $2 }' $DIR/knn+snp/snp.frq > $DIR/knn+snp/f$f/snp.list
wc -l $DIR/knn+snp/f$f/snp.list
~/bin/plink --noweb --file $DIR/knn+snp/snp --extract $DIR/knn+snp/f$f/snp.list --recode --out $DIR/knn+snp/f$f/snp
~/bin/PLINK_to_FIP.py $DIR/knn+snp/f$f/snp.ped $DIR/knn+snp/f$f/snp.matrix.tmp
NCOL=`(wc -l $DIR/knn+snp/f$f/snp.list | gawk '{print $1}')`
rm $DIR/knn+snp/f$f/snp.jsd.tmp
for i in $(seq 1 1 $SIZE);
do
	~/bin/ffpjsd -j --nrow $SIZE --ncol $NCOL -r $i $DIR/knn+snp/f$f/snp.matrix.tmp >> $DIR/knn+snp/f$f/snp.jsd.tmp
done
