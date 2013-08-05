#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y
#$ -V

DIR=$1
LIST=$2
SIZE=`(wc -l $DIR/$LIST | gawk '{print $1}')`
CASE=$3
m=$4
i=$5
j=$6
p1=$7

~/bin/plink --noweb --tped $DIR/svm+snp/snp.tped --tfam $DIR/svm+snp/snp.$m.c$i$j.tfam --assoc --adjust --out $DIR/svm+snp/snp.$m.c$i$j
sed '1d' $DIR/svm+snp/snp.$m.c$i$j.assoc.adjusted | sort -k 3 -g | head -n $p1 | gawk '{print $2}' > $DIR/svm+snp/${p1}/snp.$m.c$i$j.list

~/bin/plink --noweb --tped $DIR/svm+snp/snp.tped --tfam $DIR/svm+snp/snp.$m.c$i$j.tfam --extract $DIR/svm+snp/${p1}/snp.$m.c$i$j.list --recode --out $DIR/svm+snp/${p1}/snp.$m.c$i$j.list

~/bin/PLINK_to_libsvm.py $DIR/svm+snp/${p1}/snp.$i.ped $DIR/svm+snp/${p1}/snp.$i $i $CASE

~/bin/easy_svm.py svm+snp/${p1}/snp.$m.c$i$j.train svm+snp/${p1}/snp.$m.c$i$j.test
