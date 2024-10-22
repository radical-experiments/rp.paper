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
    * rp.session.titan-ext2.itoman.017466.0002   1p * 1kcores    1ku * 1core (test synapse profile from Manuel)
    * rp.session.titan-ext2.itoman.017469.0003   1p * 256kcores 16ku * 32core (strong-scaling timeout due to Wallclock)


### weak scaling

    run_64_32_2048_60.log      rp.session.titan-ext1.merzky1.017431.0001
    run_128_32_4096_60.log     rp.session.titan-ext1.merzky1.017431.0004
    run_256_32_8192_60.log     rp.session.titan-ext1.merzky1.017431.0000
    run_512_32_16384_60.log    rp.session.titan-ext1.merzky1.017431.0005


### strong scaling

    * rp.session.titan-ext1.itoman.017501.0001   1p * 16kcores  16ku * 32cores
    * rp.session.titan-ext1.itoman.017503.0000   1p * 16kcores  16ku * 32cores
    * rp.session.titan-ext2.itoman.017467.0000   1p * 32kcores  16ku * 32cores
    * rp.session.titan-ext1.itoman.017492.0001   1p * 32kcores  16ku * 32cores
    * rp.session.titan-ext1.itoman.017473.0000   1p * 64kcores  16ku * 32cores
    * rp.session.titan-ext1.itoman.017491.0004   1p * 64kcores  16ku * 32cores


