#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y
#$ -V

DIR=$1
LIST=$2
SIZE=`(wc -l $DIR/$LIST | gawk '{print $1}')`
m=$3
i=$4
j=$5
p1=$6

~/bin/plink --noweb --tped $DIR/svm+snp/snp.tped --tfam $DIR/svm+snp/snp.$m.c$i$j.tfam --assoc --adjust --out $DIR/svm+snp/snp.$m.c$i$j
sed '1d' $DIR/svm+snp/snp.$m.c$i$j.assoc.adjusted | sort -k 3 -g | head -n $p1 | gawk '{print $2}' > $DIR/svm+snp/${p1}/snp.$m.c$i$j.list

~/bin/plink --noweb --tped $DIR/svm+snp/snp.tped --tfam $DIR/svm+snp/snp.$m.c$i$j.tfam --extract $DIR/svm+snp/${p1}/snp.$m.c$i$j.list --recode12 --out $DIR/svm+snp/${p1}/snp.$m.c$i$j

~/bin/PLINK_to_libsvm_multi.py $DIR/svm+snp/snp.class_num $DIR/svm+snp/${p1}/snp.$m.c$i$j.ped $DIR/svm+snp/${p1}/snp.$m.c$i$j $m

~/bin/easy_svm.py svm+snp/${p1}/snp.$m.c$i$j.train svm+snp/${p1}/snp.$m.c$i$j.test
