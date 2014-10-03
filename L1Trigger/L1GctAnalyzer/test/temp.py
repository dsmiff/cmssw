import FWCore.ParameterSet.Config as cms

process = cms.Process('FibreAnalyser')

process.maxEvents = cms.untracked.PSet ( input = cms.untracked.int32 ( 50 ) )

#Input file
process.source = cms.Source ( "EmptySource" )

# Output definition
process.output = cms.OutputModule(
    "PoolOutputModule",
    outputCommands = cms.untracked.vstring("keep *"),
    fileName = cms.untracked.string('FibreAnalyser.root')
)

#Logger
process.MessageLogger = cms.Service ("MessageLogger",
    destinations = cms.untracked.vstring ( "detailedInfo" ),
    detailedInfo = cms.untracked.PSet ( threshold = cms.untracked.string("INFO") ),
#    debugModules = cms.untracked.vstring ( "l1GctHwDigis", "FibreAnalysis" ),
        debugModules = cms.untracked.vstring ( "*" ),
#    #suppressWarning = cms.untracked.vstring ( "source", "l1GctHwDigis" )

)

process.gctRaw = cms.EDProducer( "TextToRaw",
 #Only select one of these at a time
 #filename = cms.untracked.string ( "counter_2008_03_04.dat" )
 #filename = cms.untracked.string ( "logical_id_2008_03_04.dat" )
 #filename = cms.untracked.string ( "jet_counter_2008_05_14.dat" )
    filename = cms.untracked.string ( "patternCaptureOrbit_hwtest__2011_02_18__10h01m55s_HfInc.txt" )
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
  unpackerVersion = cms.uint32(3)
)


#Fibre Analyzer
process.FibreAnalysis = cms.EDAnalyzer( "GctFibreAnalyzer",
  FibreSource = cms.untracked.InputTag("l1GctHwDigis"),
  #Make sure only one of these are set to True
  doLogicalID = cms.untracked.bool(True),
  doCounter = cms.untracked.bool(False)
)

# Path and EndPath definitions

process.out = cms.EndPath(
    process.output
)

process.path = cms.Path ( process.gctRaw + process.l1GctHwDigis + process.FibreAnalysis )
