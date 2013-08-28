#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y
#$ -V

DIR=$1
LIST=$2
SIZE=`(wc -l $DIR/$LIST | gawk '{print $1}')`
CASE=$3
i=$4
p1=$5

mkdir $DIR/svm+snp/${p1}
#~/bin/plink --tped $DIR/svm+snp/snp.tped --tfam $DIR/svm+snp/snp.$i.tfam --assoc --adjust --out $DIR/svm+snp/snp.$i
sed '1d' $DIR/svm+snp/snp.$i.assoc.adjusted | sort -k 3 -g | head -n $p1 | gawk '{print $2}' > $DIR/svm+snp/${p1}/snp.$i.list

~/bin/plink --noweb --tped $DIR/svm+snp/snp.tped --tfam $DIR/svm+snp/snp.$i.tfam --extract $DIR/svm+snp/${p1}/snp.$i.list --recode --out $DIR/svm+snp/${p1}/snp.$i

~/bin/PLINK_to_libsvm.py $DIR/svm+snp/${p1}/snp.$i.ped $DIR/svm+snp/${p1}/snp.$i $i $CASE

~/bin/easy_svm.py $DIR/svm+snp/${p1}/snp.$i.train $DIR/svm+snp/${p1}/snp.$i.test
