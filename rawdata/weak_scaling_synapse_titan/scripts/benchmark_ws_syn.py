#!/usr/bin/env python

__copyright__ = 'Copyright 2013-2014, http://radical.rutgers.edu'
__license__   = 'MIT'

import os
import sys
import time

import radical.pilot as rp
import radical.utils as ru

dh = ru.DebugHelper()

# ------------------------------------------------------------------------------
#
# READ the RADICAL-Pilot documentation: http://radicalpilot.readthedocs.org/
#
# ------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#
if __name__ == '__main__':

    sid    =     sys.argv[1]
    ucount = int(sys.argv[2])
    usize  = int(sys.argv[3])
    psize  = int(sys.argv[4])
    ptime  = int(sys.argv[5])

    print "sid     : %s" % sid
    print "ucount  : %s" % ucount
    print "usize   : %s" % usize 
    print "psize   : %s" % psize 
    print "ptime   : %s" % ptime 
    print

    session = rp.Session(uid=sid)
    print "session : %s" % session.uid

    try:
        pd_init = {'resource'      : 'ornl.titan_orte',
                   'runtime'       : ptime,
                   'exit_on_error' : True,
                   'project'       : 'BIP149',
                   'queue'         : 'batch',
                   'access_schema' : 'local',
                   'cores'         : psize + 16 * 3
                  }
        pdesc = rp.ComputePilotDescription(pd_init)
        pmgr  = rp.PilotManager(session=session)
        pilot = pmgr.submit_pilots(pdesc)
        umgr  = rp.UnitManager(session=session)
        umgr.add_pilots(pilot)
        cuds  = list()
        for i in range(0, ucount):
            cud = rp.ComputeUnitDescription()
            cud.executable = 'radical-synapse-sample'
            cud.arguments  = '-f 40000000000 -s 18'.split()
            cud.cores      = usize
            cud.mpi        = True
            cuds.append(cud)
        umgr.submit_units(cuds)
        umgr.wait_units()

    finally:
        session.close(download=True)


#-------------------------------------------------------------------------------

