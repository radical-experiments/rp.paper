import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import radical.utils as ru
import radical.pilot as rp
import radical.analytics as ra
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

from IPython.core.display import display, HTML

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 50)


# ----------------------------------------------------------------------------
# Global configurations
# ----------------------------------------------------------------------------

# Expand the notebook to the width of the browser
display(HTML("<style>.container { width:100% !important; }</style>"))

# Matplotlib style
plt.style.use('seaborn-ticks')

# Use LaTeX and its body font for the diagrams' text.
mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.unicode'] = True
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif']  = ['Nimbus Roman Becker No9L']

# Font sizes
SIZE = 24
plt.rc('font', size=SIZE)  # controls default text sizes
plt.rc('axes', titlesize=SIZE)  # fontsize of the axes title
plt.rc('axes', labelsize=SIZE)  # fontsize of the x any y labels
plt.rc('xtick', labelsize=SIZE)  # fontsize of the tick labels
plt.rc('ytick', labelsize=SIZE)  # fontsize of the tick labels
plt.rc('legend', fontsize=SIZE-2)  # legend fontsize
plt.rc('figure', titlesize=SIZE)  # # size of the figure title

# Use thinner lines for axes to avoid distractions.
mpl.rcParams['axes.linewidth']    = 0.75
mpl.rcParams['xtick.major.width'] = 0.75
mpl.rcParams['xtick.minor.width'] = 0.75
mpl.rcParams['ytick.major.width'] = 0.75
mpl.rcParams['ytick.minor.width'] = 0.75
mpl.rcParams['lines.linewidth'] = 2


# Do not use a box for the legend to avoid distractions.
mpl.rcParams['legend.frameon'] = False

# Restore part of matplotlib 1.5 behavior
mpl.rcParams['patch.force_edgecolor'] = True
mpl.rcParams['errorbar.capsize'] = 3

# Use coordinated colors. These are the "Tableau 20" colors as
# RGB. Each pair is strong/light. For a theory of color
tableau20 = [(31 , 119, 180), (174, 199, 232), # blue        [ 0,1 ]
             (255, 127, 14 ), (255, 187, 120), # orange      [ 2,3 ]
             (44 , 160, 44 ), (152, 223, 138), # green       [ 4,5 ]
             (214, 39 , 40 ), (255, 152, 150), # red         [ 6,7 ]
             (148, 103, 189), (197, 176, 213), # purple      [ 8,9 ]
             (140, 86 , 75 ), (196, 156, 148), # brown       [10,11]
             (227, 119, 194), (247, 182, 210), # pink        [12,13]
             (188, 189, 34 ), (219, 219, 141), # yellow      [14,15]
             (23 , 190, 207), (158, 218, 229), # cyan        [16,17]
             (65 , 68 , 81 ), (96 , 99 , 106), # gray        [18,19]
             (127, 127, 127), (143, 135, 130), # gray        [20,21]
             (165, 172, 175), (199, 199, 199), # gray        [22,23]
             (207, 207, 207)]                   # gray        [24]

# Scale the RGB values to the [0, 1] range, which is the format
# matplotlib accepts.
for i in range(len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r / 255., g / 255., b / 255.)

# ----------------------------------------------------------------------------
# RCT Configurations
# ----------------------------------------------------------------------------

