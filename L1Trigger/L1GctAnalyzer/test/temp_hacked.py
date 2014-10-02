import FWCore.ParameterSet.Config as cms

process = cms.Process('FibreAnalyser')

process.maxEvents = cms.untracked.PSet ( input = cms.untracked.int32 ( 3564 ) )

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
    destinations = cms.untracked.vstring ( "detailedInfo_hacked" ),
    detailedInfo_hacked = cms.untracked.PSet ( threshold = cms.untracked.string("INFO") ),
#    debugModules = cms.untracked.vstring ( "l1GctHwDigis", "FibreAnalysis" ),
        debugModules = cms.untracked.vstring ( "*" ),
#    #suppressWarning = cms.untracked.vstring ( "source", "l1GctHwDigis" )

)

process.gctRaw = cms.EDProducer( "TextToRaw",
 #Only select one of these at a time
 #filename = cms.untracked.string ( "counter_2008_03_04.dat" )
 #filename = cms.untracked.string ( "logical_id_2008_03_04.dat" )
 #filename = cms.untracked.string ( "jet_counter_2008_05_14.dat" )
    filename = cms.untracked.string ( "logical_id_hacked.txt" )
)

process.l1GctHwDigis = cms.EDProducer( "GctRawToDigi",
  inputLabel = cms.InputTag("gctRaw"),
  gctFedId = cms.untracked.int32(745),
  verbose = cms.untracked.bool(False),
  hltMode = cms.bool(False),
  grenCompatibilityMode = cms.bool(False),
  unpackEm = cms.untracked.bool(True),
  unpackJets = cms.untracked.bool(True),
  unpackEtSums = cms.untracked.bool(True),
  unpackInternEm = cms.untracked.bool(True),
  unpackRct = cms.untracked.bool(True),
  unpackFibres = cms.untracked.bool(True),
  numberOfGctSamplesToUnpack = cms.uint32(5),
  numberOfRctSamplesToUnpack = cms.uint32(5),
  unpackSharedRegions  = cms.bool(True),  
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
