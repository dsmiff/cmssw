import FWCore.ParameterSet.Config as cms

process = cms.Process("HFCALIB")

## Import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')

process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')

## Global tags:
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# Note that this assumes the 6X post-LS1 Monte Carlo
process.GlobalTag.globaltag = cms.string('POSTLS162_V5::All')

process.load('SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff')

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.source = cms.Source("PoolSource",
        # eventsToProcess = cms.untracked.VEventRange(),
        fileNames = cms.untracked.vstring('/store/relval/CMSSW_7_3_0_pre2/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V1-v1/00000/0419E8FC-C46B-E411-9A71-002481E0DB88.root')
        )


# From Maria Cepeda Hermida's suggestion for rctDigis testing
#from L1Trigger.RegionalCaloTrigger.rctDigis_cfi import rctDigis
#process.rctDigis = rctDigis
process.load('L1Trigger.RegionalCaloTrigger.rctDigis_cfi')
process.rctDigis.hcalDigis = cms.VInputTag(cms.InputTag("simHcalTriggerPrimitiveDigis"))

#--- Create TP digis from unpacked digis
process.load('SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff')

# The inputtags here might need to be changed if you don't see any trigger
# primitives. If these tags aren't found, the code silently proceeds.
#process.simHcalTriggerPrimitiveDigis.inputLabel = cms.VInputTag( cms.InputTag('simHcalUnsuppressedDigis'), cms.InputTag('simHcalUnsuppressedDigis') )
process.simHcalTriggerPrimitiveDigis.inputLabel = cms.VInputTag( cms.InputTag('simHcalDigis'), cms.InputTag('simHcalDigis') )
process.simHcalTriggerPrimitiveDigis.FrontEndFormatError = cms.bool(False)

#--- Conditions dump ---#
process.hcalCond = cms.EDAnalyzer("HcalDumpConditions",
    dump = cms.untracked.vstring(
         'LutMetadata'
    ),
    outFilePrefix = cms.untracked.string('DumpCond')
)

#process.es_ascii = cms.ESSource("HcalTextCalibrations",
#    input = cms.VPSet(
#        cms.PSet(
#            object = cms.string('LutMetadata'),
#            file = cms.FileInPath('CalibCalorimetry/CaloTPG/HcalLutMetadata_now_with_HTV1')
#        )
#    )
#)
#process.es_prefer_es_ascii = cms.ESPrefer("HcalTextCalibrations", "es_ascii")

process.es_pool = cms.ESSource("PoolDBESSource",
        process.CondDBSetup,
        timetype = cms.string('runnumber'),
        toGet = cms.VPSet(
            cms.PSet(
                record = cms.string("HcalLutMetadataRcd"),
                tag = cms.string("HcalLutMetadata_v3.00_mc")
                )
            ),
        connect = cms.string('frontier://cmsfrontier.cern.ch:8000/FrontierProd/CMS_COND_31X_HCAL'),
        authenticationMethod = cms.untracked.uint32(0),
        )

process.es_prefer_es_pool = cms.ESPrefer("PoolDBESSource", "es_pool")

#--- Dump digi information ---#
process.dump  = cms.EDAnalyzer("HcalDigiDump")

process.p = cms.Path(
        process.simHcalTriggerPrimitiveDigis
        + process.dump
        #+ process.hcalCond
        + process.rctDigis
        )
