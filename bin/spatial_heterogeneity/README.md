# Experiment Runs

* Resource: Frontera at TACC.
* Experiment: Characterizing RP performance with spatially/type/time heterogeneous tasks.
* Task types: 
  - A: single thread;
  - B: multiple threads;
  - C: MPI.
* Task sizes: 1-8 threads (POSIX); 1-8 processes (MPI).
* Task times: 5-10 seconds.

## Raw Data Compression

GitHub does not allow for files > 100MB. 

* On Frontera's headnode, archive, compress, split, commit to github raw data with:

  ```
  tar -cjf - <session-ID>/* | split -b 40M - "<session-ID>.tar.bz2.part."
  git add <session-ID>.tar.bz2.part.*
  git commit -m '<message>'
  git pull
  git push
  ```

* On the machine where to analyze the data, get, join, unarchive and uncpress the raw data with:
  ```
  git pull
  cat <session-ID>.tar.bz2.part.* > <session-ID>.tar.bz2
  tar xfj <session-ID>.tar.bz2
  ```

## Strong Scaling

| run ID | # CU | # Node    | # cores | Runtime | Queue       | duration ABC | size ABC | Ratio A:B:C |
|--------|------|-----------|---------|---------|-------------|--------------|----------|-------------|
| 22     | 8192 | 8         | 448     | 2h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 23     | 8192 | 8         | 448     | 2h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 14     | 8192 | 8         | 448     | 2h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 15     | 8192 | 8         | 448     | 2h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 16     | 8192 | 16        | 896     | 1h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 17     | 8192 | 16        | 896     | 1h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 18     | 8192 | 16        | 896     | 1h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 10     | 8192 | 32        | 1792    | 1h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 19     | 8192 | 32        | 1792    | 1h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 20     | 8192 | 32        | 1792    | 1h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 21     | 8192 | 32        | 1792    | 1h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 11     | 8192 | 64        | 3584    | 1h      | flex        | 5-10s        | 1-8c     | 1:1:1       |
| 24     | 8192 | 64        | 3584    | 1h      | flex        | 5-10s        | 1-8c     | 1:1:1       |
| 25     | 8192 | 64        | 3584    | 1h      | flex        | 5-10s        | 1-8c     | 1:1:1       |
| 26     | 8192 | 64        | 3584    | 1h      | flex        | 5-10s        | 1-8c     | 1:1:1       |
| 13     | 8192 | 128       | 7168    | 1h      | flex        | 5-10s        | 1-8c     | 1:1:1       |
| 27     | 8192 | 128       | 7168    | 1h      | flex        | 5-10s        | 1-8c     | 1:1:1       |
| 28     | 8192 | 128       | 7168    | 1h      | flex        | 5-10s        | 1-8c     | 1:1:1       |
| 29     | 8192 | 128       | 7168    | 1h      | flex        | 5-10s        | 1-8c     | 1:1:1       |


| run ID | Session ID                                                      | # Failed units |
|--------|-----------------------------------------------------------------|----------------|
| 22     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018327.0009 |                |
| 23     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018327.0010 |                |
| 14     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018326.0002 |                |
| 15     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018326.0004 |                |
| 16     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018327.0000 |                |
| 17     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018327.0001 |                |
| 18     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018327.0002 |                |
| 10     | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018320.0001 | 0              |
| 19     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018327.0003 |                |
| 20     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018327.0007 |                |
| 21     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018327.0008 |                |
| 11     | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018320.0002 | 0              |
| 24     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018327.0011 |                |
| 25     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018327.0012 |                |
| 26     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018327.0013 |                |
| 13     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018325.0001 |                |
| 27     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018327.0014 |                |
| 28     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018327.0015 |                |
| 29     | rp.session.login3.frontera.tacc.utexas.edu.mturilli.018327.0016 |                |

### Broken

| run ID | # CU | # Node    | # cores | Runtime | Queue       | duration ABC | size ABC | Ratio A:B:C |
|--------|------|-----------|---------|---------|-------------|--------------|----------|-------------|
| 1      | 512  | 1\*       | 56      | 1h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 2      | 1024 | 1\*       | 56      | 1h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 3      | 2048 | 1\*       | 56      | 2h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 4      | 4096 | 1\*       | 56      | 3h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 5      | 8192 | 1\*       | 56      | 4h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 6      | 8192 | 2\*\*     | 112     | 4h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 7      | 8192 | 4\+       | 224     | 3h      | normal      | 5-10s        | 1-8c     | 1:1:1       |
| 8      | 8192 | 8\*\*\*   | 448     | 2h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 9      | 8192 | 16\*\*\*  | 896     | 1h      | development | 5-10s        | 1-8c     | 1:1:1       |
| 12     | 8192 | 128\*\*\* | 7168    | 1h      | flex        | 5-10s        | 1-8c     | 1:1:1       |

| run ID | Session ID                                                      | # Failed units |
|--------|-----------------------------------------------------------------|----------------|
| 1      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018313.0009 | NA             |
| 2      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018315.0000 | NA             |
| 3      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018315.0001 | NA             |
| 4      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018315.0002 | NA             |
| 5      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018315.0003 | NA             |
| 6      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018316.0002 | 945            |
| 7      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018317.0002 | 0              |
| 8      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018319.0002 | 1024           |
| 9      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018320.0000 | 1024           |
| 12     | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018320.0003 | 1024           |

* \* Due to an error in SAGA configuration, these sessions run on 4 nodes but
  RP thought it had 1 node.
* \*\* Broken by https://github.com/radical-cybertools/radical.pilot/pull/2032
* \*\*\* Broken due to an error with SAGA due to the number of threads used to
  create the unit sandboxes.
* \+ Missing `U_AGENT_QUEUING`, probably related to \*\*. 

## Strong Scaling

| run ID | # CU   | # Node    | # cores | Runtime | Queue  | duration ABC | size ABC | Ratio A:B:C |
|--------|--------|-----------|---------|---------|--------|--------------|----------|-------------|
| 1      | 8192   | 128       | 7168    | 1h      | flex   | 5-10s        | 1-8c     | 1:1:1       |
| 2      | 16384  | 256       | 14336   | 1h      | normal | 5-10s        | 1-8c     | 1:1:1       |
| 2      | 32768  | 512       | 28672   | 1h      | normal | 5-10s        | 1-8c     | 1:1:1       |
| 2      | 65536  | 1024      | 57344   | 1h      | large  | 5-10s        | 1-8c     | 1:1:1       |
| 2      | 131072 | 2048      | 114688  | 1h      | large  | 5-10s        | 1-8c     | 1:1:1       |
| 2      | 262144 | 4096      | 229376  | 1h      | large  | 5-10s        | 1-8c     | 1:1:1       |