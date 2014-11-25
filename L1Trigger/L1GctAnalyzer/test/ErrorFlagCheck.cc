{

  gROOT->Reset();
  gStyle->SetOptStat(0);

  //TString rootname = "gctErrorAnalyzer_single_e_50events.root";
  //TString rootname = "gctErrorAnalyzer_single_e_3564events.root";
  //TString rootname = "gctErrorAnalyzer_higgs_4e_50events.root";
  //TString rootname = "gctErrorAnalyzer_higgs_4e_3564events.root";
  //TString rootname = "gctErrorAnalyzer_susys_50events.root";
  TString rootname = "gctErrorAnalyzer_susys_3564events.root";

  TFile *rootfile = new TFile(rootname);

  std::cout << "Analysing : " << rootname<< std::endl;

  gctErrorAnalyzer.cd("ErrorHistograms_Flags");

  Int_t entries1 = isoEg_errorFlag->GetEntries();
  Int_t entries2 = nonIsoEg_errorFlag->GetEntries();
  Int_t entries3 = cenJet_errorFlag->GetEntries();
  Int_t entries4 = tauJet_errorFlag->GetEntries();
  Int_t entries5 = forJet_errorFlag->GetEntries();
  Int_t entries6 = hfRingSum_errorFlag->GetEntries();
  Int_t entries7 = hfBitCount_errorFlag->GetEntries();
  Int_t entries8 = totalEt_errorFlag->GetEntries();
  Int_t entries9 = totalHt_errorFlag->GetEntries();
  Int_t entries10 = missingEt_errorFlag->GetEntries();
  Int_t entries11 = missingHt_errorFlag->GetEntries();

  if(entries1 !=0 || entries2 != 0 || entries3 != 0 || entries4 != 0 || entries5 != 0 || entries6 != 0 || entries7 != 0 || entries8 != 0 || entries9 != 0 || entries10  != 0 || entries11 != 0){
    std::cerr << "\n\nERROR FLAGS NON ZERO" << std::endl;
    throw std::exception();
  }

  else{ std::cout << "All error flags zero" << std::endl; }


  if(entries1 !=0){ std::cerr << "\n\nERROR isoEg_errorFlag NON ZERO" << std::endl; throw std::exception(); }
  if(entries2 !=0){ std::cerr << "\n\nERROR nonIsoEg_errorFlag NON ZERO" << std::endl; throw std::exception(); }
  if(entries3 !=0){ std::cerr << "\n\nERROR cenJet_errorFlag NON ZERO" << std::endl; throw std::exception(); }
  if(entries4 !=0){ std::cerr << "\n\nERROR tauJet_errorFlag NON ZERO" << std::endl; throw std::exception(); }
  if(entries5 !=0){ std::cerr << "\n\nERROR forJet_errorFlag NON ZERO" << std::endl; throw std::exception(); }
  if(entries6 !=0){ std::cerr << "\n\nERROR hfRingSum_errorFlag NON ZERO" << std::endl;	throw std::exception();	}
  if(entries7 !=0){ std::cerr << "\n\nERROR hfBtiCount_errorFlag NON ZERO" << std::endl; throw std::exception(); }
  if(entries8 !=0){ std::cerr << "\n\nERROR totalEt_errorFlag NON ZERO"	<< std::endl; throw std::exception(); }
  if(entries9 !=0){ std::cerr << "\n\nERROR totalHt_errorFlag NON ZERO"	<< std::endl; throw std::exception(); }
  if(entries10 !=0){ std::cerr << "\n\nERROR missingEt_ErrorFlag NON ZERO" << std::endl; throw std::exception(); }
  if(entries11 !=0){ std::cerr << "\n\nERROR missingHt_ErrorFlag NON ZERO" << std::endl; throw std::exception(); }



}
