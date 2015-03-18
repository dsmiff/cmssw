// -*- C++ -*-
//
// Package:    InspectTPs/InspectTPs
// Class:      InspectTPs
// 
/**\class InspectTPs InspectTPs.cc InspectTPs/InspectTPs/plugins/InspectTPs.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Dominic Smith
//         Created:  Tue, 17 Mar 2015 14:46:30 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "DQMServices/Core/interface/DQMStore.h"
#include "DQMServices/Core/interface/MonitorElement.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"
#include "Geometry/CaloGeometry/interface/CaloSubdetectorGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloCellGeometry.h"
#include "SimDataFormats/CaloHit/interface/PCaloHitContainer.h"
#include "CalibFormats/CaloTPG/interface/CaloTPGTranscoder.h"
#include "CalibFormats/CaloTPG/interface/CaloTPGRecord.h"
#include "CalibFormats/HcalObjects/interface/HcalDbRecord.h"
#include "CalibFormats/HcalObjects/interface/HcalCoderDb.h"
#include "CalibFormats/HcalObjects/interface/HcalCalibrations.h"
#include "CondFormats/HcalObjects/interface/HcalQIEShape.h"
#include "DataFormats/HcalDigi/interface/HBHEDataFrame.h"
#include "CalibFormats/HcalObjects/interface/HcalDbService.h"
#include "DataFormats/HcalDigi/interface/HcalDigiCollections.h"
#include "Geometry/HcalTowerAlgo/interface/HcalTrigTowerGeometry.h"
#include "Geometry/CaloTopology/interface/HcalTopology.h"

#include "TGraph.h"
#include "TNtuple.h"
#include "TH1.h"
#include "TH2.h"
#include <vector>
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/HcalDetId/interface/HcalSubdetector.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"
//
// class declaration
//

class InspectTPs : public edm::EDAnalyzer {
   public:
      explicit InspectTPs(const edm::ParameterSet&);
      ~InspectTPs();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;


  
      // ----------member data ---------------------------
  edm::ESHandle<CaloGeometry> geometry;
  edm::ESHandle<HcalDbService> conditions;

  
  bool first_;

  //  std::vector<edm::InputTag> frames_;
  //  edm::InputTag digis_;
  //  edm::InputTag rechits_;

  TH2D *df_multiplicity_;
  TH2D *tp_multiplicity_;

  TTree *tps_;
  
  double tp_energy_;
  double tp_linear_;
  int tp_ieta_;
  int tp_iphi_;
  int tp_depth_max_;
  int tp_sub_max_;
  
  
  
};

InspectTPs::InspectTPs(const edm::ParameterSet& iConfig):
  edm::EDAnalyzer(),
  first_(true)
  //  frames_(iConfig.getParameter<std::vector<edm::InputTag>>("DataFrames")),
  //  digis_(iConfig.getParameter<edm::InputTag>("TriggerPrimitives")),
  //  rechits_(iConfig.getParameter<edm::InputTag>("RecHits"))

{
  edm::Service<TFileService> fs;

  tp_multiplicity_ = fs->make<TH2D>("tp_multiplicity", "TrigPrim multiplicity;ieta;iphi", 65, -32.5, 32.5, 72, 0.5, 72.5);

  tps_ = fs->make<TTree>("tps", "Trigger primitives");
  tps_->Branch("et", &tp_energy_);
  tps_->Branch("ieta", &tp_ieta_);
  tps_->Branch("iphi", &tp_iphi_);
  tps_->Branch("depth_max", &tp_depth_max_);
  tps_->Branch("sub_mac", &tp_sub_max_);
  
  consumesMany<HcalTrigPrimDigiCollection>();
  
}


InspectTPs::~InspectTPs()
{
}

void
InspectTPs::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace std;

   ESHandle<CaloTPGTranscoder> decoder;
   iSetup.get<CaloTPGRecord>().get(decoder);
   //  decoder->setup(iSetup, CaloTPGTranscoder::HcalTPG);


   Handle<HcalTrigPrimDigiCollection> htp;
   iEvent.getByLabel("htps", htp);
   
   std::vector<edm::Handle<HcalTrigPrimDigiCollection> > htps;
   
   //   vector<HcalTriggerPrimitiveDigi> tps;
   vector<HcalTriggerPrimitiveDigi> triggvec;
   
   iEvent.getManyByType(htps);
   std::vector<edm::Handle<HcalTrigPrimDigiCollection> >::iterator i;
   for (i=htps.begin(); i!=htps.end(); i++) {
     const HcalTrigPrimDigiCollection& c=*(*i);
     cout << c.size() << endl;

     for (HcalTrigPrimDigiCollection::const_iterator j=c.begin(); j!=c.end(); j++) {
       cout << *j << std::endl;
       triggvec.push_back(*j);
       }
   }

  for( unsigned int a = 0 ; a < triggvec.size() ; a++ ) {

    tp_sub_max_   = triggvec[a].id().subdet();
    tp_depth_max_ = triggvec[a].id().depth();
    tp_ieta_  = triggvec[a].id().ieta();
    tp_iphi_  = triggvec[a].id().iphi();
    tp_energy_ = triggvec[a].SOI_compressedEt();
  }

  tps_->Fill();
}


// ------------ method called once each job just before starting event loop  ------------
void 
InspectTPs::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
InspectTPs::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------

void 
InspectTPs::beginRun(edm::Run const&, edm::EventSetup const&)
{
}


// ------------ method called when ending the processing of a run  ------------

void 
InspectTPs::endRun(edm::Run const&, edm::EventSetup const&)
{
}


// ------------ method called when starting to processes a luminosity block  ------------

void 
InspectTPs::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}


// ------------ method called when ending the processing of a luminosity block  ------------

void 
InspectTPs::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
InspectTPs::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(InspectTPs);
