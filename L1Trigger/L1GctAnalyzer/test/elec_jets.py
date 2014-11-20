import FWCore.ParameterSet.Config as cms

process = cms.Process('FibreAnalyser')

process.maxEvents = cms.untracked.PSet ( input = cms.untracked.int32 ( 1 ) )

#Input file
process.source = cms.Source ( "EmptySource" )

# Output definition
process.output = cms.OutputModule(
    "PoolOutputModule",
    outputCommands = cms.untracked.vstring("keep *"),
    fileName = cms.untracked.string('FibreAnalyser.root')
)

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.destinations.append('detailedInfo')
process.MessageLogger.debugModules = ['*']

process.MessageLogger.detailedInfo = cms.untracked.PSet (
        threshold = cms.untracked.string("INFO")
        )

process.MessageLogger.cerr.threshold = 'DEBUG'
process.MessageLogger.cerr.DEBUG = cms.untracked.PSet( limit = cms.untracked.int32(-1) )
process.MessageLogger.cerr.INFO = cms.untracked.PSet( limit = cms.untracked.int32(-1) )
process.MessageLogger.cerr.WARNING = cms.untracked.PSet( limit = cms.untracked.int32(-1) )
process.MessageLogger.cerr.ERROR = cms.untracked.PSet( limit = cms.untracked.int32(-1) )

process.gctRaw = cms.EDProducer( "TextToRaw",
 #Only select one of these at a time
 #filename = cms.untracked.string ( "counter_2008_03_04.dat" )
 #filename = cms.untracked.string ( "logical_id_2008_03_04.dat" )
 #filename = cms.untracked.string ( "jet_counter_2008_05_14.dat" )
 #filename = cms.untracked.string ( "patternCaptureOrbit_hwtest__2011_02_18__10h01m55s_HfInc.txt" )
 #filename = cms.untracked.string( "patternCapture_ts__2014_10_08__17h09m45s.txt") 
 #filename = cms.untracked.string( "patternCapture_ts__2014_10_08__17h55m37s.txt") 
 #filename = cms.untracked.string( "patternCapture_ts__2014_10_08__17h09m45s_copy.txt")  
 #filename = cms.untracked.string( "patternCapture_ts__2014_10_08__18h07m10s_copy_hacked.txt")  
 #filename = cms.untracked.string( "patternCapture_ts__2014_10_08__17h55m37s.txt")  
 #filename = cms.untracked.string( "patternCapture_ts__2014_11_18__17h05m32s.txt" )
 filename = cms.untracked.string( "patternCapture_ts__2014_11_19__14h54m28s.txt" )
#GctFedId =  cms.untracked.int32( 745 ),
    #FileEventOffset = cms.untracked.int32( 0 ) 

)

process.l1GctHwDigis = cms.EDProducer( "GctRawToDigi",
  inputLabel = cms.InputTag("gctRaw"),
  gctFedId = cms.untracked.int32(745),
  verbose = cms.untracked.bool(True),
  hltMode = cms.bool(False),
  grenCompatibilityMode = cms.bool(False),
  unpackEm = cms.untracked.bool(False),
  unpackJets = cms.untracked.bool(False),
  unpackEtSums = cms.untracked.bool(False),
  unpackInternEm = cms.untracked.bool(False),
  unpackRct = cms.untracked.bool(False),
  unpackFibres = cms.untracked.bool(True),
  numberOfGctSamplesToUnpack = cms.uint32(1),
  numberOfRctSamplesToUnpack = cms.uint32(1),
  unpackSharedRegions  = cms.bool(False),  
  unpackerVersion = cms.uint32(38)
)


#Fibre Analyzer
process.FibreAnalysis = cms.EDAnalyzer( "GctFibreAnalyzer",
  FibreSource = cms.untracked.InputTag("l1GctHwDigis"),
  #Make sure only one of these are set to True
  doLogicalID = cms.untracked.bool(True),
  doElectronIDs = cms.untracked.bool(True),
  doJetIDs = cms.untracked.bool(True),
  doCounter = cms.untracked.bool(False)
)

# Path and EndPath definitions

process.out = cms.EndPath(
    process.output
)

process.path = cms.Path ( process.gctRaw*process.l1GctHwDigis*process.FibreAnalysis )
