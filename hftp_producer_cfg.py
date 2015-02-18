import FWCore.ParameterSet.Config as cms

process = cms.Process('RAW2DIGI')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.source = cms.Source("PoolSource",
        # eventsToProcess = cms.untracked.VEventRange(),
        fileNames = cms.untracked.vstring('/store/relval/CMSSW_7_3_0_pre2/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V1-v1/00000/0419E8FC-C46B-E411-9A71-002481E0DB88.root')
        )

process.hcalDigis.InputLabel = cms.InputTag("hcalRawData")

process.p = cms.Path(
        process.hcalDigis
        )
