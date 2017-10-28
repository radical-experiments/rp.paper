#!/bin/bash

module load python
module load python_setuptools
module load python_virtualenv

export PATH=$HOME/install/bin:$PATH
export RADICAL_PILOT_DBURL=mongodb://radical:2r4d1c4l@mongodb-radical-benchmark.apps.ccs.ornl.gov:30008/htcbenchmark

source $HOME/radical/ve.synapse/bin/activate

ws_syn() {
    id=$1
    ucount=$2
    usize=$3
    psize=$4
    ptime=$5

    # we don't run commented out experiments
    echo {1} | grep "#" && return

    sid="ws_syn_titan_${ucount}_${usize}_${psize}_${ptime}_${id}"
    echo "start $sid"
    python benchmark_ws_syn.py "$sid" $ucount $usize $psize $ptime > $sid.log 2>&1
    echo "stop  $sid"

    
}
export -f ws_syn

# psize, ptime, usize, ucount
# parallel -j 2 -a benchmark_ws_syn.tab --colsep '\t' 'echo {1} | grep "#" > /dev/null || echo "`which python` unum {3} usize {4} psize {7} ptime {9} {1} `sleep 0.5`"'
# parallel -j 4 -a benchmark_ws_syn.tab --colsep '\t' 'echo {1} | grep "#" > /dev/null || python benchmark_ws_syn.py "ws_syn_titan_{3}_{4}_{7}_{9}.{1}." {3} {4} {7} {9} > ws_syn_titan_{3}_{4}_{7}_{9}.{1}.log'
  parallel -j 4 -a benchmark_ws_syn.tab --colsep '\t' 'ws_syn {1} {3} {4} {7} {9}'

