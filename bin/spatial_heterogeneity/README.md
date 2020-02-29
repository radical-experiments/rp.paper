# Experiment Runs

* Resource: Frontera at TACC.
* Experiment: Characterizing RP performance with spatially/type/time heterogeneous tasks.
* Task types: single/multiple threads; MPI.
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

| Session ID                                                      | # CU | # Node | Ratio A:B:C |
|-----------------------------------------------------------------|------|--------|-------------|
| rp.session.login2.frontera.tacc.utexas.edu.mturilli.018313.0009 | 512  | 1\*    | 1:1:1       |
| rp.session.login2.frontera.tacc.utexas.edu.mturilli.018315.0000 | 1024 | 1\*    | 1:1:1       |
| rp.session.login2.frontera.tacc.utexas.edu.mturilli.018315.0001 | 2048 | 1\*    | 1:1:1       |
| rp.session.login2.frontera.tacc.utexas.edu.mturilli.018315.0002 | 4096 | 1\*    | 1:1:1       |
| rp.session.login2.frontera.tacc.utexas.edu.mturilli.018315.0003 | 8192 | 1\*    | 1:1:1       |
| rp.session.login2.frontera.tacc.utexas.edu.mturilli.018316.0002 | 8192 | 2\*\*  | 1:1:1       |
| rp.session.login2.frontera.tacc.utexas.edu.mturilli.018317.0002 | 8192 | 4      | 1:1:1       |
| rp.session.login2.frontera.tacc.utexas.edu.mturilli.018319.0002 | 8192 | 8      | 1:1:1       |
| rp.session.login2.frontera.tacc.utexas.edu.mturilli.018320.0000 | 8192 | 16     | 1:1:1       |
| rp.session.login2.frontera.tacc.utexas.edu.mturilli.018320.0001 | 8192 | 32     | 1:1:1       |
| rp.session.login2.frontera.tacc.utexas.edu.mturilli.018320.0002 | 8192 | 64     | 1:1:1       |

* \* Due to an error in SAGA configuration, these sessions run on 4 nodes but
  RP thought it had 1 node.
* \*\* Broken by https://github.com/radical-cybertools/radical.pilot/pull/2032
