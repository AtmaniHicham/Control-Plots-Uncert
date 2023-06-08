#!/usr/bin/env python
# -*-coding:Latin-1 -*

from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TLatex, TChain
from array import array
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TH1
import sys
import matplotlib.pyplot as plt
import numpy as np
from numpy import savetxt
import ROOT as root
import ROOT
from math import *
from atlasify import atlasify
plt.rcParams.update({'font.size': 14})


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


def histtoarrayError(hist):
    list1 = []
    for i in range(0, hist.GetNbinsX()):
        list1.append(hist.GetBinError(i+1))
    return np.array(list1)
    
def histtoarray(hist):
    vector = []
    for i in range(0, hist.GetNbinsX()):
        vector.append(hist.GetBinContent(i+1))
    array = np.array(vector)
    return array


class UncertClass:
    """Classe représentant une personne"""

    def __init__(self):
        """Constructeur de notre classe"""


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def MJUncertainties(self, hist, hist_shape_up, hist_ExtrapErr_up, hist_uTSliceErr_up):
        print(hist.GetNbinsX(), hist_shape_up.GetNbinsX(),
              hist_ExtrapErr_up.GetNbinsX(), hist_uTSliceErr_up.GetNbinsX())
        shape_up = hist_shape_up.Clone("shape_up")
        ExtrapErr_up = hist_ExtrapErr_up.Clone("ExtrapErr_up")
        uTSliceErr_up = hist_uTSliceErr_up.Clone("uTSliceErr_up")

        TotalMJ_Uncer = []

        for i in range(0, hist.GetNbinsX()):
            shape_up.SetBinContent(
                i+1,   hist_shape_up.GetBinContent(i+1) - hist.GetBinContent(i+1))
            ExtrapErr_up.SetBinContent(
                i+1,   hist_ExtrapErr_up.GetBinContent(i+1) - hist.GetBinContent(i+1))
            uTSliceErr_up.SetBinContent(
                i+1,   hist_uTSliceErr_up.GetBinContent(i+1) - hist.GetBinContent(i+1))

        for i in range(0, hist.GetNbinsX()):
            TotalMJ_Uncer.append(sqrt(pow(hist.GetBinError(i+1), 2) + pow(shape_up.GetBinContent(
                i+1), 2) + pow(ExtrapErr_up.GetBinContent(i+1), 2) + pow(uTSliceErr_up.GetBinContent(i+1), 2)))

        return TotalMJ_Uncer

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ReadHistogramDataError(self, Data, Indice, channel, lepton, var, multi, Energy):

        data_hist1 = histtoarrayError(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7"))
        data_hist2 = histtoarrayError(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7"))
        data_hist3 = histtoarrayError(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7"))
        data_hist4 = histtoarrayError(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7"))
        data_hist5 = histtoarrayError(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7"))
        data_hist6 = histtoarrayError(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7"))

        listFinal = np.concatenate((data_hist1, data_hist2, data_hist3, data_hist4, data_hist5, data_hist6))

        return listFinal

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ReadHistogramSignalError(self, Data, Indice, channel, lepton, var, multi, Energy):

        data_hist1 = histtoarrayError(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7"))
        data_hist2 = histtoarrayError(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7"))
        data_hist3 = histtoarrayError(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7"))
        data_hist4 = histtoarrayError(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7"))
        data_hist5 = histtoarrayError(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7"))
        data_hist6 = histtoarrayError(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7"))

        listFinal = np.concatenate((data_hist1, data_hist2, data_hist3, data_hist4, data_hist5, data_hist6))

        return listFinal
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ReadHistogramData(self, Data, Indice, channel, lepton, var, multi, Energy):

        data_hist1 = histtoarray(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7"))
        data_hist2 = histtoarray(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7"))
        data_hist3 = histtoarray(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7"))
        data_hist4 = histtoarray(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7"))
        data_hist5 = histtoarray(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7"))
        data_hist6 = histtoarray(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7"))

        listFinal = np.concatenate((data_hist1, data_hist2, data_hist3, data_hist4, data_hist5, data_hist6))

        return listFinal

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ReadHistogramSignal(self, Data, Indice, channel, lepton, var, multi, Energy):

        data_hist1 = histtoarray(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7"))
        data_hist2 = histtoarray(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7"))
        data_hist3 = histtoarray(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7"))
        data_hist4 = histtoarray(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7"))
        data_hist5 = histtoarray(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7"))
        data_hist6 = histtoarray(Data.Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7"))

        listFinal = np.concatenate((data_hist1, data_hist2, data_hist3, data_hist4, data_hist5, data_hist6))

        return listFinal

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ReadHistogramCalibratiion(self, Signal, Indice, channel, lepton, var, multi, Energy):

        data_hist1 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7"))
        data_hist2 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7"))
        data_hist3 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7"))
        data_hist4 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7"))
        data_hist5 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7"))
        data_hist6 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7"))

        CalibSystFiles = []
        CalibSystVariation1 = []
        CalibSystVariation2 = []
        CalibSystVariation3 = []
        CalibSystVariation4 = []
        CalibSystVariation5 = []
        CalibSystVariation6 = []

        for i in range(1, 25):
            CalibSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w'+channel[1::]+'_MC_'+str(Energy)+'/ElCalibVar/merge/mc16_'+str(Energy)+'.varscaleDownbin'+str(i)+'.root'))
        for i in range(1, 25):
            CalibSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w'+channel[1::]+'_MC_'+str(Energy)+'/ElCalibVar/merge/mc16_'+str(Energy)+'.varcDownbin'+str(i)+'.root'))


        for i in range(0, len(CalibSystFiles)):
            print(CalibSystFiles[i])
            CalibSystVariation1.append(histtoarray(CalibSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7")))
            CalibSystVariation2.append(histtoarray(CalibSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7")))
            CalibSystVariation3.append(histtoarray(CalibSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7")))
            CalibSystVariation4.append(histtoarray(CalibSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7")))
            CalibSystVariation5.append(histtoarray(CalibSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7")))
            CalibSystVariation6.append(histtoarray(CalibSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7")))

        for i in range(0, len(CalibSystVariation1)):
            CalibSystVariation1[i] = CalibSystVariation1[i] - data_hist1
            CalibSystVariation2[i] = CalibSystVariation2[i] - data_hist2
            CalibSystVariation3[i] = CalibSystVariation3[i] - data_hist3
            CalibSystVariation4[i] = CalibSystVariation4[i] - data_hist4
            CalibSystVariation5[i] = CalibSystVariation5[i] - data_hist5
            CalibSystVariation6[i] = CalibSystVariation6[i] - data_hist6

        CalibSystVariation1[0] = CalibSystVariation1[0]*CalibSystVariation1[0]
        CalibSystVariation2[0] = CalibSystVariation2[0]*CalibSystVariation2[0]
        CalibSystVariation3[0] = CalibSystVariation3[0]*CalibSystVariation3[0]
        CalibSystVariation4[0] = CalibSystVariation4[0]*CalibSystVariation4[0]
        CalibSystVariation5[0] = CalibSystVariation5[0]*CalibSystVariation5[0]
        CalibSystVariation6[0] = CalibSystVariation6[0]*CalibSystVariation6[0]

        for i in range(1, len(CalibSystVariation1)):
            CalibSystVariation1[0] = CalibSystVariation1[0] + CalibSystVariation1[i]*CalibSystVariation1[i]
            CalibSystVariation2[0] = CalibSystVariation2[0] + CalibSystVariation2[i]*CalibSystVariation2[i]
            CalibSystVariation3[0] = CalibSystVariation3[0] + CalibSystVariation3[i]*CalibSystVariation3[i]
            CalibSystVariation4[0] = CalibSystVariation4[0] + CalibSystVariation4[i]*CalibSystVariation4[i]
            CalibSystVariation5[0] = CalibSystVariation5[0] + CalibSystVariation5[i]*CalibSystVariation5[i]
            CalibSystVariation6[0] = CalibSystVariation6[0] + CalibSystVariation6[i]*CalibSystVariation6[i]


        listFinal = np.concatenate((CalibSystVariation1[0], CalibSystVariation2[0], CalibSystVariation3[0], CalibSystVariation4[0], CalibSystVariation5[0], CalibSystVariation6[0]))
        print(len(listFinal))
        return listFinal
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ReadHistogramCalibratiionMuons(self, Signal, Indice, channel, lepton, var, multi, Energy):

        data_hist1 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7"))
        data_hist2 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7"))
        data_hist3 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7"))
        data_hist4 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7"))
        data_hist5 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7"))
        data_hist6 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7"))

        CalibSystFiles = []
        CalibSystVariation1 = []
        CalibSystVariation2 = []
        CalibSystVariation3 = []
        CalibSystVariation4 = []
        CalibSystVariation5 = []
        CalibSystVariation6 = []

        CalibSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channel[1:] + '_MC_'+str(Energy)+'/MuCalibVar/merge/MC_varMUON_ID_1down.root'))
        CalibSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channel[1:] + '_MC_'+str(Energy)+'/MuCalibVar/merge/MC_varMUON_MS_1down.root'))
        CalibSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channel[1:] + '_MC_'+str(Energy)+'/MuCalibVar/merge/MC_varMUON_SCALE_1down.root'))
        CalibSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channel[1:] + '_MC_'+str(Energy)+'/MuCalibVar/merge/MC_varSagittaBiasOffsetDown.root'))

        for i in range(1, 25):
            CalibSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channel[1:] + '_MC_'+str(Energy)+'/MuCalibVar/merge/mc16_'+str(Energy)+'.varSagittaBiasstatDownbin'+str(i)+'.root'))


        for i in range(0, len(CalibSystFiles)):
            print(CalibSystFiles[i])
            CalibSystVariation1.append(histtoarray(CalibSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7")))
            CalibSystVariation2.append(histtoarray(CalibSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7")))
            CalibSystVariation3.append(histtoarray(CalibSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7")))
            CalibSystVariation4.append(histtoarray(CalibSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7")))
            CalibSystVariation5.append(histtoarray(CalibSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7")))
            CalibSystVariation6.append(histtoarray(CalibSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7")))

        for i in range(0, len(CalibSystVariation1)):
            CalibSystVariation1[i] = CalibSystVariation1[i] - data_hist1
            CalibSystVariation2[i] = CalibSystVariation2[i] - data_hist2
            CalibSystVariation3[i] = CalibSystVariation3[i] - data_hist3
            CalibSystVariation4[i] = CalibSystVariation4[i] - data_hist4
            CalibSystVariation5[i] = CalibSystVariation5[i] - data_hist5
            CalibSystVariation6[i] = CalibSystVariation6[i] - data_hist6

        CalibSystVariation1[0] = CalibSystVariation1[0]*CalibSystVariation1[0]
        CalibSystVariation2[0] = CalibSystVariation2[0]*CalibSystVariation2[0]
        CalibSystVariation3[0] = CalibSystVariation3[0]*CalibSystVariation3[0]
        CalibSystVariation4[0] = CalibSystVariation4[0]*CalibSystVariation4[0]
        CalibSystVariation5[0] = CalibSystVariation5[0]*CalibSystVariation5[0]
        CalibSystVariation6[0] = CalibSystVariation6[0]*CalibSystVariation6[0]

        for i in range(1, len(CalibSystVariation1)):
            CalibSystVariation1[0] = CalibSystVariation1[0] + CalibSystVariation1[i]*CalibSystVariation1[i]
            CalibSystVariation2[0] = CalibSystVariation2[0] + CalibSystVariation2[i]*CalibSystVariation2[i]
            CalibSystVariation3[0] = CalibSystVariation3[0] + CalibSystVariation3[i]*CalibSystVariation3[i]
            CalibSystVariation4[0] = CalibSystVariation4[0] + CalibSystVariation4[i]*CalibSystVariation4[i]
            CalibSystVariation5[0] = CalibSystVariation5[0] + CalibSystVariation5[i]*CalibSystVariation5[i]
            CalibSystVariation6[0] = CalibSystVariation6[0] + CalibSystVariation6[i]*CalibSystVariation6[i]


        listFinal = np.concatenate((CalibSystVariation1[0], CalibSystVariation2[0], CalibSystVariation3[0], CalibSystVariation4[0], CalibSystVariation5[0], CalibSystVariation6[0]))
        print(len(listFinal))
        return listFinal
        
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ReadHistogramRecoil(self, Signal, Indice, channel, lepton, var, multi, Energy):

        data_hist1 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7"))
        data_hist2 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7"))
        data_hist3 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7"))
        data_hist4 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7"))
        data_hist5 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7"))
        data_hist6 = histtoarray(Signal.Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7"))

        RecoilSystFiles = []
        RecoilSystVariation1 = []
        RecoilSystVariation2 = []
        RecoilSystVariation3 = []
        RecoilSystVariation4 = []
        RecoilSystVariation5 = []
        RecoilSystVariation6 = []

        if(Energy == "5TeV"):
            RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w'+channel[1::]+'_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESPONSE_EXTSYS_DOWNbin1.root'))
            RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w'+channel[1::]+'_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESOLUTION_EXTSYS_DOWNbin1.root'))
            RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w'+channel[1::]+'_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESPONSE_SYS_DOWNbin1.root'))

            for i in range(3, 20):  # 1, 20
                RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w'+channel[1::]+'_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESPONSE_STAT0_DOWNbin'+str(i)+'.root'))
                RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w'+channel[1::]+'_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESPONSE_STAT1_DOWNbin'+str(i)+'.root'))  # error
            for i in range(1, 13):  # 1, 13
                RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w'+channel[1::]+'_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESOLUTION_STAT0_DOWNbin'+str(i)+'.root'))
                RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w'+channel[1::]+'_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESOLUTION_STAT1_DOWNbin'+str(i)+'.root'))

        if(Energy == "13TeV"):
            RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w'+channel[1::]+'_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESPONSE_EXTSYS_DOWNbin1.root'))
            RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w'+channel[1::]+'_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESOLUTION_EXTSYS_DOWNbin1.root'))
            RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w'+channel[1::]+'_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESPONSE_SYS_DOWNbin1.root'))

            for i in range(1, 10):
                RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w'+channel[1::]+'_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESPONSE_STAT0_DOWNbin'+str(i)+'.root'))
                RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w'+channel[1::]+'_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESPONSE_STAT1_DOWNbin'+str(i)+'.root'))
            for i in range(1, 15):
                RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w'+channel[1::]+'_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESOLUTION_STAT0_DOWNbin'+str(i)+'.root'))
                RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w'+channel[1::]+'_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESOLUTION_STAT1_DOWNbin'+str(i)+'.root'))

        for i in range(0, len(RecoilSystFiles)):
            RecoilSystVariation1.append(histtoarray(RecoilSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7")))
            RecoilSystVariation2.append(histtoarray(RecoilSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7")))
            RecoilSystVariation3.append(histtoarray(RecoilSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7")))
            RecoilSystVariation4.append(histtoarray(RecoilSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7")))
            RecoilSystVariation5.append(histtoarray(RecoilSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7")))
            RecoilSystVariation6.append(histtoarray(RecoilSystFiles[i].Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7")))

        for i in range(0, len(RecoilSystVariation1)):
            RecoilSystVariation1[i] = RecoilSystVariation1[i] - data_hist1
            RecoilSystVariation2[i] = RecoilSystVariation2[i] - data_hist2
            RecoilSystVariation3[i] = RecoilSystVariation3[i] - data_hist3
            RecoilSystVariation4[i] = RecoilSystVariation4[i] - data_hist4
            RecoilSystVariation5[i] = RecoilSystVariation5[i] - data_hist5
            RecoilSystVariation6[i] = RecoilSystVariation6[i] - data_hist6

        RecoilSystVariation1[0] = RecoilSystVariation1[0]*RecoilSystVariation1[0]
        RecoilSystVariation2[0] = RecoilSystVariation2[0]*RecoilSystVariation2[0]
        RecoilSystVariation3[0] = RecoilSystVariation3[0]*RecoilSystVariation3[0]
        RecoilSystVariation4[0] = RecoilSystVariation4[0]*RecoilSystVariation4[0]
        RecoilSystVariation5[0] = RecoilSystVariation5[0]*RecoilSystVariation5[0]
        RecoilSystVariation6[0] = RecoilSystVariation6[0]*RecoilSystVariation6[0]

        for i in range(1, len(RecoilSystVariation1)):
            RecoilSystVariation1[0] = RecoilSystVariation1[0] + RecoilSystVariation1[i]*RecoilSystVariation1[i]
            RecoilSystVariation2[0] = RecoilSystVariation2[0] + RecoilSystVariation2[i]*RecoilSystVariation2[i]
            RecoilSystVariation3[0] = RecoilSystVariation3[0] + RecoilSystVariation3[i]*RecoilSystVariation3[i]
            RecoilSystVariation4[0] = RecoilSystVariation4[0] + RecoilSystVariation4[i]*RecoilSystVariation4[i]
            RecoilSystVariation5[0] = RecoilSystVariation5[0] + RecoilSystVariation5[i]*RecoilSystVariation5[i]
            RecoilSystVariation6[0] = RecoilSystVariation6[0] + RecoilSystVariation6[i]*RecoilSystVariation6[i]



        listFinal = np.concatenate((RecoilSystVariation1[0], RecoilSystVariation2[0], RecoilSystVariation3[0], RecoilSystVariation4[0], RecoilSystVariation5[0], RecoilSystVariation6[0]))
        return listFinal

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ReadHistogramMJStat(self, MJFile, Indice, channel, lepton, var, multi, Energy):
        if sys.argv[5] == "el":
            ETA_MJHistogram  = histtoarrayError(MJFile.Get("hist/elEta"))
            ElPt_MJHistogram = histtoarrayError(MJFile.Get("hist/elPt"))
        if sys.argv[5] == "mu":
            ETA_MJHistogram  = histtoarrayError(MJFile.Get("hist/muEta"))
            ElPt_MJHistogram = histtoarrayError(MJFile.Get("hist/muPt"))

        sum1 = ElPt_MJHistogram[25] + ElPt_MJHistogram[26] + ElPt_MJHistogram[27] + ElPt_MJHistogram[28] + ElPt_MJHistogram[29]
        sum2 = ElPt_MJHistogram[30] + ElPt_MJHistogram[31] + ElPt_MJHistogram[32] + ElPt_MJHistogram[33] + ElPt_MJHistogram[34]
        sum3 = ElPt_MJHistogram[35] + ElPt_MJHistogram[36] + ElPt_MJHistogram[37] + ElPt_MJHistogram[38] + ElPt_MJHistogram[39]
        sum4 = ElPt_MJHistogram[40] + ElPt_MJHistogram[41] + ElPt_MJHistogram[42] + ElPt_MJHistogram[43] + ElPt_MJHistogram[44]
        sum5 = ElPt_MJHistogram[45] + ElPt_MJHistogram[46] + ElPt_MJHistogram[47] + ElPt_MJHistogram[48] + ElPt_MJHistogram[49]
        sum6 = 0

        for i in range(50, len(ElPt_MJHistogram)):
            sum6 = sum6 + ElPt_MJHistogram[i]

        sumTotal = sum1 + sum2 + sum3 + sum4 + sum5 + sum6

        ETA1_MJHistogram = (sum1/sumTotal)*ETA_MJHistogram
        ETA2_MJHistogram = (sum2/sumTotal)*ETA_MJHistogram
        ETA3_MJHistogram = (sum3/sumTotal)*ETA_MJHistogram
        ETA4_MJHistogram = (sum4/sumTotal)*ETA_MJHistogram
        ETA5_MJHistogram = (sum5/sumTotal)*ETA_MJHistogram
        ETA6_MJHistogram = (sum6/sumTotal)*ETA_MJHistogram

        ETA1_MJHistogram = ETA1_MJHistogram[ int(len(ETA1_MJHistogram)/2) :: ]
        ETA2_MJHistogram = ETA2_MJHistogram[ int(len(ETA2_MJHistogram)/2) :: ]
        ETA3_MJHistogram = ETA3_MJHistogram[ int(len(ETA3_MJHistogram)/2) :: ]
        ETA4_MJHistogram = ETA4_MJHistogram[ int(len(ETA4_MJHistogram)/2) :: ]
        ETA5_MJHistogram = ETA5_MJHistogram[ int(len(ETA5_MJHistogram)/2) :: ]
        ETA6_MJHistogram = ETA6_MJHistogram[ int(len(ETA6_MJHistogram)/2) :: ]

        listFinal = np.concatenate((ETA1_MJHistogram, ETA2_MJHistogram, ETA3_MJHistogram, ETA4_MJHistogram, ETA5_MJHistogram, ETA6_MJHistogram))
        return listFinal

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ReadHistogramMJ(self, MJFile, Indice, channel, lepton, var, multi, Energy):
        if sys.argv[5] == "el":
            ETA_MJHistogram  = histtoarray(MJFile.Get("hist/elEta"))
            ElPt_MJHistogram = histtoarray(MJFile.Get("hist/elPt"))
        if sys.argv[5] == "mu":
            ETA_MJHistogram  = histtoarray(MJFile.Get("hist/muEta"))
            ElPt_MJHistogram = histtoarray(MJFile.Get("hist/muPt"))

        sum1 = ElPt_MJHistogram[25] + ElPt_MJHistogram[26] + ElPt_MJHistogram[27] + ElPt_MJHistogram[28] + ElPt_MJHistogram[29]
        sum2 = ElPt_MJHistogram[30] + ElPt_MJHistogram[31] + ElPt_MJHistogram[32] + ElPt_MJHistogram[33] + ElPt_MJHistogram[34]
        sum3 = ElPt_MJHistogram[35] + ElPt_MJHistogram[36] + ElPt_MJHistogram[37] + ElPt_MJHistogram[38] + ElPt_MJHistogram[39]
        sum4 = ElPt_MJHistogram[40] + ElPt_MJHistogram[41] + ElPt_MJHistogram[42] + ElPt_MJHistogram[43] + ElPt_MJHistogram[44]
        sum5 = ElPt_MJHistogram[45] + ElPt_MJHistogram[46] + ElPt_MJHistogram[47] + ElPt_MJHistogram[48] + ElPt_MJHistogram[49]
        sum6 = 0

        for i in range(50, len(ElPt_MJHistogram)):
            sum6 = sum6 + ElPt_MJHistogram[i]

        sumTotal = sum1 + sum2 + sum3 + sum4 + sum5 + sum6

        ETA1_MJHistogram = (sum1/sumTotal)*ETA_MJHistogram
        ETA2_MJHistogram = (sum2/sumTotal)*ETA_MJHistogram
        ETA3_MJHistogram = (sum3/sumTotal)*ETA_MJHistogram
        ETA4_MJHistogram = (sum4/sumTotal)*ETA_MJHistogram
        ETA5_MJHistogram = (sum5/sumTotal)*ETA_MJHistogram
        ETA6_MJHistogram = (sum6/sumTotal)*ETA_MJHistogram

        ETA1_MJHistogram = ETA1_MJHistogram[ int(len(ETA1_MJHistogram)/2) :: ]
        ETA2_MJHistogram = ETA2_MJHistogram[ int(len(ETA2_MJHistogram)/2) :: ]
        ETA3_MJHistogram = ETA3_MJHistogram[ int(len(ETA3_MJHistogram)/2) :: ]
        ETA4_MJHistogram = ETA4_MJHistogram[ int(len(ETA4_MJHistogram)/2) :: ]
        ETA5_MJHistogram = ETA5_MJHistogram[ int(len(ETA5_MJHistogram)/2) :: ]
        ETA6_MJHistogram = ETA6_MJHistogram[ int(len(ETA6_MJHistogram)/2) :: ]

        listFinal = np.concatenate((ETA1_MJHistogram, ETA2_MJHistogram, ETA3_MJHistogram, ETA4_MJHistogram, ETA5_MJHistogram, ETA6_MJHistogram))
        return listFinal

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ReadHistogramMJShape(self, MJFile, Indice, channel, lepton, var, multi, Energy):

        if sys.argv[5] == "el":
            ETA_MJHistogram  = histtoarray(MJFile.Get("shape_uphist/elEta"))
            ElPt_MJHistogram = histtoarray(MJFile.Get("shape_uphist/elPt"))
        if sys.argv[5] == "mu":
            ETA_MJHistogram  = histtoarray(MJFile.Get("shape_uphist/muEta"))
            ElPt_MJHistogram = histtoarray(MJFile.Get("shape_uphist/muPt"))


        sum1 = ElPt_MJHistogram[25] + ElPt_MJHistogram[26] + ElPt_MJHistogram[27] + ElPt_MJHistogram[28] + ElPt_MJHistogram[29]
        sum2 = ElPt_MJHistogram[30] + ElPt_MJHistogram[31] + ElPt_MJHistogram[32] + ElPt_MJHistogram[33] + ElPt_MJHistogram[34]
        sum3 = ElPt_MJHistogram[35] + ElPt_MJHistogram[36] + ElPt_MJHistogram[37] + ElPt_MJHistogram[38] + ElPt_MJHistogram[39]
        sum4 = ElPt_MJHistogram[40] + ElPt_MJHistogram[41] + ElPt_MJHistogram[42] + ElPt_MJHistogram[43] + ElPt_MJHistogram[44]
        sum5 = ElPt_MJHistogram[45] + ElPt_MJHistogram[46] + ElPt_MJHistogram[47] + ElPt_MJHistogram[48] + ElPt_MJHistogram[49]
        sum6 = 0

        for i in range(50, len(ElPt_MJHistogram)):
            sum6 = sum6 + ElPt_MJHistogram[i]

        sumTotal = sum1 + sum2 + sum3 + sum4 + sum5 + sum6

        ETA1_MJHistogram = (sum1/sumTotal)*ETA_MJHistogram
        ETA2_MJHistogram = (sum2/sumTotal)*ETA_MJHistogram
        ETA3_MJHistogram = (sum3/sumTotal)*ETA_MJHistogram
        ETA4_MJHistogram = (sum4/sumTotal)*ETA_MJHistogram
        ETA5_MJHistogram = (sum5/sumTotal)*ETA_MJHistogram
        ETA6_MJHistogram = (sum6/sumTotal)*ETA_MJHistogram

        ETA1_MJHistogram = ETA1_MJHistogram[ int(len(ETA1_MJHistogram)/2) :: ]
        ETA2_MJHistogram = ETA2_MJHistogram[ int(len(ETA2_MJHistogram)/2) :: ]
        ETA3_MJHistogram = ETA3_MJHistogram[ int(len(ETA3_MJHistogram)/2) :: ]
        ETA4_MJHistogram = ETA4_MJHistogram[ int(len(ETA4_MJHistogram)/2) :: ]
        ETA5_MJHistogram = ETA5_MJHistogram[ int(len(ETA5_MJHistogram)/2) :: ]
        ETA6_MJHistogram = ETA6_MJHistogram[ int(len(ETA6_MJHistogram)/2) :: ]

        listFinal = np.concatenate((ETA1_MJHistogram, ETA2_MJHistogram, ETA3_MJHistogram, ETA4_MJHistogram, ETA5_MJHistogram, ETA6_MJHistogram))
        return listFinal
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ReadHistogramMJExtrap(self, MJFile, Indice, channel, lepton, var, multi, Energy):

        if sys.argv[5] == "el":
            ETA_MJHistogram  = histtoarray(MJFile.Get("ExtrapErr_uphist/elEta"))
            ElPt_MJHistogram = histtoarray(MJFile.Get("ExtrapErr_uphist/elPt"))
        if sys.argv[5] == "mu":
            ETA_MJHistogram  = histtoarray(MJFile.Get("ExtrapErr_uphist/muEta"))
            ElPt_MJHistogram = histtoarray(MJFile.Get("ExtrapErr_uphist/muPt"))


        sum1 = ElPt_MJHistogram[25] + ElPt_MJHistogram[26] + ElPt_MJHistogram[27] + ElPt_MJHistogram[28] + ElPt_MJHistogram[29]
        sum2 = ElPt_MJHistogram[30] + ElPt_MJHistogram[31] + ElPt_MJHistogram[32] + ElPt_MJHistogram[33] + ElPt_MJHistogram[34]
        sum3 = ElPt_MJHistogram[35] + ElPt_MJHistogram[36] + ElPt_MJHistogram[37] + ElPt_MJHistogram[38] + ElPt_MJHistogram[39]
        sum4 = ElPt_MJHistogram[40] + ElPt_MJHistogram[41] + ElPt_MJHistogram[42] + ElPt_MJHistogram[43] + ElPt_MJHistogram[44]
        sum5 = ElPt_MJHistogram[45] + ElPt_MJHistogram[46] + ElPt_MJHistogram[47] + ElPt_MJHistogram[48] + ElPt_MJHistogram[49]
        sum6 = 0

        for i in range(50, len(ElPt_MJHistogram)):
            sum6 = sum6 + ElPt_MJHistogram[i]

        sumTotal = sum1 + sum2 + sum3 + sum4 + sum5 + sum6

        ETA1_MJHistogram = (sum1/sumTotal)*ETA_MJHistogram
        ETA2_MJHistogram = (sum2/sumTotal)*ETA_MJHistogram
        ETA3_MJHistogram = (sum3/sumTotal)*ETA_MJHistogram
        ETA4_MJHistogram = (sum4/sumTotal)*ETA_MJHistogram
        ETA5_MJHistogram = (sum5/sumTotal)*ETA_MJHistogram
        ETA6_MJHistogram = (sum6/sumTotal)*ETA_MJHistogram

        ETA1_MJHistogram = ETA1_MJHistogram[ int(len(ETA1_MJHistogram)/2) :: ]
        ETA2_MJHistogram = ETA2_MJHistogram[ int(len(ETA2_MJHistogram)/2) :: ]
        ETA3_MJHistogram = ETA3_MJHistogram[ int(len(ETA3_MJHistogram)/2) :: ]
        ETA4_MJHistogram = ETA4_MJHistogram[ int(len(ETA4_MJHistogram)/2) :: ]
        ETA5_MJHistogram = ETA5_MJHistogram[ int(len(ETA5_MJHistogram)/2) :: ]
        ETA6_MJHistogram = ETA6_MJHistogram[ int(len(ETA6_MJHistogram)/2) :: ]

        listFinal = np.concatenate((ETA1_MJHistogram, ETA2_MJHistogram, ETA3_MJHistogram, ETA4_MJHistogram, ETA5_MJHistogram, ETA6_MJHistogram))
        return listFinal

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ReadHistogramMJuTSlice(self, MJFile, Indice, channel, lepton, var, multi, Energy):

        if sys.argv[5] == "el":
            ETA_MJHistogram  = histtoarray(MJFile.Get("uTSliceErr_uphist/elEta"))
            ElPt_MJHistogram = histtoarray(MJFile.Get("uTSliceErr_uphist/elPt"))
        if sys.argv[5] == "mu":
            ETA_MJHistogram  = histtoarray(MJFile.Get("uTSliceErr_uphist/muEta"))
            ElPt_MJHistogram = histtoarray(MJFile.Get("uTSliceErr_uphist/muPt"))

        sum1 = ElPt_MJHistogram[25] + ElPt_MJHistogram[26] + ElPt_MJHistogram[27] + ElPt_MJHistogram[28] + ElPt_MJHistogram[29]
        sum2 = ElPt_MJHistogram[30] + ElPt_MJHistogram[31] + ElPt_MJHistogram[32] + ElPt_MJHistogram[33] + ElPt_MJHistogram[34]
        sum3 = ElPt_MJHistogram[35] + ElPt_MJHistogram[36] + ElPt_MJHistogram[37] + ElPt_MJHistogram[38] + ElPt_MJHistogram[39]
        sum4 = ElPt_MJHistogram[40] + ElPt_MJHistogram[41] + ElPt_MJHistogram[42] + ElPt_MJHistogram[43] + ElPt_MJHistogram[44]
        sum5 = ElPt_MJHistogram[45] + ElPt_MJHistogram[46] + ElPt_MJHistogram[47] + ElPt_MJHistogram[48] + ElPt_MJHistogram[49]
        sum6 = 0

        for i in range(50, len(ElPt_MJHistogram)):
            sum6 = sum6 + ElPt_MJHistogram[i]

        sumTotal = sum1 + sum2 + sum3 + sum4 + sum5 + sum6

        ETA1_MJHistogram = (sum1/sumTotal)*ETA_MJHistogram
        ETA2_MJHistogram = (sum2/sumTotal)*ETA_MJHistogram
        ETA3_MJHistogram = (sum3/sumTotal)*ETA_MJHistogram
        ETA4_MJHistogram = (sum4/sumTotal)*ETA_MJHistogram
        ETA5_MJHistogram = (sum5/sumTotal)*ETA_MJHistogram
        ETA6_MJHistogram = (sum6/sumTotal)*ETA_MJHistogram

        ETA1_MJHistogram = ETA1_MJHistogram[ int(len(ETA1_MJHistogram)/2) :: ]
        ETA2_MJHistogram = ETA2_MJHistogram[ int(len(ETA2_MJHistogram)/2) :: ]
        ETA3_MJHistogram = ETA3_MJHistogram[ int(len(ETA3_MJHistogram)/2) :: ]
        ETA4_MJHistogram = ETA4_MJHistogram[ int(len(ETA4_MJHistogram)/2) :: ]
        ETA5_MJHistogram = ETA5_MJHistogram[ int(len(ETA5_MJHistogram)/2) :: ]
        ETA6_MJHistogram = ETA6_MJHistogram[ int(len(ETA6_MJHistogram)/2) :: ]

        listFinal = np.concatenate((ETA1_MJHistogram, ETA2_MJHistogram, ETA3_MJHistogram, ETA4_MJHistogram, ETA5_MJHistogram, ETA6_MJHistogram))
        return listFinal

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def MJHistUncertainties(self, MJBackgrodHist, MJBackgrodShape, MJBackgrodExtra, MJBackgroduTSli):

        MJBackgrodShape = MJBackgrodShape - MJBackgrodHist
        MJBackgrodExtra = MJBackgrodExtra - MJBackgrodHist
        MJBackgroduTSli = MJBackgroduTSli - MJBackgrodHist

        UncertainTotal  = MJBackgrodShape*MJBackgrodShape + MJBackgrodExtra*MJBackgrodExtra + MJBackgroduTSli*MJBackgroduTSli
        print(UncertainTotal)
        return UncertainTotal
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ReadHistogramSF(self, Signal, Signal_Sf, Indice, channel, lepton, var, multi, Energy):

        # HistVariation:
        pT1Version1 = []
        pT1Version2 = []
        pT1Version3 = []
        pT1Version4 = []
        pT1Version5 = []
        pT1Version6 = []
        DireName    = channel + "Selection_WeightVariations"
        directory   = Signal_Sf.GetDirectory(DireName)

        for key in directory.GetListOfKeys():
            hist = key.ReadObj()
            if (hist.ClassName() == 'TH1D' and (hist.GetName()).find("Lepton_Eta_Reco") != -1 and (hist.GetName()).find("_cut7") != -1 and (hist.GetName()).find("up") == -1):
                if ( (hist.GetName()).find("pt1") != -1 ):
                    pT1Version1.append( histtoarray(hist)*histtoarray(hist) )            
                if ( (hist.GetName()).find("pt2") != -1 ):
                    pT1Version2.append( histtoarray(hist)*histtoarray(hist) ) 
                if ( (hist.GetName()).find("pt3") != -1 ):
                    pT1Version3.append( histtoarray(hist)*histtoarray(hist) ) 
                if ( (hist.GetName()).find("pt4") != -1 ):
                    pT1Version4.append( histtoarray(hist)*histtoarray(hist) ) 
                if ( (hist.GetName()).find("pt5") != -1 ):
                    pT1Version5.append( histtoarray(hist)*histtoarray(hist) ) 
                if ( (hist.GetName()).find("pt6") != -1 ):
                    pT1Version6.append( histtoarray(hist)*histtoarray(hist) )

        for i in range(1, len(pT1Version1)):
            pT1Version1[0] = pT1Version1[0] + pT1Version1[i]
            pT1Version2[0] = pT1Version2[0] + pT1Version2[i]
            pT1Version3[0] = pT1Version3[0] + pT1Version3[i]
            pT1Version4[0] = pT1Version4[0] + pT1Version4[i]
            pT1Version5[0] = pT1Version5[0] + pT1Version5[i]
            pT1Version6[0] = pT1Version6[0] + pT1Version6[i]

        listFinal = np.concatenate((pT1Version1[0], pT1Version2[0], pT1Version3[0], pT1Version4[0], pT1Version5[0], pT1Version6[0]))
        return listFinal

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def UncertSF(self, data, Signal, Signal_Sf, Indice, channel, lepton, var, multi, Energy):
        # HistVariation:
        IsoVersion1 = []
        DireName = channel + "Selection_WeightVariations"
        directory = Signal_Sf.GetDirectory(DireName)

        for key in directory.GetListOfKeys():
            hist = key.ReadObj()
            if (hist.ClassName() == 'TH1D' and (hist.GetName()).find("Lepton_"+var+"_Reco_cut7") != -1 and (hist.GetName()).find("up") == -1):
                IsoVersion1.append(histtoarray(hist)*histtoarray(hist))

        for i in range(1, len(IsoVersion1)):
            IsoVersion1[0] = IsoVersion1[0] + IsoVersion1[i]

        return IsoVersion1[0]


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def BackgroundUncer(self, Bkg_W, Bkg_T, Bkg_Z, Bkg_D,  Indice, channel, lepton, var,   multi, Energy):

        background_Unce = []
        Bkg_W_hist1 = histtoarray(Bkg_W.Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7"))
        Bkg_W_hist2 = histtoarray(Bkg_W.Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7"))
        Bkg_W_hist3 = histtoarray(Bkg_W.Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7"))
        Bkg_W_hist4 = histtoarray(Bkg_W.Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7"))
        Bkg_W_hist5 = histtoarray(Bkg_W.Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7"))
        Bkg_W_hist6 = histtoarray(Bkg_W.Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7"))

        Bkg_T_hist1 = histtoarray(Bkg_T.Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7"))
        Bkg_T_hist2 = histtoarray(Bkg_T.Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7"))
        Bkg_T_hist3 = histtoarray(Bkg_T.Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7"))
        Bkg_T_hist4 = histtoarray(Bkg_T.Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7"))
        Bkg_T_hist5 = histtoarray(Bkg_T.Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7"))
        Bkg_T_hist6 = histtoarray(Bkg_T.Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7"))

        Bkg_Z_hist1 = histtoarray(Bkg_Z.Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7"))
        Bkg_Z_hist2 = histtoarray(Bkg_Z.Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7"))
        Bkg_Z_hist3 = histtoarray(Bkg_Z.Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7"))
        Bkg_Z_hist4 = histtoarray(Bkg_Z.Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7"))
        Bkg_Z_hist5 = histtoarray(Bkg_Z.Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7"))
        Bkg_Z_hist6 = histtoarray(Bkg_Z.Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7"))

        Bkg_D_hist1 = histtoarray(Bkg_D.Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7"))
        Bkg_D_hist2 = histtoarray(Bkg_D.Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7"))
        Bkg_D_hist3 = histtoarray(Bkg_D.Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7"))
        Bkg_D_hist4 = histtoarray(Bkg_D.Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7"))
        Bkg_D_hist5 = histtoarray(Bkg_D.Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7"))
        Bkg_D_hist6 = histtoarray(Bkg_D.Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7"))

        Bkg_W       = np.concatenate((Bkg_W_hist1, Bkg_W_hist2, Bkg_W_hist3, Bkg_W_hist4, Bkg_W_hist5, Bkg_W_hist6))
        Bkg_T       = np.concatenate((Bkg_T_hist1, Bkg_T_hist2, Bkg_T_hist3, Bkg_T_hist4, Bkg_T_hist5, Bkg_T_hist6))
        Bkg_Z       = np.concatenate((Bkg_Z_hist1, Bkg_Z_hist2, Bkg_Z_hist3, Bkg_Z_hist4, Bkg_Z_hist5, Bkg_Z_hist6))
        Bkg_D       = np.concatenate((Bkg_D_hist1, Bkg_D_hist2, Bkg_D_hist3, Bkg_D_hist4, Bkg_D_hist5, Bkg_D_hist6))

        background_Unce = 0.05*0.05*Bkg_W*Bkg_W + 0.1*0.1*Bkg_T*Bkg_T + 0.05*0.05*Bkg_Z*Bkg_Z + 0.1*0.1*Bkg_D*Bkg_D

        return background_Unce


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def LuminosityUncer(self, SignalContent, Bkg_W, Bkg_T, Bkg_Z, Bkg_D,  Indice, channel, lepton, var,   multi, Energy):

        background_Unce = []
        Bkg_W_hist1 = histtoarray(Bkg_W.Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7"))
        Bkg_W_hist2 = histtoarray(Bkg_W.Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7"))
        Bkg_W_hist3 = histtoarray(Bkg_W.Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7"))
        Bkg_W_hist4 = histtoarray(Bkg_W.Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7"))
        Bkg_W_hist5 = histtoarray(Bkg_W.Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7"))
        Bkg_W_hist6 = histtoarray(Bkg_W.Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7"))

        Bkg_T_hist1 = histtoarray(Bkg_T.Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7"))
        Bkg_T_hist2 = histtoarray(Bkg_T.Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7"))
        Bkg_T_hist3 = histtoarray(Bkg_T.Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7"))
        Bkg_T_hist4 = histtoarray(Bkg_T.Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7"))
        Bkg_T_hist5 = histtoarray(Bkg_T.Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7"))
        Bkg_T_hist6 = histtoarray(Bkg_T.Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7"))

        Bkg_Z_hist1 = histtoarray(Bkg_Z.Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7"))
        Bkg_Z_hist2 = histtoarray(Bkg_Z.Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7"))
        Bkg_Z_hist3 = histtoarray(Bkg_Z.Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7"))
        Bkg_Z_hist4 = histtoarray(Bkg_Z.Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7"))
        Bkg_Z_hist5 = histtoarray(Bkg_Z.Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7"))
        Bkg_Z_hist6 = histtoarray(Bkg_Z.Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7"))

        Bkg_D_hist1 = histtoarray(Bkg_D.Get(channel+"Selection/Lepton_Eta_Reco_pt1_cut7"))
        Bkg_D_hist2 = histtoarray(Bkg_D.Get(channel+"Selection/Lepton_Eta_Reco_pt2_cut7"))
        Bkg_D_hist3 = histtoarray(Bkg_D.Get(channel+"Selection/Lepton_Eta_Reco_pt3_cut7"))
        Bkg_D_hist4 = histtoarray(Bkg_D.Get(channel+"Selection/Lepton_Eta_Reco_pt4_cut7"))
        Bkg_D_hist5 = histtoarray(Bkg_D.Get(channel+"Selection/Lepton_Eta_Reco_pt5_cut7"))
        Bkg_D_hist6 = histtoarray(Bkg_D.Get(channel+"Selection/Lepton_Eta_Reco_pt6_cut7"))

        Bkg_W       = np.concatenate((Bkg_W_hist1, Bkg_W_hist2, Bkg_W_hist3, Bkg_W_hist4, Bkg_W_hist5, Bkg_W_hist6))
        Bkg_T       = np.concatenate((Bkg_T_hist1, Bkg_T_hist2, Bkg_T_hist3, Bkg_T_hist4, Bkg_T_hist5, Bkg_T_hist6))
        Bkg_Z       = np.concatenate((Bkg_Z_hist1, Bkg_Z_hist2, Bkg_Z_hist3, Bkg_Z_hist4, Bkg_Z_hist5, Bkg_Z_hist6))
        Bkg_D       = np.concatenate((Bkg_D_hist1, Bkg_D_hist2, Bkg_D_hist3, Bkg_D_hist4, Bkg_D_hist5, Bkg_D_hist6))

        if(Energy == "5TeV"):
            ErrForLumi = 0.016

        if(Energy == "13TeV"):
            ErrForLumi = 0.015

        background_lumi = Bkg_W + Bkg_T + Bkg_Z + Bkg_D + SignalContent
        background_lumi = (ErrForLumi*background_lumi)*(ErrForLumi*background_lumi)

        return background_lumi
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def TotalScaleFacUnceEl(self, Signal, IsoUncertai, TrigUncertai, RecoUncertai, IdUncertai, Indice, channel, lepton, var,   multi, Energy):

        sig_hist = Signal.Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")

        UncertTotal = IsoUncertai + TrigUncertai + RecoUncertai + IdUncertai

        # for i in range(0, sig_hist.GetNbinsX()):
        #    if(sig_hist.GetBinContent(i+1) != 0):
        #        UncertTotal[i] = 100.*sqrt(UncertTotal[i])/sig_hist.GetBinContent(i+1)

        return UncertTotal

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def TotalScaleFacUnceMu(self, Signal, IsoUncertai, TrigUncertai, RecoUncertai,  Indice, channel, lepton, var, multi, Energy):

        sig_hist = Signal.Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")

        UncertTotal = IsoUncertai + TrigUncertai + RecoUncertai

        # for i in range(0, sig_hist.GetNbinsX()):
        #    if(sig_hist.GetBinContent(i+1) != 0):
        #        UncertTotal[i] = 100.*sqrt(UncertTotal[i])/sig_hist.GetBinContent(i+1)

        return UncertTotal


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def CalibrationVariat(self, Signal, channel, channelName, Energy, var):

        sig_hist = Signal.Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")
        Signalarray = histtoarray(sig_hist)

        CalibSystFiles = []
        CalibSystVariation = []

        for i in range(1, 25):
            CalibSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName +
                                             '_MC_'+str(Energy)+'/ElCalibVar/merge/mc16_'+str(Energy)+'.varscaleDownbin'+str(i)+'.root'))
        for i in range(1, 25):
            CalibSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName +
                                             '_MC_'+str(Energy)+'/ElCalibVar/merge/mc16_'+str(Energy)+'.varcDownbin'+str(i)+'.root'))

        for i in range(0, len(CalibSystFiles)):
            CalibSystVariation.append(histtoarray(CalibSystFiles[i].Get(
                channel+"Selection/Lepton_"+var+"_Reco_cut7")))

        for i in range(0, len(CalibSystVariation)):
            CalibSystVariation[i] = CalibSystVariation[i] - Signalarray

        CalibSystVariation[0] = CalibSystVariation[0]*CalibSystVariation[0]
        for i in range(1, len(CalibSystVariation)):
            CalibSystVariation[0] = CalibSystVariation[0] + \
                CalibSystVariation[i]*CalibSystVariation[i]

        CalibTotal = CalibSystVariation[0]
        # for i in range(0, sig_hist.GetNbinsX()):
        #    if(sig_hist.GetBinContent(i+1) != 0):
        #        CalibTotal[i] = 100.*sqrt(CalibTotal[i])/sig_hist.GetBinContent(i+1)

        return CalibTotal


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def PlotTotalUncerMu(self, Signal, data, arr_SF, arr_Re, Indice, channel, lepton, var, multi, Energy):

        sig_hist = Signal.Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")
        data_hist = data.Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")

        # convert hist to numpy array
        list_sig = []
        list_data = []

        for i in range(0, sig_hist.GetNbinsX()):
            if(sig_hist.GetBinContent(i+1) != 0):
                list_sig.append(100.*sig_hist.GetBinError(i+1) /
                                sig_hist.GetBinContent(i+1))
            if(sig_hist.GetBinContent(i+1) == 0):
                list_sig.append(0)
            if(data_hist.GetBinContent(i+1) != 0):
                list_data.append(
                    100.*data_hist.GetBinError(i+1) / data_hist.GetBinContent(i+1))
            if(data_hist.GetBinContent(i+1) == 0):
                list_data.append(0)

        arr_sig = np.array(list_sig)
        arr_data = np.array(list_data)

        if(var == "pT"):
            xlabel = np.array([25, 30, 35, 40, 45, 50, 60, 80, 100])
        if(var == "Eta"):
            if(lepton == "el"):
                xlabel = np.array([-2.47, -2.37, -2.01, -1.81, -1.52, -1.37, -1.15, -0.8, -
                                   0.6, -0.1, 0, 0.1, 0.6, 0.8, 1.15, 1.37, 1.52, 1.81, 2.01, 2.37, 2.47])
            if(lepton == "mu"):
                xlabel = np.array([-2.4, -1.918, -1.348, -1.1479, -1.05, -0.908, -
                                   0.476, 0, 0.476, 0.908, 1.05, 1.1479, 1.348, 1.918, 2.4])

        plt.show()
        plt.plot(xlabel, arr_sig,  label="Stats signal")
        plt.plot(xlabel, arr_data, label="Stats data")
        plt.plot(xlabel, arr_SF,   label="SF")
        plt.plot(xlabel, arr_Re,   label="Recoil")

        plt.xlim(0, 100)
        # plt.ylim(0,1.5)
        if(var == "pT"):
            plt.xlabel(r"$p_{T, lepton}$")
        if(var == "Eta"):
            plt.xlabel(r"$\eta_{lepton}$")
        plt.ylabel("Uncertainties (%)")
        plt.legend()
        plt.savefig("Output/Uncertainties/"+var+"_"+channel+"_"+Energy+".pdf")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def PlotTotalUncer(self, DataError, DataContent, SignalError, SignalContent, BackgroundUnce, SFUncertainty, CalibrationUncer, RecoilUncer, Indice, channel, lepton, var, multi, Energy):
        

        TotalUncerarr = []
        TotalErrorarr = []
        TotalErrorarr.append(0)
        for i in range(0, len(SFUncertainty)):
            if SignalContent[i] != 0:
                TotalUncerarr.append(  100*sqrt(BackgroundUnce[i] + SFUncertainty[i] + CalibrationUncer[i] + RecoilUncer[i] + DataError[i]*DataError[i])/ SignalContent[i] )
                TotalErrorarr.append(      sqrt(BackgroundUnce[i] + SFUncertainty[i] + CalibrationUncer[i] + RecoilUncer[i] + DataError[i]*DataError[i])/ SignalContent[i] )
            if SignalContent[i] == 0:
                TotalUncerarr.append(0)
                TotalErrorarr.append(0)
    
        for i in range(0, len(SFUncertainty)):
            if SignalContent[i] != 0:
                BackgroundUnce[i]   = 100*sqrt( BackgroundUnce[i]           )/SignalContent[i]
                SFUncertainty[i]    = 100*sqrt( SFUncertainty[i]            )/SignalContent[i]
                RecoilUncer[i]      = 100*sqrt( RecoilUncer[i]              )/SignalContent[i]
                DataError[i]        = 100*sqrt( DataError[i]*DataError[i]   )/SignalContent[i]
                CalibrationUncer[i] = 100*sqrt( CalibrationUncer[i]         )/SignalContent[i]
                SignalError[i]      = 100*sqrt( SignalError[i]              )/SignalContent[i]
            if SignalContent[i] == 0:
                SFUncertainty[i]    = 0
                RecoilUncer[i]      = 0
                DataError[i]        = 0
                CalibrationUncer[i] = 0
                SignalError[i]      = 0


        for i in range(0, len(DataError)):
            print(i, DataError[i], SFUncertainty[i], RecoilUncer[i], CalibrationUncer[i], TotalUncerarr[i])

        TotalUncer    = np.array(TotalUncerarr)
        TotalError    = np.array(TotalErrorarr)

        print(1, len(SFUncertainty),    type(SFUncertainty))
        print(2, len(CalibrationUncer), type(CalibrationUncer))
        print(3, len(RecoilUncer),      type(RecoilUncer))
        print(4, len(DataError),        type(DataError))
        print(5, len(DataContent),      type(DataContent))
        print(6, len(TotalUncer),       type(TotalUncer))
        print(6, len(SignalError),      type(SignalError))

        plt.show()
        fig = plt.figure()
        ax1 = fig.add_subplot()
        plt.ylim(0, 10)
        plt.figure(figsize=(12,5.5)) #12,5

        if(lepton == "el"):
            xlabel = np.array([0.05, 0.35, 0.7, 0.975, 1.26, 1.445, 1.665, 1.91, 2.19, 2.42, 2.5200000000000005, 2.8200000000000003, 3.1700000000000004, 3.4450000000000003, 3.7300000000000004, 3.915, 4.135, 4.380000000000001, 4.66, 4.890000000000001, 4.99, 5.290000000000001, 5.640000000000001, 5.915, 6.2, 6.385000000000001, 6.605, 6.8500000000000005, 7.130000000000001, 7.36, 7.460000000000001, 7.760000000000002, 8.110000000000001, 8.385000000000002, 8.670000000000002, 8.855, 9.075000000000001, 9.32, 9.600000000000001, 9.830000000000002, 9.930000000000001, 10.230000000000002, 10.580000000000002, 10.855, 11.14, 11.325000000000003, 11.545000000000002, 11.790000000000003, 12.070000000000002, 12.3, 12.400000000000002, 12.700000000000003, 13.050000000000002, 13.325000000000003, 13.610000000000003, 13.795000000000002, 14.015000000000002, 14.260000000000002, 14.540000000000003, 14.770000000000003])
            labelname = [ "0", " "," "," "," "," "," "," "," ","2.47", "", " "," "," "," "," "," "," "," ","2.47", "", " "," "," "," "," "," "," "," ","2.47", "", " "," "," "," "," "," "," "," ","2.47", "", " "," "," "," "," "," "," "," ","2.47", "", " "," "," "," "," "," "," "," ","2.47"]
            print(len(xlabel))
        if(lepton == "mu"):
            xlabel = np.array([0.238, 0.692, 0.9790000000000001, 1.0989499999999999, 1.24795, 1.633, 2.159, 2.638, 3.0919999999999996, 3.379, 3.49895, 3.64795, 4.0329999999999995, 4.558999999999999, 5.038, 5.492, 5.779, 5.898949999999999, 6.04795, 6.433, 6.959, 7.438, 7.892, 8.179, 8.29895, 8.447949999999999, 8.833, 9.359, 9.838000000000001, 10.292000000000002, 10.579, 10.69895, 10.84795, 11.233, 11.759, 12.238, 12.692, 12.979000000000001, 13.09895, 13.24795, 13.633000000000001, 14.159])
            labelname = [ "0", " "," "," "," "," ","2.4", " ", " "," "," "," "," ","2.4", " ", " "," "," "," "," ","2.4"," ", " "," "," "," "," ","2.4"," ", " "," "," "," "," ","2.4"," ", " "," "," "," "," ","2.4"]


        plt.plot(xlabel, SignalError,     label="Statistics (MC)")
        plt.plot(xlabel, DataError,       label="Statistics (Data)")
        plt.plot(xlabel, BackgroundUnce,  label="Syst. Background")
        plt.plot(xlabel, SFUncertainty,   label="Syst. Sf")
        plt.plot(xlabel, RecoilUncer,     label="Syst. recoil calibration")
        plt.plot(xlabel, TotalUncer,      label="Total Uncertainty")
        if (lepton == "el"):
            plt.plot(xlabel, CalibrationUncer,  label="Syst. lepton calibration")

        atlasify("Internal", r"$"+Indice+"$", font_size=20, label_font_size=20, sub_font_size=20)

        nline = 8
        if(lepton == "mu"):

            plt.text(0,     8, r' 25 < $p_{T}^{\ell}$ < 30', fontsize=15)
            plt.text(2.4,   8, r' 30 < $p_{T}^{\ell}$ < 35', fontsize=15)
            plt.text(4.8,   8, r' 35 < $p_{T}^{\ell}$ < 40', fontsize=15)
            plt.text(7.2,   8, r' 40 < $p_{T}^{\ell}$ < 45', fontsize=15)
            plt.text(9.6,   8, r' 55 < $p_{T}^{\ell}$ < 50', fontsize=15)
            plt.text(12.,   8, r' 50 < $p_{T}^{\ell}$ < 100', fontsize=15)

            plt.vlines(0,    -1, nline, colors='k', linestyles='dotted')
            plt.vlines(2.4,  -1, nline, colors='k', linestyles='dotted')
            plt.vlines(4.8,  -1, nline, colors='k', linestyles='dotted')
            plt.vlines(7.2,  -1, nline, colors='k', linestyles='dotted')
            plt.vlines(9.6,  -1, nline, colors='k', linestyles='dotted')
            plt.vlines(12,   -1, nline, colors='k', linestyles='dotted')
            plt.vlines(14.4, -1, nline, colors='k', linestyles='dotted')

        if(lepton == "el"):
            plt.text(0,      8, r' 25 < $p_{T}^{\ell}$ < 30', fontsize=15)
            plt.text(2.47,   8, r' 30 < $p_{T}^{\ell}$ < 35', fontsize=15)
            plt.text(4.94,   8, r' 35 < $p_{T}^{\ell}$ < 40', fontsize=15)
            plt.text(7.41,   8, r' 40 < $p_{T}^{\ell}$ < 45', fontsize=15)
            plt.text(9.88,   8, r' 45 < $p_{T}^{\ell}$ < 50', fontsize=15)
            plt.text(12.35,  8, r' 50 < $p_{T}^{\ell}$ < 100', fontsize=15)

            plt.vlines(0,     -1, nline, colors='k', linestyles='dotted')
            plt.vlines(2.47,  -1, nline, colors='k', linestyles='dotted')
            plt.vlines(4.94,  -1, nline, colors='k', linestyles='dotted')
            plt.vlines(7.41,  -1, nline, colors='k', linestyles='dotted')
            plt.vlines(9.88,  -1, nline, colors='k', linestyles='dotted')
            plt.vlines(12.35, -1, nline, colors='k', linestyles='dotted')
            plt.vlines(14.82, -1, nline, colors='k', linestyles='dotted')


        plt.ylim(0, 14)
        plt.xlabel(r"$\eta_{lepton}$")
        plt.ylabel("Relative Uncertainties (%)")
        plt.legend(ncol=2,loc='upper right')
        plt.xticks(xlabel, labelname, fontsize=14)
        plt.savefig("Output/Uncertainties/2D_"+var+"_"+channel+"_"+Energy+".pdf")
        savetxt("Output/UncertaintyBand/2D_"+var+"_"+channel +"_"+Energy+".csv", TotalError, delimiter=',')