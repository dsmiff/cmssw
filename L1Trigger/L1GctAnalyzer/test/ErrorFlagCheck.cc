{

  gROOT->Reset();
  gStyle->SetOptStat(0);

  //TString rootname = "gctErrorAnalyzer_single_e_50events.root";
  //TString rootname = "gctErrorAnalyzer_single_e_3564events.root";
  //TString rootname = "gctErrorAnalyzer_higgs_4e_50events.root";
  //TString rootname = "gctErrorAnalyzer_higgs_4e_3564events.root";
  //TString rootname = "gctErrorAnalyzer_susy_50events.root";
  TString rootname = "gctErrorAnalyzer_susy_3564events.root";

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


	if(entries1 !=0){
	 std:cout << "\nERROR isoEg_errorFlag NON ZERO" << std::endl;
	 
        }	

 	if(entries2 !=0){
	 std::cout << "\n\nERROR nonIsoEg_errorFlag NON ZERO" << std::endl;
	 }
  
	if(entries3 !=0){
	 std::cout << "\n\nERROR cenJet_errorFlag NON ZERO" << std::endl; 
        }	
  
	if(entries4 !=0){
	 std::cout << "\n\nERROR tauJet_errorFlag NON ZERO" << std::endl; 
	}
  
	if(entries5 !=0){
	 std::cout << "\n\nERROR forJet_errorFlag NON ZERO" << std::endl; 
	}
  
	if(entries6 !=0){ 
	std::cout << "\n\nERROR hfRingSum_errorFlag NON ZERO" << std::endl;	
        }		
  
	if(entries7 !=0){ 
	std::cout << "\n\nERROR hfBtiCount_errorFlag NON ZERO" << std::endl; 
	}

        if(entries8 !=0){ 
	std::cout << "\n\nERROR totalEt_errorFlag NON ZERO"	<< std::endl; 
	}

        if(entries9 !=0){ 
	std::cout << "\n\nERROR totalHt_errorFlag NON ZERO"	<< std::endl; 
	}
  
	if(entries10 !=0){
	 std::cout << "\n\nERROR missingEt_ErrorFlag NON ZERO" << std::endl; 
	}
  
	if(entries11 !=0){ 
	std::cout << "\n\nERROR missingHt_ErrorFlag NON ZERO" << std::endl; 
	}



}
