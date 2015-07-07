# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: miniAOD-prod -s PAT --eventcontent MINIAOD --runUnscheduled --data --filein /store/data/Run2015A/SingleMu/AOD/PromptReco-v1/000/246/951/00000/2EF6AD99-BA0B-E511-B4F6-02163E0141BD.root --conditions GR_P_V56 --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('PAT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source -- CHANGE ACCORDING TO SAMPLES
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(['/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/0E3B9C6A-2B0C-E511-AEC0-02163E013653.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/189003F4-7B0C-E511-931E-02163E0145E7.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/2A5DF0A9-5E0C-E511-8257-02163E012069.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/2AD84A65-D30B-E511-A36D-02163E0145F4.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/3EC9494E-720C-E511-8664-02163E0142D7.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/50523478-9F0C-E511-B1C4-02163E0145E7.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/50964885-C70B-E511-BC20-02163E011B58.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/5CA9D3BF-550C-E511-BE3F-02163E0134D5.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/5EA3D912-E30B-E511-A2DC-02163E013614.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/6AD3BAD2-8C0C-E511-9383-02163E0145D0.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/6C667956-4C0C-E511-96D9-02163E012808.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/7613CFAB-530C-E511-8226-02163E013768.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/763DA532-DC0B-E511-98DF-02163E01369F.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/7A4D4037-5A0C-E511-ABAE-02163E01429D.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/7C361CCC-CC0B-E511-BC22-02163E01380F.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/825CC73E-190C-E511-99F6-02163E013653.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/92A508A0-130C-E511-9701-02163E01257B.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/A030BBE2-1B0C-E511-A666-02163E014299.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/A2657E09-410C-E511-BE38-02163E014485.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/A8E9D5EE-470C-E511-8876-02163E01379B.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/AC14810F-C10B-E511-A4AB-02163E014695.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/C0613452-C90B-E511-9511-02163E0144F5.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/C23A5100-C90B-E511-9123-02163E014338.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/C66E68DC-CA0B-E511-959F-02163E011C14.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/E279FB62-CB0B-E511-B19B-02163E014458.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/E665EEF4-C90B-E511-89AD-02163E0119DC.root',
                                       '/store/data/Run2015A/Commissioning/AOD/PromptReco-v1/000/246/951/00000/EEB1C981-620C-E511-92C3-02163E012808.root']),
    secondaryFileNames = cms.untracked.vstring()
)
# CHANGE ACCORDING TO JSON DOWNLOADED
import FWCore.PythonUtilities.LumiList as LumiList 
process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/work/d/dosmith/CMGTools/CMSSW_7_4_5/src/2015-06-23/Cert_246908-248005_13TeV_PromptReco_Collisions15_ZeroTesla_JSON.txt').getVLuminosityBlockRange()


process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('miniAOD-prod nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.MINIAODoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('miniAOD-prod_PAT_BATCH.root'),
    outputCommands = process.MINIAODEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_P_V56', '')

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODoutput_step = cms.EndPath(process.MINIAODoutput)

#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
process.load('Configuration.StandardSequences.PAT_cff')

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllData 

#call to customisation function miniAOD_customizeAllData imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllData(process)

# End of customisation functions