# List of events of RP
event_list = [
    # {ru.STATE: 'NEW'                          , ru.EVENT: 'state'           },
    # {ru.STATE: 'UMGR_SCHEDULING_PENDING'      , ru.EVENT: 'state'           },
    # {ru.STATE: 'UMGR_SCHEDULING'              , ru.EVENT: 'state'           },
    # {ru.STATE: 'UMGR_STAGING_INPUT_PENDING'   , ru.EVENT: 'state'           },
    # {ru.STATE: 'UMGR_STAGING_INPUT'           , ru.EVENT: 'state'           },
    # {ru.STATE: 'AGENT_STAGING_INPUT_PENDING'  , ru.EVENT: 'state'           },
    # {ru.COMP : 'agent_0'                      , ru.EVENT: 'get'             },
    # {ru.STATE: 'AGENT_STAGING_INPUT'          , ru.EVENT: 'state'           },
    # {ru.STATE: 'AGENT_SCHEDULING_PENDING'     , ru.EVENT: 'state'           },
      {ru.STATE: None                           , ru.EVENT: 'schedule_try'    }, # Scheduling start
    # {ru.STATE: 'AGENT_SCHEDULING'             , ru.EVENT: 'state'           },
      {ru.STATE: None                           , ru.EVENT: 'schedule_ok'     }, # Scheduling stop
      {ru.STATE: 'AGENT_EXECUTING_PENDING'      , ru.EVENT: 'state'           }, # Queuing Execution start
      {ru.STATE: 'AGENT_EXECUTING'              , ru.EVENT: 'state'           }, # Queuing Execution stop  | Preparing Execution start
      {ru.STATE: None                           , ru.EVENT: 'exec_mkdir'      }, # Agent Executing Component
      {ru.STATE: None                           , ru.EVENT: 'exec_mkdir_done' }, # Agent Executing Component
      {ru.STATE: None                           , ru.EVENT: 'exec_start'      }, # Agent Executing Component
      {ru.STATE: None                           , ru.EVENT: 'exec_ok'         }, # System OS
      {ru.STATE: None                           , ru.EVENT: 'cu_start'        }, # System OS
      {ru.STATE: None                           , ru.EVENT: 'cu_cd_done'      }, # CU script
      {ru.STATE: None                           , ru.EVENT: 'cu_pre_start'    }, # CU script
      {ru.STATE: None                           , ru.EVENT: 'cu_pre_stop'     }, # CU script
      {ru.STATE: None                           , ru.EVENT: 'cu_exec_start'   }, # CU script [orterun spawner]
      {ru.STATE: None                           , ru.EVENT: 'app_start'       }, # Synapse
      {ru.STATE: None                           , ru.EVENT: 'app_stop'        }, # Synapse, orterun [orterun spawner]
      {ru.STATE: None                           , ru.EVENT: 'cu_exec_stop'    }, # CU script
      {ru.STATE: None                           , ru.EVENT: 'cu_post_start'   }, # CU script
      {ru.STATE: None                           , ru.EVENT: 'cu_post_stop'    }, # CU script
      {ru.STATE: None                           , ru.EVENT: 'exec_stop'       }, # Agent Executing Component
      {ru.STATE: None                           , ru.EVENT: 'unschedule_start'}, # Agent Scheduling Component
      {ru.STATE: None                           , ru.EVENT: 'unschedule_stop' }, # Agent Scheduling Component    # {ru.STATE: 'AGENT_STAGING_OUTPUT_PENDING' , ru.EVENT: 'state'           },
    # {ru.STATE: 'UMGR_STAGING_OUTPUT_PENDING'  , ru.EVENT: 'state'           },
    # {ru.STATE: 'UMGR_STAGING_OUTPUT'          , ru.EVENT: 'state'           },
    # {ru.STATE: 'AGENT_STAGING_OUTPUT'         , ru.EVENT: 'state'           },
    # {ru.STATE: 'DONE'                         , ru.EVENT: 'state'           },
]

# Durations from events
event_durations = {
    'Scheduling'         : [{ru.STATE: None, ru.EVENT: 'schedule_try'}              , {ru.STATE: None, ru.EVENT: 'schedule_ok'}],
    'Queuing Execution'  : [{ru.STATE: 'AGENT_EXECUTING_PENDING', ru.EVENT: 'state'}, {ru.STATE: 'AGENT_EXECUTING', ru.EVENT: 'state'}],
    'Preparing Execution': [{ru.STATE: 'AGENT_EXECUTING', ru.EVENT: 'state'}        , {ru.STATE: None, ru.EVENT: 'exec_start'}],
    'Making directory'   : [{ru.STATE: None, ru.EVENT: 'exec_mkdir'}                , {ru.STATE: None, ru.EVENT: 'exec_mkdir_done'}],
    'Spawning'           : [{ru.STATE: None, ru.EVENT: 'exec_start'}                , {ru.STATE: None, ru.EVENT: 'exec_ok'}],
    'Executing'          : [{ru.STATE: None, ru.EVENT: 'exec_ok'}                   , {ru.STATE: None, ru.EVENT: 'exec_stop'}],
    'Unscheduling'       : [{ru.STATE: None, ru.EVENT: 'unschedule_start'}          , {ru.STATE: None, ru.EVENT: 'unschedule_stop'}]
}

# ----------------------------------------------------------------------------
# Utils
# ----------------------------------------------------------------------------

# Return a single plot without right and top axes, spanning one column text.
def fig_setup():
    fig = plt.figure(figsize=(13,7))
    ax = fig.add_subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    return fig, ax


