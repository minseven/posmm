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


#mkdir -p $DIR/svm+snp/e3 $DIR/svm+snp/e4 $DIR/svm+snp/e5 $DIR/svm+snp/e6
gawk '{ print $1 " " $1}' $DIR/$LIST > $DIR/$LIST.plink
~/bin/plink --noweb --file $DATASET.code --keep $DIR/$LIST.plink --transpose --recode --out $DIR/svm+snp/snp
~/bin/make_svm_snp_train_tfam.py $DIR/svm+snp/snp.tfam $DIR/svm+snp/snp $CASE

for i in $(seq 1 1 $SIZE);
do
	qsub ~/bin/run.sh ~/bin/plink --tped $DIR/svm+snp/snp.tped --tfam $DIR/svm+snp/snp.$i.tfam --assoc --adjust --out $DIR/svm+snp/snp.$i
done
