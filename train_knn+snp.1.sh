#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y
#$ -V

DIR=$1
LIST=$2
DATASET=$3
SIZE=`(wc -l $DIR/$LIST | gawk '{print $1}')`

mkdir -p $DIR/knn+snp
gawk '{ print $1 " " $1}' $DIR/$LIST > $DIR/$LIST.plink
~/bin/plink --noweb --file $DATASET.code --keep $DIR/$LIST.plink --recode --out $DIR/knn+snp/snp
~/bin/plink --noweb --file $DIR/knn+snp/snp --freq --out $DIR/knn+snp/snp

