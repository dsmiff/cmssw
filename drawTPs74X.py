import ROOT as ROOT
from ROOT import gROOT, TH1F, TH2, TFile, TCanvas, gBenchmark, TLegend, TLatex, TObject

gROOT.Reset()

def CanvasSetup(co):
    co.GetFrame().SetFillColor( 21 )
    co.GetFrame().SetBorderSize( 6 )
    co.GetFrame().SetBorderMode( -1 )

c1 = TCanvas("c1","iEtaBEFV0",200,10,700,500)
CanvasSetup(c1)

c2 = TCanvas("c2","iEtaV0",200,10,700,500)
CanvasSetup(c2)

c3 = TCanvas("c3","iEtaV0",200,10,700,500)
CanvasSetup(c3)

c4 = TCanvas("c4","iEtaV1", 200, 10, 700,500)
CanvasSetup(c4)

c5 = TCanvas("c5","iEtavsiPhi", 200, 10, 700,500)
CanvasSetup(c5)

c6 = TCanvas("c6","iEtV1", 200, 10, 700,500)
CanvasSetup(c6)

c7 = TCanvas("c7","iEtV0", 200, 10, 700,500)
CanvasSetup(c7)



ROOT.gStyle.SetOptStat(0)

samples = ['HydJetQ','MinBias']

for sample in samples:

    leg = TLegend(0.4,0.8,0.6,0.88)
    leg.SetHeader("CMSSW_7_4_X")
    leg.SetTextSize(0.04)
    leg.SetBorderSize(0)
    leg.SetFillColor(-1)
    
    file = gROOT.FindObject('HCalTPDump_'+sample+'.root')
    if file:
        file.Close()

        gBenchmark.Start('drawTPs')

    
    file = TFile('HCalTPDump_'+sample+'.root')
    dir = file.GetDirectory('histos')
    tree = dir.Get('tps')
        
    c1.cd()
    tree.Draw("ieta>>h_ieta_v0")
    h_ieta_v0BEF = ROOT.gROOT.FindObject("h_ieta_v0")
    iEtanBinsV0BEF = h_ieta_v0BEF.GetNbinsX()
    h_ieta_v0BEF.SetXTitle("ieta")
    h_ieta_v0BEF.SetTitle("Tower hits for B/E/F in ieta, V0 + V1")
    h_ieta_v0BEF.SetFillColor( 49 )
    leg.Draw()
    c1.Modified()
    c1.Update()
    c1.Print("h_ieta_v0BEF_"+sample+".pdf")
    

    c2.cd()
    h_ieta_v0 = h_ieta_v0BEF.Clone("h_ieta_v0")
    for i in range(9, 66):
        h_ieta_v0.SetBinContent(i,0)
        h_ieta_v0.Draw()
        h_ieta_v0.SetTitle("Tower hits in ieta, V0")
        h_ieta_v0.SetFillColor( 48 )
        c2.Modified()
    leg.Draw()    
    c2.Update()
    c2.Print("h_ieta_v0_"+sample+".pdf")
            

    c3.cd()
    tree.Draw("ieta>>h_ieta_v1","version==1")
    h_ieta_v1 = ROOT.gROOT.FindObject("h_ieta_v1")
    iEtanBinsV1 = h_ieta_v1.GetNbinsX()
    h_ieta_v1.SetXTitle("ieta")
    h_ieta_v1.SetTitle("Tower hits in ieta, V1")
    h_ieta_v1.SetFillColor( 48 )
    leg.Draw()
    c3.Modified()
    c3.Update()
    c3.Print("h_ieta_v1_"+sample+".pdf")
    
    c4.cd()
    h_ieta_v1_1 = h_ieta_v1.Clone("h_ieta_v1_1")
    for i in range(10,84):
        h_ieta_v1_1.SetBinContent(i,0)
        h_ieta_v1_1.Draw()
        h_ieta_v1_1.SetTitle("Tower hits in ieta, V1")
        h_ieta_v1_1.SetFillColor( 2 )
        #h_ieta_v1_1.GetYaxis().SetRangeUser(0,28000)
        #h_ieta_v0.Draw("SAME")

    leg.Draw()
    c4.Modified()
    c4.Update()
    c4.Print("h_ieta_v1_1_"+sample+".pdf")

    c5.cd()
    hietavsiphi = dir.Get('tp_multiplicity')
    
    #for i in range(12,80):
     #   hietavsiphi.SetBinContent(i,0)
      #  hietavsiphi.Draw("CONTZ")
    hietavsiphi.Draw("CONTZ")
    c5.Modified()
    c5.Update()
    c5.Print("h_ietavsiphi_"+sample+".pdf")

    c6.cd()
    tree.Draw("et>>heta_v1","version==1")
    heta_v1 = ROOT.gROOT.FindObject("heta_v1")
    heta_v1.SetXTitle("E_{T} [GeV]")
    heta_v1.SetTitle("Compressed Et, V1")
    heta_v1.Draw()
    leg.Draw()
    c6.Modified()
    c6.Update()
    c6.Print("het_v1_"+sample+".pdf")

    
    c7.cd()
    tree.Draw("et>>heta_v0","version==0")
    heta_v0 = ROOT.gROOT.FindObject("heta_v0")
    heta_v0.SetXTitle("E_{T} [GeV]")
    heta_v0.SetTitle("Compressed Et, V1")
    heta_v0.Draw()
    leg.Draw()
    c7.Modified()
    c7.Update()
    c7.Print("het_v0_"+sample+".pdf")

                

    

