Please:
* upload only compressed sessions in tar.bz2 format
* add \<session_id\>/\<expID\> tag to README.md (see experiment ID/descriptions [here](https://github.com/radical-experiments/rp-paper-ipdps2018/wiki))
* add output of `radical-stack`

    * RP branch: experiment/ipdps2018
    * RS branch: experiment/ipdps2018
    * RU branch: experiment/ipdps2018
    * DBURL: ornl DTN: ???


### tests:
  
    * rp.session.titan-ext1.merzky1.017423.0022  1p * 2kcores    8ku * 8cores
    * rp.session.titan-ext1.merzky1.017423.0023  1p * 2kcores    4ku * 8cores
    * rp.session.titan-ext1.merzky1.017423.0028  1p * 2kcores   16ku * 8cores
    * rp.session.titan-ext1.merzky1.017424.0000  1p * 8kcores   32ku * 8cores


### weak scaling

    run_64_32_2048_60.log      rp.session.titan-ext1.merzky1.017431.0001
    run_128_32_4096_60.log     rp.session.titan-ext1.merzky1.017431.0004
    run_256_32_8192_60.log     rp.session.titan-ext1.merzky1.017431.0000
    run_512_32_16384_60.log    rp.session.titan-ext1.merzky1.017431.0005


