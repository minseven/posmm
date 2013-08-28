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
p1=$5

gawk '{ print $1 " " $1}' $DIR/$LIST > $DIR/$LIST.plink
~/bin/plink --noweb --file $DATASET.code --keep $DIR/$LIST.plink --transpose --recode --out $DIR/svm+snp/test_snp

~/bin/plink --noweb --tfile $DIR/svm+snp/snp --assoc --adjust --out $DIR/svm+snp/snp

####sed '1d' $DIR/svm+snp/snp.assoc.adjusted | gawk -v v=$p2 '{ if ($3 < v) print $2}' > $DIR/svm+snp/${p1}/snp.list
sed '1d' $DIR/svm+snp/snp.assoc.adjusted | sort -k 3 -g | head -n $p1 | gawk '{print $2}' > $DIR/svm+snp/${p1}/test_snp.list

~/bin/plink --noweb --tfile $DIR/svm+snp/test_snp --extract $DIR/svm+snp/${p1}/test_snp.list --recode --out $DIR/svm+snp/${p1}/test_snp
~/bin/plink --noweb --tfile $DIR/svm+snp/snp --extract $DIR/svm+snp/${p1}/test_snp.list --recode --out $DIR/svm+snp/${p1}/snp

~/bin/PLINK_to_libsvm2.py $DIR/svm+snp/${p1}/test_snp.ped $DIR/svm+snp/${p1}/test_snp.test
~/bin/PLINK_to_libsvm2.py $DIR/svm+snp/${p1}/snp.ped $DIR/svm+snp/${p1}/test_snp.train

~/bin/easy_svm.py $DIR/svm+snp/${p1}/test_snp.train $DIR/svm+snp/${p1}/test_snp.test
