#!/bin/bash

DIR=$1
LIST=$2
l=$3
f=$4

SIZE=`(wc -l ${DIR}/${LIST} | gawk '{print $1}')`
rm $DIR/knn+snps/l$l/f$f/snps.matrix.tmp
for name in $(cat $DIR/$LIST);
do
	a=`(gawk '{print NF}' $DIR/knn+snps/l$l/f$f/snps.$name.matrix.tmp)`
	if [ $a -eq 0 ];
	then
		echo -e "1	1" > $DIR/knn+snps/l$l/f$f/snps.$name.matrix.tmp
	fi
	cat $DIR/knn+snps/l$l/f$f/snps.$name.matrix.tmp >> $DIR/knn+snps/l$l/f$f/snps.matrix.tmp
done
NCOL=`(wc -l $DIR/knn+snps/l$l/f$f/snps.list | gawk '{print $1}')`
for i in $(seq 1 1 $SIZE);
do
	qsub ~/bin/run_ffpjsd.one.sh $SIZE $NCOL $i $DIR/knn+snps/l$l/f$f/snps.matrix.tmp $DIR/knn+snps/l$l/f$f/snps.$i.jsd.tmp
done
