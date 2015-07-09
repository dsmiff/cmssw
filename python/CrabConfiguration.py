"""
This is an example configuration file for CRAB3 client, covering
most of the available configuration options.
"""

from WMCore.Configuration import Configuration
import os

config = Configuration()

## General options for the client
config.section_("General")

'''
Request Name can be changed 
'''
config.General.requestName   = 'MiniAOD_prod'
#config.General.workArea   = '/path/to/workarea'

## Specific option of the job type
## these options are directly readable from the job type plugin
config.section_("JobType")

'''
Full path needed, need to change for individual user
'''
config.JobType.psetName    = '/afs/cern.ch/work/d/dosmith/CMGTools/CMSSW_7_4_5/src/miniAOD-PROD_CRAB.py'

## Does the job read any additional private file:
#config.JobType.inputFiles  = ['/tmp/input_file']
## Does the job write any output files that need to be collected BESIDES those in output modules or TFileService
#config.JobType.outputFiles  = ['output_file']

'''
Specific data options - change to run over data in question
'''
config.section_("Data")
config.Data.inputDataset = '/EGamma/Run2015A-PromptReco-v1/AOD'


'''
Splitting Algorithms - LumiBased given by JSON downloaded into job dir
'''

config.Data.splitting = 'LumiBased'
#config.Data.splitting = 'EventBased'
#config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 20
NJOBS = 10
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

## For lumiMask http and https urls are also allowed
## Full path is needed, need to change to individual user
config.Data.lumiMask = '/afs/cern.ch/work/d/dosmith/CMGTools/CMSSW_7_4_5/src/'


#config.Data.splitting = 'EventBased'
#config.Data.unitsPerJob = 10
#config.Data.totalUnits = 100

## To publish produced data there are 3 parameters to set:
#config.Data.inputDBS = "https://cmsweb.cern.ch/dbs/prod/global/DBSReader"
#config.Data.publishDBS = "https://cmsweb.cern.ch/dbs/prod/prod/phys03/DBSWriter"

## User options
config.section_("User")
#config.User.email = ''


'''
Storage site can change if necessary - can be set to T2_UK_SGrid_Bristol, T2_UK_London_IC
'''
config.section_("Site")
config.Site.storageSite = 'T2_UK_SGrid_Bristol'
config.Data.outLFNDirBase = '/store/user/dosmith/'
config.Data.publication = True

'''
To maintain consistency, publishDataName should be the same for every crab job -- awaiting an agreed name
'''
config.Data.publishDataName = "NAME"

