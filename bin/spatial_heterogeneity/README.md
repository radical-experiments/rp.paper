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

| run ID | # CU | # Node | # cores | duration ABC | size ABC | Ratio A:B:C |
|--------|------|--------|---------|--------------|----------|-------------|
| 1      | 512  | 1\*    | 56      | 5-10s        | 1-8c     | 1:1:1       |
| 2      | 1024 | 1\*    | 56      | 5-10s        | 1-8c     | 1:1:1       |
| 3      | 2048 | 1\*    | 56      | 5-10s        | 1-8c     | 1:1:1       |
| 4      | 4096 | 1\*    | 56      | 5-10s        | 1-8c     | 1:1:1       |
| 5      | 8192 | 1\*    | 56      | 5-10s        | 1-8c     | 1:1:1       |
| 6      | 8192 | 2\*\*  | 112     | 5-10s        | 1-8c     | 1:1:1       |
| 7      | 8192 | 4      | 224     | 5-10s        | 1-8c     | 1:1:1       |
| 8      | 8192 | 8      | 448     | 5-10s        | 1-8c     | 1:1:1       |
| 9      | 8192 | 16     | 896     | 5-10s        | 1-8c     | 1:1:1       |
| 10     | 8192 | 32     | 1792    | 5-10s        | 1-8c     | 1:1:1       |
| 11     | 8192 | 64     | 3584    | 5-10s        | 1-8c     | 1:1:1       |
| 12     | 8192 | 128    | 7168    | 5-10s        | 1-8c     | 1:1:1       |

* \* Due to an error in SAGA configuration, these sessions run on 4 nodes but
  RP thought it had 1 node.
* \*\* Broken by https://github.com/radical-cybertools/radical.pilot/pull/2032

| run ID | Session ID                                                      |
|--------|-----------------------------------------------------------------|
| 1      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018313.0009 |
| 2      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018315.0000 |
| 3      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018315.0001 |
| 4      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018315.0002 |
| 5      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018315.0003 |
| 6      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018316.0002 |
| 7      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018317.0002 |
| 8      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018319.0002 |
| 9      | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018320.0000 |
| 10     | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018320.0001 |
| 11     | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018320.0002 |
| 12     | rp.session.login2.frontera.tacc.utexas.edu.mturilli.018320.0003 |











