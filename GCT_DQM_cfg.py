import FWCore.ParameterSet.Config as cms

process = cms.Process("GCTO2O")

## Import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration/StandardSequences/SimL1Emulator_cff')
process.load('Configuration/StandardSequences/EndOfProcess_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")

## Global tags:
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag.globaltag = cms.string('GR_P_V56')

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",

        fileNames = cms.untracked.vstring('root://xrootd.unl.edu//store/data/Run2015A/L1MinimumBias/RAW/v1/000/247/612/00000/AA9A78F7-D60F-E511-A531-02163E013835.root')

)

#process.load('L1TriggerConfig.GctConfigProducers.l1GctConfig_cfi')
#process.L1GctConfigProducers.JetFinderCentralJetSeed = cms.double(0.5)
#process.L1GctConfigProducers.JetFinderForwardJetSeed = cms.double(0.5)


process.gctDigis.numberOfGctSamplesToUnpack = cms.uint32(1)
process.simGctDigis.inputLabel = cms.InputTag('gctDigis')
process.simGctDigis.writeInternalData = cms.bool(True)

# Path
process.p = cms.Path(
    process.gctDigis
    *process.simGctDigis
)

process.output = cms.OutputModule(
    "PoolOutputModule",
    outputCommands = cms.untracked.vstring(
        # 'keep *'
        'drop *',
        'keep *_gctDigis_*_*',
        'keep *_simGctDigis_*_*',
        'keep *_simGctDigisRCT_*_*',
        ),
    fileName = cms.untracked.string('GCTDataEmulatorL1MinBias_bug.root')
    )

process.output_step = cms.EndPath(process.output)

process.schedule = cms.Schedule(
    process.p,
    process.output_step
    )
