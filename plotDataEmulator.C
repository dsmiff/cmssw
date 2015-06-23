{ 
  TFile f("GCTDataEmulator.root");
  TTree * tree;
  f.GetObject("Events", tree);

  // Cen jets------------------------
  TH1* hDataRank = new TH1D("hDataRank","hDataRank",64, 0, 64);
  TH1* hEmuRank = new TH1D("hEmuRank","hEmuRank", 64, 0, 64);;

  TH1* hDataEtaIndex = new TH1D("hDataEtaIndex", "hDataEta", 10, 0, 15);
  TH1* hEmuEtaIndex = new TH1D("hEmuEtaIndex", "hDataEta", 10, 0, 15);

  TH1* hDataPhiIndex = new TH1D("hDataPhiIndex", "hDataPhiIndex", 18, 0, 18);
  TH1* hEmuPhiIndex = new TH1D("hEmuPhiIndex", "hEmuPhiIndex", 18, 0, 18);

  // Forward jets----------------------------
  TH1* hDataForRank = new TH1D("hDataForRank","hDataForRank",64, 0, 64);
  TH1* hEmuForRank = new TH1D("hEmuForRank","hEmuForRank", 64, 0, 64);;

  TH1* hDataForEtaIndex = new TH1D("hDataForEtaIndex", "hDataForEta", 10, 0, 15);
  TH1* hEmuForEtaIndex = new TH1D("hEmuForEtaIndex", "hDataForEta", 10, 0, 15);

  TH1* hDataForPhiIndex = new TH1D("hDataForPhiIndex", "hDataForPhiIndex", 18, 0, 18);
  TH1* hEmuForPhiIndex = new TH1D("hEmuForPhiIndex", "hEmuForPhiIndex", 18, 0, 18);


  // Tau jets----------------------------
  TH1* hDataTauRank = new TH1D("hDataTauRank","hDataTauRank",64, 0, 64);
  TH1* hEmuTauRank = new TH1D("hEmuTauRank","hEmuTauRank", 64, 0, 64);;

  TH1* hDataTauEtaIndex = new TH1D("hDataTauEtaIndex", "hDataTauEta", 10, 0, 15);
  TH1* hEmuTauEtaIndex = new TH1D("hEmuTauEtaIndex", "hDataTauEta", 10, 0, 15);

  TH1* hDataTauPhiIndex = new TH1D("hDataTauPhiIndex", "hDataTauPhiIndex", 18, 0, 18);
  TH1* hEmuTauPhiIndex = new TH1D("hEmuTauPhiIndex", "hEmuTauPhiIndex", 18, 0, 18);


  // Cen jets---------------------------------
  tree->Draw("L1GctJetCands_gctDigis_cenJets_GCTO2O.obj.rank()>>hDataRank","L1GctJetCands_gctDigis_cenJets_GCTO2O.obj.rank()> 0");
  tree->Draw("L1GctJetCands_simGctDigis_cenJets_GCTO2O.obj.rank()>>hEmuRank","L1GctJetCands_simGctDigis_cenJets_GCTO2O.obj.rank()> 0");
  tree->Draw("L1GctJetCands_gctDigis_cenJets_GCTO2O.obj.etaIndex()>>hDataEtaIndex");			   
  tree->Draw("L1GctJetCands_simGctDigis_cenJets_GCTO2O.obj.etaIndex()>>hEmuEtaIndex");
  tree->Draw("L1GctJetCands_gctDigis_cenJets_GCTO2O.obj.phiIndex()>>hDataPhiIndex");			   
  tree->Draw("L1GctJetCands_simGctDigis_cenJets_GCTO2O.obj.phiIndex()>>hEmuPhiIndex");
  
  // Forward jets------------------------------
  tree->Draw("L1GctJetCands_gctDigis_forJets_GCTO2O.obj.rank()>>hDataForRank","L1GctJetCands_gctDigis_forJets_GCTO2O.obj.rank()> 0");
  tree->Draw("L1GctJetCands_simGctDigis_forJets_GCTO2O.obj.rank()>>hEmuForRank","L1GctJetCands_simGctDigis_forJets_GCTO2O.obj.rank()> 0");
  tree->Draw("L1GctJetCands_gctDigis_forJets_GCTO2O.obj.etaIndex()>>hDataForEtaIndex");         
  tree->Draw("L1GctJetCands_simGctDigis_forJets_GCTO2O.obj.etaIndex()>>hEmuForEtaIndex");
  tree->Draw("L1GctJetCands_gctDigis_forJets_GCTO2O.obj.phiIndex()>>hDataForPhiIndex");         
  tree->Draw("L1GctJetCands_simGctDigis_forJets_GCTO2O.obj.phiIndex()>>hEmuForPhiIndex");

  // Tau jets------------------------------
  tree->Draw("L1GctJetCands_gctDigis_tauJets_GCTO2O.obj.rank()>>hDataTauRank","L1GctJetCands_gctDigis_tauJets_GCTO2O.obj.rank()> 0");
  tree->Draw("L1GctJetCands_simGctDigis_tauJets_GCTO2O.obj.rank()>>hEmuTauRank","L1GctJetCands_simGctDigis_tauJets_GCTO2O.obj.rank()> 0");
  tree->Draw("L1GctJetCands_gctDigis_tauJets_GCTO2O.obj.etaIndex()>>hDataTauEtaIndex");         
  tree->Draw("L1GctJetCands_simGctDigis_tauJets_GCTO2O.obj.etaIndex()>>hEmuTauEtaIndex");
  tree->Draw("L1GctJetCands_gctDigis_tauJets_GCTO2O.obj.phiIndex()>>hDataTauPhiIndex");         
  tree->Draw("L1GctJetCands_simGctDigis_tauJets_GCTO2O.obj.phiIndex()>>hEmuTauPhiIndex");

  // Cen jets---------------------------------
  hDataRank->SetLineColor(2);
  hEmuRank->SetLineColor(3);
  hDataRank->SetLineStyle(9);

  hDataEtaIndex->SetLineColor(2);
  hEmuEtaIndex->SetLineColor(3);
  hDataEtaIndex->SetLineStyle(9);

  hDataPhiIndex->SetLineColor(2);
  hEmuPhiIndex->SetLineColor(3);
  hDataPhiIndex->SetLineStyle(9);

  TLegend leg(0.5, 0.5, 0.8, 0.8);
  leg.AddEntry(hDataRank, "Cen Jets Data Rank","L");
  leg.AddEntry(hEmuRank, "Cen Jet Emulator Rank","L");
  hEmuRank->SetTitle("Cen Jets rank");
  hEmuRank->Draw();
  hDataRank->Draw("SAME");
  leg.Draw();
  c1->SaveAs("GctDataEmu_CenJetCands_rank.pdf");

  
  TLegend leg2(0.5, 0.5, 0.8, 0.8);
  leg2.AddEntry(hDataRank, "Cen Jets Data EtaIndex","L");
  leg2.AddEntry(hEmuRank, "Cen Jets Emulator EtaIndex","L");
  hEmuEtaIndex->SetTitle("Cen Jets Eta Index");
  hEmuEtaIndex->Draw();
  hDataEtaIndex->Draw("SAME");
  leg2.Draw();
  c1->SaveAs("GctDataEmu_CenJetCands_EtaIndex.pdf");

  
  TLegend leg3(0.5, 0.5, 0.8, 0.8);
  leg3.AddEntry(hDataRank, "Cen Jets Data PhiIndex","L");
  leg3.AddEntry(hEmuRank, "Cen Jets Emulator PhiIndex","L");
  hEmuPhiIndex->SetTitle("Cen Jets Phi Index");
  hEmuPhiIndex->Draw();
  hDataPhiIndex->Draw("SAME");
  leg3.Draw();
  c1->SaveAs("GctDataEmu_CenJetCands_PhiIndex.pdf");


// For jets---------------------------------
  hDataForRank->SetLineColor(2);
  hEmuForRank->SetLineColor(3);
  hDataForRank->SetLineStyle(9);

  hDataForEtaIndex->SetLineColor(2);
  hEmuForEtaIndex->SetLineColor(3);
  hDataForEtaIndex->SetLineStyle(9);

  hDataForPhiIndex->SetLineColor(2);
  hEmuForPhiIndex->SetLineColor(3);
  hDataForPhiIndex->SetLineStyle(9);

  TLegend leg4(0.5, 0.5, 0.8, 0.8);
  leg4.AddEntry(hDataForRank, "For Jets Data Rank","L");
  leg4.AddEntry(hEmuForRank, "For Jet Emulator Rank","L");
  hEmuForRank->SetTitle("For Jets rank");
  hEmuForRank->Draw();
  hDataForRank->Draw("SAME");
  leg4.Draw();
  c1->SaveAs("GctDataEmu_ForJetCands_rank.pdf");

  
  TLegend leg5(0.5, 0.5, 0.8, 0.8);
  leg5.AddEntry(hDataForRank, "For Jets Data EtaIndex","L");
  leg5.AddEntry(hEmuForRank, "For Jets Emulator EtaIndex","L");
  hEmuForEtaIndex->SetTitle("For Jets Eta Index");
  hEmuForEtaIndex->Draw();
  hDataForEtaIndex->Draw("SAME");
  leg5.Draw();
  c1->SaveAs("GctDataEmu_ForJetCands_EtaIndex.pdf");

  
  TLegend leg6(0.5, 0.5, 0.8, 0.8);
  leg6.AddEntry(hDataForRank, "For Jets Data PhiIndex","L");
  leg6.AddEntry(hEmuForRank, "For Jets Emulator PhiIndex","L");
  hEmuForPhiIndex->SetTitle("For Jets Phi Index");
  hEmuForPhiIndex->Draw();
  hDataForPhiIndex->Draw("SAME");
  leg6.Draw();
  c1->SaveAs("GctDataEmu_ForJetCands_PhiIndex.pdf");

// Tau jets---------------------------------
  hDataTauRank->SetLineColor(2);
  hEmuTauRank->SetLineColor(3);
  hDataTauRank->SetLineStyle(9);

  hDataTauEtaIndex->SetLineColor(2);
  hEmuTauEtaIndex->SetLineColor(3);
  hDataTauEtaIndex->SetLineStyle(9);

  hDataTauPhiIndex->SetLineColor(2);
  hEmuTauPhiIndex->SetLineColor(3);
  hDataTauPhiIndex->SetLineStyle(9);

  TLegend leg7(0.5, 0.5, 0.8, 0.8);
  leg7.AddEntry(hDataForRank, "Tau Jets Data Rank","L");
  leg7.AddEntry(hEmuForRank, "Tau Jet Emulator Rank","L");
  hEmuTauRank->SetTitle("Tau Jets rank");
  hEmuTauRank->Draw();
  hDataTauRank->Draw("SAME");
  leg7.Draw();
  c1->SaveAs("GctDataEmu_TauJetCands_rank.pdf");

  
  TLegend leg8(0.5, 0.5, 0.8, 0.8);
  leg8.AddEntry(hDataTauRank, "Tau Jets Data EtaIndex","L");
  leg8.AddEntry(hEmuTauRank, "Tau Jets Emulator EtaIndex","L");
  hEmuTauEtaIndex->SetTitle("Tau Jets Eta Index");
  hEmuTauEtaIndex->Draw();
  hDataTauEtaIndex->Draw("SAME");
  leg8.Draw();
  c1->SaveAs("GctDataEmu_TauJetCands_EtaIndex.pdf");

  
  TLegend leg9(0.5, 0.5, 0.8, 0.8);
  leg9.AddEntry(hDataForRank, "Tau Jets Data PhiIndex","L");
  leg9.AddEntry(hEmuForRank, "Tau Jets Emulator PhiIndex","L");
  hEmuTauPhiIndex->SetTitle("Tau Jets Phi Index");
  hEmuTauPhiIndex->Draw();
  hDataTauPhiIndex->Draw("SAME");
  leg9.Draw();
  c1->SaveAs("GctDataEmu_TauJetCands_PhiIndex.pdf");

}
