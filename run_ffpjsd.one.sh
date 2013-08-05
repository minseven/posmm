#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y
## -p 1024

~/bin/ffpjsd -j --nrow $1 --ncol $2 -r $3 $4 > $5
