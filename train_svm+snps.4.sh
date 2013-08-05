#!/bin/bash


#$ -S /bin/bash
#$ -cwd
#$ -j y
#$ -V

DIR=$1
CASE=$2
l=$3
p1=$4
i=$5

rm $DIR/svm+snps/l$l/${p1}/snps.$i.matrix.tmp
for name in $(cat $DIR/svm+snps/snps.$i.tfam | gawk '{print $1}');
do
	#b=`(grep '1 1' $DIR/svm+snps/l$l/${p1}/snps.$name.matrix.tmp | wc -l)`
	#if [ $b -eq 1 ];
	#then
	#	echo "1" > $DIR/svm+snps/l$l/${p1}/snps.$name.matrix.tmp
	#	echo "found"
	#fi
	a=`(gawk '{print NF}' $DIR/svm+snps/l$l/${p1}/snps.$name.$i.matrix.tmp)`
        if [ $a -eq 0 ];
        then
                echo "1" > $DIR/svm+snps/l$l/${p1}/snps.$name.$i.matrix.tmp
        fi
	cat $DIR/svm+snps/l$l/${p1}/snps.$name.$i.matrix.tmp >> $DIR/svm+snps/l$l/${p1}/snps.$i.matrix.tmp
done

~/bin/FIP_to_libsvm.py $DIR/svm+snps/snps.$i.tfam $DIR/svm+snps/l$l/${p1}/snps.$i.matrix.tmp $DIR/svm+snps/l$l/${p1}/snps.libsvm.$i $i $CASE
~/bin/easy_svm.py $DIR/svm+snps/l$l/${p1}/snps.libsvm.$i.train $DIR/svm+snps/l$l/${p1}/snps.libsvm.$i.test
