#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -j y
#$ -V
## -l hostname=cg12
## -p 1024
## -l mem_free=2G

echo $*
$*