# Return a single plot without right and top axes, spanning two columns text.
def fig_hdouble_setup():
    fig = plt.figure(figsize=(26,7))
    ax = fig.add_subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    return fig, ax


# load ra session objects.
def load_sessions(sdir, sessions, snunits):
    # number of units in the sessions
    # snunits = sorted(sessions.nunit.unique().tolist())

    # load the RA session objects
    sras = {}
    for snunit in snunits:
        sras[snunit] = []
        s = sessions[(sessions.nunit == snunit)]
        for sid in s.sid.tolist():
            exp = s.loc[sid]['experiment']
            src = '%s/%s/%s' % (sdir, exp, sid)
            sras[snunit].append(ra.Session(src, 'radical.pilot'))

    return sras


# Collect timestamps of all the event specified in event_list for every unit
def get_df_unit_events(session):
    s = session
    s.filter(etype='unit', inplace=True)
    data = dict()
    for thing in s.get():

        tstamps = dict()
        for event in event_list:
            eid = event[1]
            if eid == 'state':
                eid = event[5]
            times = thing.timestamps(event=event)
            if times:
                tstamps[eid] = times[0]
            else:
                tstamps[eid] = None

        data[thing.uid] = tstamps

    # We sort the entities by the timestamp of the first event
    # Also, for all timestamps, we move the baseline to the first
    # timestamp in the list
    df = pd.DataFrame.from_dict(data)
    df = df.sort_values(by=list(df.columns))
    df = df.transpose()
    df = df.reset_index()

    # Rename events to make them intellegible
    df.rename_axis(                                           # Components
        {'index'                   :'uid'                   ,
         'schedule_try'            :'Scheduler Schedule'    , # Agent Scheduling Component
         'schedule_ok'             :'Scheduler Scheduled'   , # Agent Scheduling Component
         'AGENT_EXECUTING_PENDING' :'Scheduler Queued'      , # Agent Scheduling Component
         'AGENT_EXECUTING'         :'Executor Execute'      , # Agent Executing Component
         'exec_mkdir'              :'Executor Make Dir'     , # Agent Executing Component
         'exec_mkdir_done'         :'Executor Made Dir'     , # Agent Executing Component
         'exec_start'              :'Executor Spawn'        , # Agent Executing Component
         'exec_ok'                 :'OS Accepted Spawn'     , # System OS
         'cu_start'                :'OS Spawn'              , # System OS
         'cu_cd_done'              :'CU Changed Dir'        , # CU script
         'cu_pre_start'            :'CU Pre-execute'        , # CU script
         'cu_pre_stop'             :'CU Pre-executed'       , # CU script
         'cu_exec_start'           :'CU Spawn'              , # CU script [orterun spawner]
         'app_start'               :'Exe Execute'           , # Synapse
         'app_stop'                :'Exe Executed'          , # Synapse [orterun spawner]
         'cu_exec_stop'            :'CU Executed'           , # CU script
         'cu_post_start'           :'CU Post-execute'       , # CU script
         'cu_post_stop'            :'CU Post-executed'      , # CU script
         'exec_stop'               :'Executor Executed'     , # Agent Executing Component
         'unschedule_start'        :'Scheduler Unschedule'  , # Agent Scheduling Component
         'unschedule_stop'         :'Scheduler Unscheduled'}, # Agent Scheduling Component
        axis='columns', inplace=True)

    # Durations sub-component level
    df['Scheduler Scheduling']       = df['Scheduler Scheduled']   - df['Scheduler Schedule']
    df['Scheduler Queuing Executor'] = df['Executor Execute']      - df['Scheduler Queued']
    df['Executor Pre-executing']     = df['Executor Spawn']        - df['Executor Execute']
    df['Executor Making Dir']        = df['Executor Made Dir']     - df['Executor Make Dir']
    df['Executor Spawning']          = df['OS Accepted Spawn']     - df['Executor Spawn']
    df['OS Spawning']                = df['OS Spawn']              - df['OS Accepted Spawn']
    df['CU Changing Dir']            = df['CU Changed Dir']        - df['OS Spawn']
    df['CU Pre-executing']           = df['CU Pre-executed']       - df['CU Pre-execute']
    df['CU Spawning']                = df['Exe Execute']           - df['CU Spawn']
    df['Exe Executing']              = df['Exe Executed']          - df['Exe Execute']
    df['Scheduler Unscheduling']     = df['Scheduler Unscheduled'] - df['Scheduler Unschedule']

    # Durations component level

    # Durations chunk level

    return df
