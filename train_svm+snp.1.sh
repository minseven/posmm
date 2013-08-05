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

mkdir -p $DIR/svm+snp/e3 $DIR/svm+snp/e4 $DIR/svm+snp/e5 $DIR/svm+snp/e6
gawk '{ print $1 " " $1}' $DIR/$LIST > $DIR/$LIST.plink
~/bin/plink --noweb --file $DATASET.code --keep $DIR/$LIST.plink --transpose --recode --out $DIR/svm+snp/snp
if [ $CASE == 'MULTI' ];
then
	~/bin/make_svm_snp_train_tfam_multi.py $DIR/svm+snp/snp.tfam $DIR/svm+snp/snp
else
	~/bin/make_svm_snp_train_tfam.py $DIR/svm+snp/snp.tfam $DIR/svm+snp/snp $CASE
fi
