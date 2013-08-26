#!/bin/bash

ARG=$1
i_list=(1 2 3 4 5 6 7 8 9 10);
j_list=(2 4 6 8);
k_list=(10 20 40 80 120 180 200 240 280 320 400 480 500);

if [ $ARG == 'result' ];
then
	rm svm+snps.train.result
	for i in ${i_list[@]};
	do
		rm r$i/svm+snps.train.result
		for j in ${j_list[@]};
		do
			for k in ${k_list[@]};
			do
				#if [ -f r$i/svm+snps/l$j/$k/snps.libsvm.train.predict ];
				#then
				rm r$i/svm+snps/l$j/$k/snps.libsvm.train.predict
				#fi
				#if [ -f r$i/svm+snps/l$j/$k/snps.libsvm.test ];
        			#then
                		rm r$i/svm+snps/l$j/$k/snps.libsvm.test
        			#fi

				for m in $(seq 1 1 10);
				do
					cat r$i/svm+snps/l$j/$k/snps.libsvm.$m.test >> r$i/svm+snps/l$j/$k/snps.libsvm.test;
                			cat r$i/svm+snps/l$j/$k/snps.libsvm.$m.train.predict >> r$i/svm+snps/l$j/$k/snps.libsvm.train.predict;
					#~/bin/get_accuracy_svm2.py r$i/svm+snps/l$j/$k/snps.libsvm.$m >> r$i/svm+snps/l$j/$k/snps.train.result
				done
	
				a=`(~/bin/get_accuracy_svm2.py r$i/svm+snps/l$j/$k/snps.libsvm)`;
        			echo $i $j $k $a >> r$i/svm+snps.train.result;
			done
		done
		sort -k 8 -g -r r$i/svm+snps.train.result | head -n 1 >> svm+snps.train.result;
	done
fi
