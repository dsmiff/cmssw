[Certified Runs](https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/)

[DAS](https://cmsweb.cern.ch/das/)

### Setup
Create working area with latest certified runs via:
``` shell
source createJob.sh
```
which will create a directory according to the date. 
#To submit with CRAB3
After running createJob.sh, you can submit your jobs to CRAB3 using the template CRAB config that has been copied from the main directory.
The items to change are
```
config.Data.inputDataset
config.Data.lumiMask
```
where the JSON file passed should be the one downloaded in the jobs directory.
After making the necessary changes, please submit to crab with
```
crab submit
```


#To run on the batch
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