#!/bin/bash

DIR=$1
i=$2
CASE_LABEL=$3

sort -k 1 $DIR/knn+snp.test.result.list > $DIR/knn+snp.tmp
sort -k 1 $DIR/knn+snps.test.result.list > $DIR/knn+snps.tmp
sort -k 1 $DIR/svm+snp.test.result.list > $DIR/svm+snp.tmp
sort -k 1 $DIR/svm+snps.test.result.list > $DIR/svm+snps.tmp

paste $DIR/knn+snp.tmp $DIR/knn+snps.tmp $DIR/svm+snp.tmp $DIR/svm+snps.tmp | gawk '{print $1 "\t" $2 "\t" $4 "\t" $6 "\t" $8}' > $DIR/total.result.list
./bayes_inference.py $DIR/total.result.list $i $CASE_LABEL
