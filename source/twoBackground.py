#!/usr/bin/env python
# -*-coding:Latin-1 -*

import atlasplots
from   atlasplots import atlas_style as astyle
from   atlasplots import utils
from   atlasplots import config_reader as config

import ROOT
import ROOT as root
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine,TChain
import ROOT as root

from array import array

def makeLegend(hists, xmin, ymin, xmax, ymax):
    legend = root.TLegend(xmin, ymin, xmax, ymax)
    legend.SetTextSize(0.03)
    legend.SetFillColor(0)
    legend.SetLineColor(0)
    legend.SetBorderSize(0)
    for hist in hists:
        legend.AddEntry(hist, hist.GetName())
    return legend

def ColorParameter(Hist, FillStyle, FillColor, LineColor, LineWidth):
    Hist.SetFillStyle(FillStyle)
    Hist.SetFillColor(FillColor)
    Hist.SetLineColor(LineColor)
    Hist.SetLineWidth(LineWidth)

class two2DBackground:
    """Classe représentant une personne"""

    def __init__(self):
        """Constructeur de notre classe"""


    def makeControlPlot(self, data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Indice, channel, Energy, Indic):
	

	Nsignal, Ndata, NBkg_top, NBkg_diboson, NBkg_w, NBkg_z =  ([] for i in range(6))
	for i in range(1, 7):
	    Nsignal.append( 	 Signal.Get(channel+'Selection/Lepton_Eta_Reco_pt'+str(i)+'_cut7')		)
	    Ndata.append( 	 data.Get(channel+'Selection/Lepton_Eta_Reco_pt'+str(i)+'_cut7')		)
 	    NBkg_top.append(  	 Background_Top.Get(channel+'Selection/Lepton_Eta_Reco_pt'+str(i)+'_cut7')	)
	    NBkg_diboson.append( Background_diboson.Get(channel+'Selection/Lepton_Eta_Reco_pt'+str(i)+'_cut7')	)
	    NBkg_w.append(	 Background_W.Get(channel+'Selection/Lepton_Eta_Reco_pt'+str(i)+'_cut7')  	)
	    NBkg_z.append(	 Background_Z.Get(channel+'Selection/Lepton_Eta_Reco_pt'+str(i)+'_cut7')  	)

	RecoBin = [ 0.,  0.1 ,  0.46,  0.66,  0.95,  1.1 ,  1.32,  1.67,  1.87,  2.37,  2.47,  2.57,  3.07,  3.27, 3.62,  3.84,  3.99,  4.28,  4.48,  4.84,  4.94,  5.04,  			      5.4 ,  5.6 ,  5.89,  6.04,  6.26,  6.61,  6.81,  7.31,  7.41,  7.51,  8.01,  8.21,  8.56,  8.78, 8.93,  9.22,  9.42,  9.78,  9.88, 14.92, 15.28, 15.48,				 15.77,	15.92, 16.14, 16.49, 16.69, 17.19, 17.29, 17.39, 17.89, 18.09, 18.44, 18.66, 18.81, 19.1 , 19.3 , 19.66, 19.76, 29.74, 30.1 , 30.3, 30.59, 30.74, 			     30.96, 31.31, 31.51, 32.01, 32.11, 32.21, 32.71, 32.91, 33.26, 33.48, 33.63, 33.92, 34.12, 34.48, 34.58, 49.5 , 49.86, 50.06, 50.35, 50.5, 50.72, 51.07, 				 51.27, 51.77, 51.87, 51.97, 52.47, 52.67, 53.02, 53.24, 53.39, 53.68, 53.88, 54.24, 54.34, 74.2 , 74.56, 74.76, 75.05, 75.2 , 75.42, 75.77, 75.97, 76.47, 			     76.57, 76.67, 77.17, 77.37, 77.72, 77.94, 78.09, 78.38, 78.58, 78.94, 79.04]

        # Make a Clone of hists
        Herror              = TH1F("Herror",                "error",                len(RecoBin)-1, array('d',RecoBin))     # data
        Hdata               = TH1F("Hdata",                 "data",                 len(RecoBin)-1, array('d',RecoBin))     # data
        Hsignal             = TH1F("Hsignal1",              "signal",               len(RecoBin)-1, array('d',RecoBin))   # Signal
        HBackgroundW        = TH1F("NBackgroundW",          "Background_W",         len(RecoBin)-1, array('d',RecoBin))    # W+-
        HBackgroundZ        = TH1F("HBackgroundZ",          "Background_Z",         len(RecoBin)-1, array('d',RecoBin))    # Z+-
        HBackgroundDiboson  = TH1F("HBackgroundDiboson",    "Background_Diboson",   len(RecoBin)-1, array('d',RecoBin))   # diboson
        HBackgroundMultijet = TH1F("HBackgroundMultijet",   "Background_Multijet",  len(RecoBin)-1, array('d',RecoBin))     # MJ
        HBackgroundTop      = TH1F("HBackgroundTop",        "Background_Top",       len(RecoBin)-1, array('d',RecoBin))     # Top
        Hratio1             = TH1F("Hratio1",               "ratio",                len(RecoBin)-1, array('d',RecoBin))     # ratio

	
	 
	      
	N = Ndata[0].GetNbinsX()
	for k in range(0, len(Ndata)):
	    for i in range(0,  N):
		Hdata.SetBinContent(  k*N+i+1,    Ndata[k].GetBinContent(i+1))
		Hdata.SetBinError(    k*N+i+1,    Ndata[k].GetBinError(  i+1))


	for i in range(0, Hdata.GetNbinsX()):
	    print(i+1, Hdata.GetBinContent(i+1))

	for i in range(0, Ndata[0].GetNbinsX()):
            print(i+1, Ndata[0].GetBinContent(i+1))

        for i in range(0, Ndata[5].GetNbinsX()):
            print(i+1, Ndata[5].GetBinContent(i+1))


	

	#axis = Nsignal[0].GetXaxis()
	#array = axis.GetXbins().GetArray()
	
	#for i in range(0, len(array)):
	#    print(array[i])
	#print(array)
	#print(axis.GetXbins().GetArray())	
	#Hist = TH1F("Hist", "Hist", axis.GetNbins(), axis.GetXbins().GetArray())
	#Hist.Draw()

	"""
        Nsignal                 = Signal.Get(channel+'Selection/Lepton_pT_Reco_cut7')                # Signal
        Ndata                   = data.Get(channel+'Selection/Lepton_pT_Reco_cut7')                  # Data

        print("Nombre de bins de MC : ",Nsignal.GetNbinsX())
        
        NBackgroundW            = Background_W.Get(channel+'Selection/Lepton_pT_Reco_cut7')          # background "W"
        NBackgroundZ            = Background_Z.Get(channel+'Selection/Lepton_pT_Reco_cut7')          # background "Z"
        NBackgroundDiboson      = Background_diboson.Get(channel+'Selection/Lepton_pT_Reco_cut7')    # background "diboson"
        NBackgroundTop          = Background_Top.Get(channel+'Selection/Lepton_pT_Reco_cut7')        # background "Top"
        NBackgroundMultijet     = Background_MiltiJet.Get('hist/'+lepton+'Pt')                     # background "Miltijet"

        # Make a Clone of hists
        Hdata               = TH1F("Hdata",                 "data",                 100, 0, 100)    # data
        Hsignal             = TH1F("Hsignal1",              "signal",               100, 0, 100)    # Signal
        HBackgroundW        = TH1F("NBackgroundW",          "Background_W",         100, 0, 100)    # W+-
        HBackgroundZ        = TH1F("HBackgroundZ",          "Background_Z",         100, 0, 100)    # Z+-
        HBackgroundDiboson  = TH1F("HBackgroundDiboson",    "Background_Diboson",   100, 0, 100)    # diboson
        HBackgroundMultijet = TH1F("HBackgroundMultijet",   "Background_Multijet",  100, 0, 100)    # MJ
        HBackgroundTop      = TH1F("HBackgroundTop",        "Background_Top",       100, 0, 100)    # Top
        Hratio1             = TH1F("Hratio1",               "ratio",                100, 0, 100)    # ratio

        i=1
        while i < 101:
            Hdata.SetBinContent(i,                  Ndata.GetBinContent(i))
            Hdata.SetBinError(i,                    Ndata.GetBinError(i))

            Hsignal.SetBinContent(i,                Nsignal.GetBinContent(i))
            #Hsignal.SetBinError(i,                  Nsignal.GetBinError(i))

            HBackgroundW.SetBinContent(i,           NBackgroundW.GetBinContent(i))
            HBackgroundZ.SetBinContent(i,           NBackgroundZ.GetBinContent(i))
            HBackgroundDiboson.SetBinContent(i,     NBackgroundDiboson.GetBinContent(i))
            HBackgroundMultijet.SetBinContent(i,    NBackgroundMultijet.GetBinContent(i))
            HBackgroundTop.SetBinContent(i,         NBackgroundTop.GetBinContent(i))

            Hratio1.SetBinContent(i,                Ndata.GetBinContent(i))
            Hratio1.SetBinError(i,                  Ndata.GetBinError(i))
            i=i+1

        # MC Total
        #Hsignal.SetLineColor(2)
        #Hsignal.SetLineWidth(2)
        #Hsignal.SetLineStyle(2)

        MCTotal = Hsignal.Clone("MCTotal")
        MCTotal.Add(HBackgroundDiboson)
        MCTotal.Add(HBackgroundTop)
        MCTotal.Add(HBackgroundMultijet)
        MCTotal.Add(HBackgroundW)
        MCTotal.Add(HBackgroundZ)
        MCTotal.SetMarkerSize(0)

        # Ratio Plot
        Nratio1 =  Hdata.Clone("Nratio1")

        print("Nombre de bins de data : ",Nratio1.GetNbinsX())
        print("Nombre de bins de MC : ",Hsignal.GetNbinsX())

        # Hist Syle 2, 4, 209, 93, 221
        ColorParameter(Hsignal, 		1001,  155, 1, 1)
        ColorParameter(HBackgroundW, 		1001, 	 2, 1, 1)
        ColorParameter(HBackgroundZ, 		1001, 	 4, 1, 1)
        ColorParameter(HBackgroundDiboson, 	1001,  209, 1, 1)
        ColorParameter(HBackgroundMultijet, 	1001, 	93, 1, 1)
        ColorParameter(HBackgroundTop, 		1001, 	53, 1, 1)

        Hdata.SetLineColor(1)
        Hdata.SetLineWidth(2)
        Hdata.SetMarkerStyle(1)
        Hdata.SetMarkerColor(1)
        Hdata.SetMarkerSize(1)

        Legend = ROOT.TLegend(0.66,0.5,0.94,0.9)
        Legend.AddEntry(Hdata,"data");
        Legend.AddEntry(Hsignal,Indic,"f");
        Legend.AddEntry(HBackgroundZ,"Z #rightarrow ll","f");
        Legend.AddEntry(HBackgroundW,"W^{\pm} #rightarrow l^{\pm}v, BG","f");
        Legend.AddEntry(HBackgroundDiboson,"Diboson","f");
        Legend.AddEntry(HBackgroundMultijet,"Multijet","f");
        Legend.AddEntry(HBackgroundTop,"Top","f");
        Legend.SetBorderSize(0)

        # Tline
        line1 = ROOT.TLine(0,0.95,100,0.95)
        line2 = ROOT.TLine(0,1.05,100,1.05)
        line3 = ROOT.TLine(0,1.,100,1.)
        line1.SetLineStyle(2)
        line2.SetLineStyle(2)
        line3.SetLineStyle(2)

        # TStack
        BackgroundPlot = ROOT.THStack("ss","")
        BackgroundPlot.Add(HBackgroundDiboson)
        BackgroundPlot.Add(HBackgroundTop)
        BackgroundPlot.Add(HBackgroundMultijet)
        BackgroundPlot.Add(HBackgroundZ)
        BackgroundPlot.Add(HBackgroundW)
        BackgroundPlot.Add(Hsignal)


        # Draw
	root.gROOT.SetStyle("ATLAS")
	#gROOT.SetStyle("ATLAS")
        #astyle.SetAtlasStyle()
        c = TCanvas("c", "canvas", 800, 700)
        pad1 = TPad("pad1", "pad1", 0, 0.32, 1, 1.0)
        pad1.SetBottomMargin(0);
        pad1.Draw();
        pad1.SetLogy()
        pad1.cd();
        Hdata.SetStats(0)
        Hdata.SetName("")
        Hdata.SetTitle("")
        Hdata.GetYaxis().SetTitle("Event")
        Hdata.GetYaxis().SetTitleOffset(0.8)
        Hdata.GetYaxis().SetTitleSize(0.06)
        Hdata.GetYaxis().SetLabelSize(0.05)
        Hdata.GetXaxis().SetRangeUser(0,200)
        Hdata.SetMarkerStyle(20)
        Hdata.SetMarkerSize(0.8)
        Hdata.SetMinimum(1.4)
        Hdata.SetMaximum(1000000)
        Hdata.Draw("same")
        BackgroundPlot.Draw("same")
        Hdata.Draw("same")
        Legend.Draw("same")
        astyle.ATLASLabel(0.2, 0.88, "Internal")
        utils.DrawText(0.2, 0.82, Indice)

        c.Update()

        c.cd();
        pad2 = TPad("pad2", "pad2", 0, 0., 1, 0.3)
        pad2.SetTopMargin(0);
        pad2.SetBottomMargin(0.4);
        pad2.Draw();
        pad2.cd();
        Nratio1.GetXaxis().SetRangeUser(0,200)
        Nratio1.GetYaxis().SetRangeUser(0.885,1.115)
        Nratio1.GetXaxis().SetLabelSize(0.1)
        Nratio1.GetYaxis().SetLabelSize(0.1)
        Nratio1.GetXaxis().SetTitleSize(0.1)
        Nratio1.GetYaxis().SetTitleSize(0.1)
        Nratio1.GetYaxis().CenterTitle()
        Nratio1.GetYaxis().SetTitleOffset(0.5)
        Nratio1.GetYaxis().SetTitleSize(0.12)
        Nratio1.GetXaxis().SetTitleSize(0.12)
        Nratio1.GetXaxis().SetTitleOffset(1.2)
        Nratio1.SetTitle("")
        Nratio1.Divide(MCTotal)
        Nratio1.SetLineColor(1)
        Nratio1.SetMarkerStyle(20)
        Nratio1.SetMarkerSize(0.6)
        Nratio1.SetLineWidth(2)
        Nratio1.SetStats(0)
        Nratio1.GetXaxis().SetTitle("p_{T}^{lepton} [GeV]")
        Nratio1.GetYaxis().SetTitle("Data/MC")
        Nratio1.Draw("P")
        line1.Draw("same")
        line2.Draw("same")
        line3.Draw("same")
        c.Print("Output/Backgrounds/BackgroundPlot_ptLepton_"+channel+"_"+Energy+".pdf")

	"""




