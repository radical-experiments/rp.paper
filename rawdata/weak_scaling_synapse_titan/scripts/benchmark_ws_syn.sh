#!/bin/bash

module load python
module load python_setuptools
module load python_virtualenv

export PATH=$HOME/install/bin:$PATH
export RADICAL_PILOT_DBURL=mongodb://radical:2r4d1c4l@mongodb-radical-benchmark.apps.ccs.ornl.gov:30008/htcbenchmark

source $HOME/radical/ve.synapse/bin/activate

# psize, ptime, usize, ucount
# parallel -j 2 -a benchmark_ws.tab --colsep '\t' 'echo "`which python` unum {3} usize {4} psize {7} ptime {9} `sleep 2`"'
parallel -j 4 -a benchmark_ws_syn.tab --colsep '\t' 'python benchmark_ws_syn.py {3} {4} {7} {9} > run_{3}_{4}_{7}_{9}.{1}.log'

