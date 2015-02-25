import FWCore.ParameterSet.Config as cms

process = cms.Process("HFCALIB")


#--- Steps available to this configuration       ---#
#--- (1) Trigger filter.  Input data RAW/AOD     ---#
#--- (2) N(vertex) filter.  Only valid for MC    ---#
#--- (3) Reconstruction, assuming RAW input data ---#
#--- (4) Filtering on ECAL+HF, Z mass            ---#
#--- (5) HF Calibration analysis                 ---#
doRerecoOnRaw = True

#-----------------------------------#
#--- Flag for running on data/MC ---#
#-----------------------------------#
isData = False

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
#process.HcalTrigTowerGeometryESProducer.useFullGranularityHF = cms.bool( True )

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.source = cms.Source("PoolSource",
        # eventsToProcess = cms.untracked.VEventRange(),
        #fileNames = cms.untracked.vstring('/store/relval/CMSSW_7_0_0_pre11/RelValZEE_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU50ns_POSTLS162_V5_OldTrk-v1/00000/48CC1D33-6E6A-E311-8855-001D09F251EF.root')
        fileNames = cms.untracked.vstring('/store/relval/CMSSW_7_3_0_pre2/RelValMinBias_13/GEN-SIM-DIGI-RAW-HLTDEBUG/MCRUN2_73_V1-v1/00000/0419E8FC-C46B-E411-9A71-002481E0DB88.root')
        )

process.out = cms.OutputModule( "PoolOutputModule",
        fileName = cms.untracked.string("output.root"),
        SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
        outputCommands = cms.untracked.vstring( 'keep *' )
        )

###--- (3) Re-RECO from RAW ---###
### Auto generated configuration file using Revision: 1.381.2.6
### Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v
### with command line options: -s RAW2DIGI,RECO ...

if doRerecoOnRaw:
    # process.reconstructionFromRawSequence = cms.Sequence(process.RawToDigi * process.L1Reco * process.reconstruction)
    process.reconstructionFromRawSequence = cms.Sequence(process.RawToDigi)

# From Maria Cepeda Hermida's suggestion for rctDigis testing
#from L1Trigger.RegionalCaloTrigger.rctDigis_cfi import rctDigis
#process.rctDigis = rctDigis
process.load('L1Trigger.RegionalCaloTrigger.rctDigis_cfi')
process.rctDigis.hcalDigis = cms.VInputTag(cms.InputTag("simHcalTriggerPrimitiveDigis"))


#--- Create TP digis from unpacked digis by calling HcalTrigPrimiProducer.cc in hcaltpdigi_cfi.py
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
#--- Histograms ---#
process.TFileService = cms.Service("TFileService",
        fileName = cms.string('HcalTrigDigiDump.root')
        )
#process.histos = cms.EDAnalyzer("HcalTriggerDigiDump")

###--- Assemble everything ---###
process.boolTrue = cms.EDFilter( 'HLTBool',
        result = cms.bool( True )
        )
process.calibPreSequence = cms.Sequence(process.boolTrue)

process.p = cms.Path( process.calibPreSequence + process.hcalCond + process.simHcalTriggerPrimitiveDigis + process.dump )
#process.p = cms.Path( process.calibPreSequence + process.simHcalTriggerPrimitiveDigis + process.dump + process.rctDigis )


