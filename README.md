Preprocessing step

1) Create a directory for each set of training/testing compositions. For example,

for i in $(seq 1 1 10);
do
	mkdir r$i;
done

2) Make sure each list of training and testing is placed in the corresponding directory

3) Copy all binaries and scripts in your local bin directory

KNN/SNP method

1) train_knn+snp.1.sh을 다음 매개변수로 실행시킵니다. 

for i in $(seq 1 1 10);
do
	qsub ~/bin/train_knn+snp.1.sh r$i lqt+conA.$i.train.list /compgen5/shared/dataset/LQTS/diLQTS.qc.inf
done

2) 위의 작업이 오류 없이 끝난 것을 확인한 뒤에는 train_knn+snp.2.sh을 다음과 같이 실행시킵니다. 

for i in $(seq 1 1 10);
do
	for j in 5 10 15 20 25;
	do
		qsub ~/bin/train_knn+snp.2.sh r$i lqt+conA.$i.train.list $j;
	done
done

3) 그 뒤에는 KNN을 실행시켜서 training 결과를 확인합니다. 

for i in $(seq 1 1 10);
do
	for j in 5 10 15 20 25;
	do
		for k in $(seq 1 1 160); 
		do
			cat r$i/knn+snp/f$j/snp.$k.jsd.tmp >> r$i/knn+snp/f$j/snp.jsd.tmp; 
		done
		
		for k in 1 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40; 
		do
			a=`(~/bin/get_accuracy_k.py r$i/lqt+conA.$i.train.list r$i/knn+snp/f$j/snp.jsd.tmp  LQTS $k)`;
			echo $i $j $k $a >> r$i/knn+snp.train.result;	 
		done
	done
	sort -k 9 -g -r r$i/knn+snp.train.result | head -n 1 >> knn+snp.train.result;
done

4) 최적 파라미터를 testing에 적용합니다.

~/bin/test_knn+snp.0.sh knn+snp.train.result

5) 위의 작업이 끝나면 다음을 실행시켜서 최종 결과를 얻어냅니다.

while read f1 f2 f3 f4 f5 f6 f7 f8 f9;
do
	~/bin/get_accuracy_one_k.py r$f1/lqt+conA.$f1.train.list r$f1/knn+snp/f$f2/test_snp.1.jsd.tmp $f3 LQTS;
done < knn+snp.train.result

KNN/SNP-S method

1) train_knn+snps.1.sh를 실행시킵니다. KNN/SNP-S의 주요 변수중 하나인 SNP-S의 길이를 다르게 하여 data를 preprocessing하는 과정입니다.

for i in $(seq 1 1 10); do for j in 2 4 6 8; do qsub ~/bin/train_knn+snps.1.sh r$i lqt+conA.$i.train.list $j; done done

2) 위의 결과가 제대로 나온것을 확인한 뒤에는 길이를 다르게 하여 만든 SNP-S profile에 필터링 퍼센트를 다르게 적용하여 분석을 위한 최종 프로파일을 만들어 냅니다.

for i in $(seq 1 1 10); do for j in 2 4 6 8; do for k in 5 10 15 20 25; do qsub ~/bin/train_knn+snps.2.sh r$i lqt+conA.$i.train.list $j $k; done done

3) 최종 프로파일을 JSD matrix로 변환시킵니다.

for i in $(seq 1 1 10); do for j in 2 4 6 8; do for k in 5 10 15 20 25; do ~/bin/train_knn+snps.3.sh r$i lqt+conA.$i.train.list $j $k; done done

4) 변환된 JSD matrix을 하나의 파일로 통합합니다. 

for i in $(seq 1 1 10); do for j in 2 4 6 8; do for k in 5 10 15 20 25; do for m in $(seq 1 1 160); do cat r$i/knn+snps/l$j/f$k/snps.$m.jsd.tmp >> r$i/knn+snps/l$j/f$k/snps.jsd.tmp; done done done done

5) training결과를 확인합니다. 

for i in $(seq 1 1 10); do for j in 2 4 6 8; do for k in 5 10 15 20 25; do for m in 1 10 20 40 60 80; do a=`(~/bin/get_accuracy_k.py r$i/lqt+conA.$i.train.list r$i/knn+snps/l$j/f$k/snps.jsd.tmp $m LQTS)`; echo $i $j $k $m $a >> r$i/knn+snps.train.result; done done done done

6) 최적 training파라미터를 저장합니다.

for i in $(seq 1 1 10); do sort -k 10 -g -r r$i/knn+snps.train.result | head -n 1 >> knn+snps.train.result; done

7) 최적 training파라미터로 모델을 새로운 샘플에 테스트하는 첫번째 과정입니다. 

~/bin/test_knn+snps.0.sh knn+snps.train.result

8) 두번째 과정으로 새로운 샘플 하나를 포함하여 다시 JSD matrix를 구성합니다. 

while read f1 f2 f3 f4 f5 f6 f7 f8 f9 f10
do
        ~/bin/test_knn+snps.2.sh r$f1 lqt+conA.$f1.test.list $f2 $f3
done < knn+snps.train.result

9) 마지막으로 KNN을 적용하여 testing결과를 도출합니다.

