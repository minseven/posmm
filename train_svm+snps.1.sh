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

gawk '{ print $1 " " $1}' $DIR/$LIST > $DIR/$LIST.plink
~/bin/plink --noweb --file $DATASET.code --keep $DIR/$LIST.plink --transpose --recode --out $DIR/svm+snps/snps
~/bin/make_svm_snp_train_tfam.py $DIR/svm+snps/snps.tfam $DIR/svm+snps/snps $CASE

mkdir -p $DIR/svm+snps/l$l
