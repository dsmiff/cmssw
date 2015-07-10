[Certified Runs](https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/)

[DAS](https://cmsweb.cern.ch/das/)

NB: T0 waits 48h to process the data in the physics stream before AOD production can begin (once prompt calibrations are in place)

### Setup
Create working area with latest certified runs via:
``` shell
source createJob.sh
```
which will create a directory according to the date. 
#Privately produce miniAOD from AOD
After running createJob.sh, you can submit your jobs to CRAB3 using the template CRAB config that has been copied from the main directory.
The items to change are
```
config.Data.inputDataset
config.Data.lumiMask
```
where the JSON file passed should be the one downloaded in the jobs directory.
After making the necessary changes, please submit to crab with
```
crab submit CrabConfiguarition.py
```
#To manage contents of Storage Site (awaiting mirror directory structures)
```
./python/copyData.py -H <host> --dry-run 
```
where `<host>` is 'bristol', 'imperial' or 'cern'.
If left unfilled, scipt lists current hosts SE
This requires a valid GRID certificate:
```
voms-proxy-init --voms-cms
```
The `source` and `destination` of the transfer can be given via the arguments `--from-site` and `--to-site`.
The output of the script is a file containing the necessary `gfal-copy`:
```
fileList.sh
```
Should a user specifically desire to access their samples, pass the `--add_user` command.
A `dry-run` will list and execute the `gfal-ls` command.
##To list the directories of T2_UK_SGrid_Bristol
```
gfal-ls gsiftp://lcgse01.phy.bris.ac.uk/dpm/phy.bris.ac.uk/home/cms/store/
```
##To list the directories of T2_UK_London_IC
```
gfal-ls gsiftp://lcgse01.phy.bris.ac.uk/dpm/phy.bris.ac.uk/home/cms/store/
```
##To list the directories of T2_CERN_CH
```
gfal-ls srm://srm-eoscms.cern.ch//eos/cms/store/
```

#To calculate the integrated luminosity using lcr2
Use the interim `python/lcr2.py` with the arugments:
```
python python/lcr2.py -r <run number>
python python/lcr2.py -i <json txt>
python python/lcr2.py -f <fill>
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