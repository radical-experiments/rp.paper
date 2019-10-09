#!/usr/bin/env python

import os
from random import randint, choice
import radical.pilot as rp

# ------------------------------------------------------------------------------
#
if __name__ == '__main__':

    session = rp.Session()

    try:
        pmgr    = rp.PilotManager(session=session)
        pd_init = {'resource'      : 'xsede.stampede2_srun',
                   'queue'         : 'normal',
                   'project'       : 'TG-MCB090174',
                   'queue'         : 'development',
                   'access_schema' : 'gsissh',
                   'runtime'       : 60,
                   'exit_on_error' : True,
                   'cores'         : 68
                  }
        pdesc = rp.ComputePilotDescription(pd_init)
        pilot = pmgr.submit_pilots(pdesc)
        umgr  = rp.UnitManager(session=session)
        umgr.add_pilots(pilot)

        cuds = list()
        for i in range(512):
            cud = rp.ComputeUnitDescription()
            cud.executable       = '/home1/02855/mturilli/bin/hello_rp.sh'
            cud.arguments        = [randint(5, 10) * 1]
            cud.cpu_threads      =  randint(1, 8)
            cud.cpu_processes    =  randint(1, 8) # * 10
            # cud.gpu_processes    =  choice([0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4])
            # cud.gpu_process_type = rp.POSIX  # rp.MPI
            cud.cpu_process_type = rp.MPI      # rp.POSIX  # rp.MPI
            cud.cpu_thread_type  = rp.POSIX
            cuds.append(cud)

        umgr.submit_units(cuds)
        umgr.wait_units()
        session.close(download=True)

    except:
        session.close(download=False)
        raise

