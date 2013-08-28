#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y
#$ -V

DIR=$1
LIST=$2
DATASET=$3
SIZE=`(wc -l $DIR/$LIST | gawk '{print $1}')`
CASE=$4
l=$5

NCASE=`(grep ^$CASE $DIR/$LIST | wc -l | gawk '{print $1}')`
NCONTROL=`(grep ^$CASE $DIR/$LIST | wc -l | gawk '{print $1}')`

if [ ! -f $DIR/$LIST.plink ];
then
	gawk '{ print $1 " " $1}' $DIR/$LIST > $DIR/$LIST.plink
fi

if [ ! -f $DIR/svm+snps/snps.tped ] && [ ! -f $DIR/svm+snps/snps.tfam ];
then
	~/bin/plink --noweb --file $DATASET.code --keep $DIR/$LIST.plink --transpose --recode --out $DIR/svm+snps/snps
fi
#~/bin/make_svm_snp_train_tfam.py $DIR/svm+snps/snps.tfam $DIR/svm+snps/snps $CASE
~/bin/split_train_test_data.py $DIR/$LIST $CASE $DIR/$LIST.test
for i in $(seq 1 1 10);
do
        cat $DIR/$LIST $DIR/$LIST.test$i | sort | uniq -c | gawk '{ if ($1 == 1) print $2}' > $DIR/$LIST.train$i
done

mkdir -p $DIR/svm+snps/l$l
