import ROOT as ROOT
from ROOT import gROOT, TH1F, TH2, TFile, TCanvas, gBenchmark, TLegend, gStyle

gROOT.Reset()

##__________________________________________________________________________________||
def CanvasSetup(co):
    co.GetFrame().SetFillColor( 21 )
    co.GetFrame().SetBorderSize( 6 )
    co.GetFrame().SetBorderMode( -1 )
    co.SetGrid()
    
def EtaBinsCalc(hist, Bins):
    bins =0
    for bin in range(0,Bins):
        if(hist.GetBinContent(bin) > 0):
            bins += 1
    return bins/2

def PhiBinsCalc(hist,Bins):
    bins = 0
    for bin in range(0,Bins):
        if(hist.GetBinContent(bin) > 0):
            bins +=1
    return bins

##___________________________________________________________________________________||
c1 = TCanvas("c1","iEtaBEFV0",200,10,700,500)
CanvasSetup(c1)

c2 = TCanvas("c2","iEtaV0",200,10,700,500)
CanvasSetup(c2)

c3 = TCanvas("c3","iPhiV0",200,10,700,500)
CanvasSetup(c3)

c4 = TCanvas("c4","iPhiV1", 200, 10, 700,500)
CanvasSetup(c4)

c5 = TCanvas("c5","iPhiEta40V1", 200, 10, 700,500)
CanvasSetup(c5)


leg = TLegend(0.4,0.8,0.6,0.88)
leg.SetHeader("CMSSW_7_3_0_pre2")
leg.SetTextSize(0.04)
leg.SetBorderSize(0)
leg.SetFillColor(-1)

##___________________________________________________________________________________||
ROOT.gStyle.SetOptStat(0)

file = gROOT.FindObject('HcalTPDump_100evts.root')
if file:
    file.Close()

gBenchmark.Start('plotTPs')

    
file = TFile('HCalTPDump_100evts.root')
dir = file.GetDirectory('histos')
tree = dir.Get('tps')

gStyle.SetTitleFontSize(0.03)
##___________________________________________________________________________________||
c1.cd()
tree.Draw("ieta_v0>>h_ieta_v0")
h_ieta_v0 = ROOT.gROOT.FindObject("h_ieta_v0")
iEtaBinsV0 = h_ieta_v0.GetNbinsX()
print 'Bins in h_ieta_V0: ', EtaBinsCalc(h_ieta_v0, iEtaBinsV0)
h_ieta_v0.SetXTitle("ieta, v0")
h_ieta_v0.SetTitle("Tower hits for v0 in ieta")
h_ieta_v0.SetFillColor( 49 )
h_ieta_v0.GetXaxis().SetNdivisions(iEtaBinsV0)
h_ieta_v0.GetXaxis().SetLabelSize(0.01)
h_ieta_v0.SetTitleFont(60)
leg.Draw()
c1.Modified()
c1.Update()
c1.Print("h_ieta_v0_73X.pdf")
c1.Print("results.pdf(")

c2.cd()
tree.Draw("ieta_v1>>h_ieta_v1")
h_ieta_v1 = ROOT.gROOT.FindObject("h_ieta_v1")
iEtaBinsV1 = h_ieta_v1.GetNbinsX()
print 'Bins in h_ieta_V1: ', EtaBinsCalc(h_ieta_v1, iEtaBinsV1)
h_ieta_v1.SetXTitle("ieta, v1")
h_ieta_v1.SetTitle("Tower hits for v1 in ieta")
h_ieta_v1.SetFillColor( 49 )
h_ieta_v1.GetXaxis().SetNdivisions(iEtaBinsV1)
h_ieta_v1.GetXaxis().SetLabelSize(0.01)
h_ieta_v1.SetTitleFont(60)
leg.Draw()
c2.Modified()
c2.Update()
c2.Print("h_ieta_v1_73X.pdf")
c2.Print("results.pdf(")

c3.cd()
tree.Draw("iphi_v0>>h_iphi_v0")
h_iphi_v0 = ROOT.gROOT.FindObject("h_iphi_v0")
iPhiBinsV0 = h_iphi_v0.GetNbinsX()
print 'Bins in h_iphi_V0: ', PhiBinsCalc(h_iphi_v0,iPhiBinsV0)
h_iphi_v0.SetXTitle("iphi, v0")
h_iphi_v0.SetTitle("Tower hits for v0 in iphi")
h_iphi_v0.SetTitleSize(0.04)
h_iphi_v0.SetFillColor( 49 )
h_iphi_v0.GetXaxis().SetNdivisions(iPhiBinsV0)
h_iphi_v0.GetXaxis().SetLabelSize(0.01)
h_iphi_v0.SetTitleFont(60)
leg.Draw()
c3.Modified()
c3.Update()
c3.Print("h_iphi_v0_73X.pdf")
c3.Print("results.pdf(")

c4.cd()
tree.Draw("iphi_v1>>h_iphi_v1")
h_iphi_v1 = ROOT.gROOT.FindObject("h_iphi_v1")
iPhiBinsV1 = h_iphi_v1.GetNbinsX()
print 'Bins in h_iphi_V1: ', PhiBinsCalc(h_iphi_v1,iPhiBinsV1)
h_iphi_v1.SetXTitle("iphi, v1")
h_iphi_v1.SetTitle("Tower hits for v1 in iphi")
h_iphi_v1.SetFillColor( 49 )
h_iphi_v1.GetXaxis().SetNdivisions(iPhiBinsV1)
h_iphi_v1.GetXaxis().SetLabelSize(0.01)
h_iphi_v1.SetTitleFont(60)
leg.Draw()
c4.Modified()
c4.Update()
c4.Print("h_iphi_v1_73X.pdf")
c4.Print("results.pdf(")


c5.cd()
tree.Draw("iphi_v1_eta40>>h_iphi_v1_eta40")
h_iphi_v1_eta40 = ROOT.gROOT.FindObject("h_iphi_v1_eta40")
iPhiBinsV1_ETA40 = h_iphi_v1_eta40.GetNbinsX()
print 'Bins in h_iphi_V1_ETA40: ', PhiBinsCalc(h_iphi_v1_eta40,iPhiBinsV1_ETA40) - 1 # Remove 1 for the 1st bin that shouldn't be filled
h_iphi_v1_eta40.SetXTitle("iphi, v1")
h_iphi_v1_eta40.SetTitle("Tower hits for v1, ieta > 40, in iphi")
h_iphi_v1_eta40.SetFillColor( 49 )
h_iphi_v1_eta40.GetXaxis().SetRangeUser(1,75)
h_iphi_v1_eta40.GetXaxis().SetNdivisions(iPhiBinsV1_ETA40)
h_iphi_v1_eta40.GetXaxis().SetLabelSize(0.01)
h_iphi_v1_eta40.SetTitleFont(60)
leg.Draw()
c5.Modified()
c5.Update()
c5.Print("h_iphi_v1_eta40_73X.pdf")
c5.Print("results.pdf)")




##___________________________________________________________________________________||



