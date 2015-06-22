[Certified Runs](https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/)

[DAS](https://cmsweb.cern.ch/das/)

### Setup
Create working area with latest certified runs via:
``` shell
       source createJob.sh
```
which will create a directory according to the date. 
In the directory, there will be:
```
lxplusbatchscript.sh
```
to allow submission of jobs to the batch system. 

The main config will be copied to this directory and for time being the following contents will need to be updated:
-fileNames
-lumisToProcess (downloaded JSON)
-MINIAODoutput (to match that in the batch script)
-Global Tag (GT will remain unless stated otherwise)

To submit the batch script:
``` shell
bsub -R "pool>20000" -q 1nd -J job7 < lxplusbatchscript.sh
```