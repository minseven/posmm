#!/bin/bash

DIR=$1
LIST=$2
l=$3
f=$4

SIZE=`(wc -l ${DIR}/${LIST} | gawk '{print $1}')`
NCOL=`(wc -l $DIR/knn+snps/l$l/f$f/snps.list | gawk '{print $1}')`
for i in $(seq 1 1 $SIZE);
do
	name=`(head -n $i $DIR/$LIST | tail -n 1)`
	cp $DIR/knn+snps/l$l/f$f/snps.$name.matrix.tmp $DIR/knn+snps/l$l/f$f/test_snps.$i.matrix.tmp
	cat $DIR/knn+snps/l$l/f$f/snps.matrix.tmp >> $DIR/knn+snps/l$l/f$f/test_snps.$i.matrix.tmp
	NROW=`(wc -l $DIR/knn+snps/l$l/f$f/test_snps.$i.matrix.tmp | gawk '{print $1}')`
	qsub ~/bin/run_ffpjsd.one.sh $NROW $NCOL 1 $DIR/knn+snps/l$l/f$f/test_snps.$i.matrix.tmp $DIR/knn+snps/l$l/f$f/test_snps.$i.jsd.tmp
done