while read f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 do a=`(~/bin/get_accuracy_one_k.py r$f1/lqt+conA.$f1.train.list r$f1/lqt+conA.$f1.test.list r$f1/knn+snps/l$f2/f$f3/test_snps LQTS $f4)`; echo $f1 $f2 $f3 $f4 $a done < knn+snps.train.result

SVM/SNP method

1) train_svm+snp.1.sh을 다음 매개변수로 실행시킵니다. 

for i in $(seq 1 1 10); do qsub ~/bin/train_svm+snp.1.sh r$i lqt+conA.$i.train.list /compgen5/shared/dataset/LQTS/diLQTS.qc.inf LQTS

분석을 하기전에 data preprocessing하기 위한 스크립트입니다.

2) 위의 작업이 오류 없이 끝난 것을 확인한 뒤에는 train_svm+snp.2.sh을 다음과 같이 실행시킵니다. 

for i in $(seq 1 1 10); do for j in $(seq 1 1 160); do for k in 10 50 100 500 1000; do qsub ~/bin/train_svm+snp.2.sh r$i lqt+conA.$i.train.list LQTS $j $k; done done

SVM으로 training하는 과정입니다. 

3) 그 뒤에는 training 결과를 확인합니다. 

for i in $(seq 1 1 10); do for j in 10 50 100 500 1000; do a=`(~/bin/get_accuracy_svm.py r$i/svm+snp/$j/snp 160)`; echo $i $j $a >> r$i/svm+snp.train.result; done done

4) training결과중에 최적을 저장합니다. 

for i in $(seq 1 1 10); do sort -k 8 -g -r r$i/svm+snp.train.result | head -n 1 >> svm+snp.train.result; done

5) 최적 파라미터를 testing에 적용합니다.

~/bin/test_svm+snp.0.sh svm+snp.train.result

6) 위의 작업이 끝나면 다음을 실행시켜서 최종 결과를 얻어냅니다.

while read f1 f2 f3 f4 f5 f6 f7 f8 do a=`(~/bin/get_accuracy_svm_test.py r$f1/svm+snp/$f2/test_snp.ped r$f1/svm+snp/$f2/test_snp.test r$f1/svm+snp/$f2/test_snp.train.predict LQTS)`; echo $f1 $f2 $a; done < svm+snp.train.result

SVM/SNP-S method

1) data preprocessing 과정을 진행합니다.

for i in $(seq 1 1 10); do for j in 2 4 6 8; do qsub ~/bin/train_svm+snps.1.sh r$i lqt+conA.$i.train.list /compgen5/shared/dataset/LQTS/diLQTS.qc.inf LQTS $j; done done

2) association test를 통해 feature selection과정을 진행합니다.

for i in $(seq 1 1 10); do for j in 2 4 6 8; do for k in $(seq 1 1 160); do qsub ~/bin/train_svm+snps.2.sh r$i lqt+conA.$i.train.list LQTS $j $k; done done done

이 작업은 DISK I/O 로드가 다른 작업에 비해 높습니다. 위에서처럼 하나씩 큐에 집어넣을 수도 있지만 로드를 줄이기 위해 몇개의 작업들을 batch로 묶어서 실행시키는 것도 권장하고 싶습니다. 

3) 선택된 SNP-S로 각 개인에 대한 프로파일을 만듭니다. 

for i in $(seq 1 1 10); do for j in 2 4 6 8; do for k in 10 50 100 500 1000; do for m in $(seq 1 1 160); do qsub ~/bin/train_svm+snps.3.h r$i lqt+conA.$i.train.list $j $k $m; done done done done

4) 프로파일로 SVM을 실행시킵니다. 

for i in $(seq 1 1 10); do for j in 2 4 6 8; do for k in 10 50 100 500 1000; do for m in $(seq 1 1 160); do qsub ~/bin/train_svm+snps.4.sh r$i LQTS $j $k $m; done done done done

5) training결과를 확인합니다.

for i in $(seq 1 1 10); do for j in 2 4 6 8; do for k in 10 50 100 500 1000; do a=`(~/bin/get_accuracy_svm.py r$i/svm+snps/l$j/$k/snps 160)`; echo $i $j $k $a >> r$i/svm+snps.train.result; done done

6) 최적 결과를 저장합니다.

for i in $(seq 1 1 10); do sort -k 6 -g -r r$i/svm+snps.train.result | head -n 1 >> svm+snps.train.result; done

7) 최적 파라미터로 새로운 샘플에 대한 분석을 위한 data preprocessing을 진행합니다. 

~/bin/test_svm+snps.0.sh svm+snps.train.result

8) 새로운 샘플에 대해 SVM으로 예측을 시도합니다. 

for i in $(seq 1 1 10); do for j in 2 4 6 8; do for k in 10 50 100 500 1000; do qsub ~/bin/test_svm+snps.2.sh r$i lqt+conA.$i.train.list lqt+conA.$i.test.list LQTS $j $k; done done done

9) 최종 결과를 얻어냅니다. 

while read f1 f2 f3 f4 f5 f6 do a=`(~/bin/get_accuracy_svm_test.py r$f1/lqt+conA.$f1.test.list r$f1/svm+snps/l$f2/$f3/test_snps.libsvm r$f1/svm+snps/l$f2/$f3/test_snps.libsvm.predict LQTS)`; echo $f1 $f2 $f3 $a; done < svm+snps.train.result
