#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y
#$ -V

DIR=$1
LIST=$2
DATASET=$3
SIZE=`(wc -l $DIR/$LIST | gawk '{print $1}')`
p1=$4
i=$5
j=$6

gawk '{ print $1 " " $1}' $DIR/$LIST > $DIR/$LIST.plink
~/bin/plink --noweb --file $DATASET.code --keep $DIR/$LIST.plink --transpose --recode --out $DIR/svm+snp/test_snp

~/bin/make_svm_snp_test_tfam_multi.py $DIR/svm+snp/snp.class_num $DIR/svm+snp/snp.tfam $DIR/svm+snp/snp.c$i$j.tfam $i $j
~/bin/plink --noweb --tped $DIR/svm+snp/snp.tped --tfam $DIR/svm+snp/snp.c$i$j.tfam --assoc --adjust --out $DIR/svm+snp/snp.c$i$j

####sed '1d' $DIR/svm+snp/snp.assoc.adjusted | gawk -v v=$p2 '{ if ($3 < v) print $2}' > $DIR/svm+snp/${p1}/snp.list
sed '1d' $DIR/svm+snp/snp.c$i$j.assoc.adjusted | sort -k 3 -g | head -n $p1 | gawk '{print $2}' > $DIR/svm+snp/${p1}/test_snp.c$i$j.list

~/bin/plink --noweb --tfile $DIR/svm+snp/test_snp --extract $DIR/svm+snp/${p1}/test_snp.c$i$j.list --recode --out $DIR/svm+snp/${p1}/test_snp.c$i$j
~/bin/plink --noweb --tfile $DIR/svm+snp/snp --extract $DIR/svm+snp/${p1}/test_snp.c$i$j.list --recode --out $DIR/svm+snp/${p1}/snp.c$i$j

~/bin/PLINK_to_libsvm2_multi.py $DIR/svm+snp/snp.class_num $DIR/svm+snp/${p1}/test_snp.c$i$j.ped $DIR/svm+snp/${p1}/test_snp.c$i$j.test
~/bin/PLINK_to_libsvm2_multi.py $DIR/svm+snp/snp.class_num $DIR/svm+snp/${p1}/snp.c$i$j.ped $DIR/svm+snp/${p1}/test_snp.c$i$j.train

~/bin/easy_svm.py $DIR/svm+snp/${p1}/test_snp.c$i$j.train $DIR/svm+snp/${p1}/test_snp.c$i$j.test
