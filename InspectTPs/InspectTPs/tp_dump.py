import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
        # eventsToProcess = cms.untracked.VEventRange(),
        fileNames = cms.untracked.vstring('/store/relval/CMSSW_7_3_0_pre2/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V1-v1/00000/6E3DF4C0-BB6B-E411-BBB2-FA163EC39500.root')
)

process.demo = cms.EDAnalyzer('InspectTPs'
)

process.TFileService = cms.Service("TFileService",
        closeFileFast = cms.untracked.bool(True),
        fileName = cms.string("HcalTPDump.root")
)

process.p = cms.Path(process.demo)
