#!/usr/bin/python

# for d in */
# do 
#   cat $d/pilot.0000/*log \
#   | grep -e '^2017-12' \
#   | sort -n \
#   | sed -n '1p;$p' \
#   | cut -f 1,2 -d ' ' \
#   > $(basename $d).out.log
#   get_tdiff $(basename $d).out.log
# done

import os
import sys
import datetime

t_format = '%Y-%m-%d %H:%M:%S,%f'

for arg in sys.argv[1:]:
    with open(arg, 'r') as fin:
        line_1, line_2 = fin.readlines()
    
    tstring_1 =  ':'.join(line_1.split(':')[0:3])
    tstring_2 =  ':'.join(line_2.split(':')[0:3])
    tstamp_1  = datetime.datetime.strptime(tstring_1, t_format)
    tstamp_2  = datetime.datetime.strptime(tstring_2, t_format)
    
    print '%30s %10.1f' % (arg, (tstamp_2-tstamp_1).total_seconds())
    
