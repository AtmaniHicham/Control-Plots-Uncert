#!/usr/bin/env python
# -*-coding:Latin-1 -*

from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TLatex, TChain
from array import array
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TH1
import sys
import atlasplots as aplt
import numpy as np
from numpy import savetxt
import ROOT as root
import ROOT
from math import *
from atlasify import atlasify
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 15})


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
        print(hist.GetNbinsX(), hist_shape_up.GetNbinsX(),hist_ExtrapErr_up.GetNbinsX(), hist_uTSliceErr_up.GetNbinsX())

        shape_up = hist_shape_up.Clone("shape_up")
        ExtrapErr_up = hist_ExtrapErr_up.Clone("ExtrapErr_up")
        uTSliceErr_up = hist_uTSliceErr_up.Clone("uTSliceErr_up")

        TotalMJ_Uncer = []

        for i in range(0, hist.GetNbinsX()):
            shape_up.SetBinContent(i+1,         hist_shape_up.GetBinContent(i+1) - hist.GetBinContent(i+1))
            ExtrapErr_up.SetBinContent(i+1,     hist_ExtrapErr_up.GetBinContent(i+1) - hist.GetBinContent(i+1))
            uTSliceErr_up.SetBinContent(i+1,    hist_uTSliceErr_up.GetBinContent(i+1) - hist.GetBinContent(i+1))

        for i in range(0, hist.GetNbinsX()):
            TotalMJ_Uncer.append(pow(hist.GetBinError(i+1), 2) + pow(shape_up.GetBinContent(i+1), 2) + pow(ExtrapErr_up.GetBinContent(i+1), 2) + pow(uTSliceErr_up.GetBinContent(i+1), 2) )

        return TotalMJ_Uncer


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

    def LuminosityUncer(self, Signal, Bkg_W, Bkg_T, Bkg_Z, Bkg_D, Indice, channel, lepton, var,   multi, Energy):

        background_Unce = []
        Signal_hist = (Signal.Get(channel+"Selection/Lepton_" +var+"_Reco_cut7")).Clone("Signal_hist")
        Bkg_W_hist  = (Bkg_W.Get(channel+"Selection/Lepton_" +var+"_Reco_cut7")).Clone("Bkg_W_hist")
        Bkg_T_hist  = (Bkg_T.Get(channel+"Selection/Lepton_" +var+"_Reco_cut7")).Clone("Bkg_T_hist")
        Bkg_Z_hist  = (Bkg_Z.Get(channel+"Selection/Lepton_" +var+"_Reco_cut7")).Clone("Bkg_Z_hist")
        Bkg_D_hist  = (Bkg_D.Get(channel+"Selection/Lepton_" +var+"_Reco_cut7")).Clone("Bkg_D_hist")

        Total_Unce = Bkg_W_hist.Clone()

        for i in range(0, Bkg_W_hist.GetNbinsX()):
            Total_Unce.SetBinContent(i+1,  Signal_hist.GetBinContent(i+1) + Bkg_W_hist.GetBinContent(i+1) + Bkg_T_hist.GetBinContent(i+1) + Bkg_Z_hist.GetBinContent(i+1) + Bkg_D_hist.GetBinContent(i+1))

        if(Energy == "5TeV"):
            ErrForLumi = 0.016

        if(Energy == "13TeV"):
            ErrForLumi = 0.015

        for i in range(0, Total_Unce.GetNbinsX()):
            background_Unce.append(ErrForLumi*Total_Unce.GetBinContent(i+1))
            print("Luminosity Uncer : ", i+1, ErrForLumi*Total_Unce.GetBinContent(i+1) )
        return background_Unce

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def BackgroundUncer(self, Bkg_W, Bkg_T, Bkg_Z, Bkg_D, Indice, channel, lepton, var,   multi, Energy):

        background_Unce = []
        Bkg_W_hist = (Bkg_W.Get(channel+"Selection/Lepton_" + var+"_Reco_cut7")).Clone("Bkg_W_hist")
        Bkg_T_hist = (Bkg_T.Get(channel+"Selection/Lepton_" + var+"_Reco_cut7")).Clone("Bkg_T_hist")
        Bkg_Z_hist = (Bkg_Z.Get(channel+"Selection/Lepton_" + var+"_Reco_cut7")).Clone("Bkg_Z_hist")
        Bkg_D_hist = (Bkg_D.Get(channel+"Selection/Lepton_" + var+"_Reco_cut7")).Clone("Bkg_D_hist")

        Total_Unce = Bkg_W_hist.Clone()

        for i in range(0, Bkg_W_hist.GetNbinsX()):
            Total_Unce.SetBinContent(i+1, sqrt(pow(0.05 * Bkg_W_hist.GetBinContent(i+1), 2) +
                                               pow(0.1 * Bkg_T_hist.GetBinContent(i+1), 2) +
                                               pow(0.05 * Bkg_Z_hist.GetBinContent(i+1), 2) +
                                               pow(0.1 * Bkg_D_hist.GetBinContent(i+1), 2)))

        for i in range(0, Total_Unce.GetNbinsX()):
            background_Unce.append(Total_Unce.GetBinContent(i+1))

        return background_Unce

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

    def CalibrationVariatmu(self, Signal, channel, channelName, Energy, var):

        sig_hist = Signal.Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")
        Signalarray = histtoarray(sig_hist)

        CalibSystFiles = []
        CalibSystVariation = []

        CalibSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName + '_MC_'+str(Energy)+'/MuCalibVar/merge/MC_varMUON_ID_1down.root'))
        CalibSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName + '_MC_'+str(Energy)+'/MuCalibVar/merge/MC_varMUON_MS_1down.root'))
        CalibSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName + '_MC_'+str(Energy)+'/MuCalibVar/merge/MC_varMUON_SCALE_1down.root'))
        CalibSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName + '_MC_'+str(Energy)+'/MuCalibVar/merge/MC_varSagittaBiasOffsetDown.root'))

        for i in range(1, 25):
            CalibSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName + '_MC_'+str(Energy)+'/MuCalibVar/merge/mc16_'+str(Energy)+'.varSagittaBiasstatDownbin'+str(i)+'.root'))

        for i in range(0, len(CalibSystFiles)):
            CalibSystVariation.append(histtoarray(CalibSystFiles[i].Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")))

        for i in range(0, len(CalibSystVariation)):
            CalibSystVariation[i] = CalibSystVariation[i] - Signalarray

        CalibSystVariation[0] = CalibSystVariation[0]*CalibSystVariation[0]
        for i in range(1, len(CalibSystVariation)):
            CalibSystVariation[0] = CalibSystVariation[0] + CalibSystVariation[i]*CalibSystVariation[i]

        CalibTotal = CalibSystVariation[0]
        # for i in range(0, sig_hist.GetNbinsX()):
        #    if(sig_hist.GetBinContent(i+1) != 0):
        #        CalibTotal[i] = 100.*sqrt(CalibTotal[i])/sig_hist.GetBinContent(i+1)

        return CalibTotal
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def CalibrationVariat(self, Signal, channel, channelName, Energy, var):

        sig_hist = Signal.Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")
        Signalarray = histtoarray(sig_hist)

        CalibSystFiles = []
        CalibSystVariation = []

        for i in range(1, 25):
            CalibSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName + '_MC_'+str(Energy)+'/ElCalibVar/merge/mc16_'+str(Energy)+'.varscaleDownbin'+str(i)+'.root'))
        for i in range(1, 25):
            CalibSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName + '_MC_'+str(Energy)+'/ElCalibVar/merge/mc16_'+str(Energy)+'.varcDownbin'+str(i)+'.root'))

        for i in range(0, len(CalibSystFiles)):
            CalibSystVariation.append(histtoarray(CalibSystFiles[i].Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")))

        for i in range(0, len(CalibSystVariation)):
            CalibSystVariation[i] = CalibSystVariation[i] - Signalarray

        CalibSystVariation[0] = CalibSystVariation[0]*CalibSystVariation[0]
        for i in range(1, len(CalibSystVariation)):
            CalibSystVariation[0] = CalibSystVariation[0] + CalibSystVariation[i]*CalibSystVariation[i]

        CalibTotal = CalibSystVariation[0]

        return CalibTotal

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def Recoil(self, Signal, channel, channelName, Energy, var):

        sig_hist = Signal.Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")
        Signalarray = histtoarray(sig_hist)

        RecoilSystFiles = []
        RecoilSystVariation = []

        if(Energy == "5TeV"):

            print('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName +
                  '_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESPONSE_EXTSYS_DOWNbin1.root')
            print('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName +
                  '_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESOLUTION_EXTSYS_DOWNbin1.root')
            print('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName +
                  '_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESPONSE_SYS_DOWNbin1.roo')

            RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' +
                                              channelName+'_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESPONSE_EXTSYS_DOWNbin1.root'))
            RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' +
                                              channelName+'_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESOLUTION_EXTSYS_DOWNbin1.root'))
            RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' +
                                              channelName+'_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESPONSE_SYS_DOWNbin1.root'))

            for i in range(3, 20):  # 1, 20
                RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' +
                                                  channelName+'_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESPONSE_STAT0_DOWNbin'+str(i)+'.root'))
                RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName +
                                                  '_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESPONSE_STAT1_DOWNbin'+str(i)+'.root'))  # error

            for i in range(1, 13):  # 1, 13
                RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' +
                                                  channelName+'_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESOLUTION_STAT0_DOWNbin'+str(i)+'.root'))
                RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' +
                                                  channelName+'_MC_5TeV/RecoilVar/merge/mc16_5TeV.varRESOLUTION_STAT1_DOWNbin'+str(i)+'.root'))

        if(Energy == "13TeV"):
            print('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName +
                  '_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESPONSE_EXTSYS_DOWNbin1.root')
            print('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName +
                  '_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESOLUTION_EXTSYS_DOWNbin1.root')
            print('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName +
                  '_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESPONSE_SYS_DOWNbin1.roo')

            # RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' +channelName+'_MC_13TeV/RecoilVar/merge/mc16_13TeV.varSET_SYSbin1.root'))
            RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' +
                                              channelName+'_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESPONSE_EXTSYS_DOWNbin1.root'))
            RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' +
                                              channelName+'_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESOLUTION_EXTSYS_DOWNbin1.root'))
            RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' +
                                              channelName+'_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESPONSE_SYS_DOWNbin1.root'))

            for i in range(1, 10):
                print('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName +
                      '_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESPONSE_STAT0_DOWNbin'+str(i)+'.root')
                print('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName +
                      '_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESPONSE_STAT1_DOWNbin'+str(i)+'.root')

                RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' +
                                                  channelName+'_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESPONSE_STAT0_DOWNbin'+str(i)+'.root'))
                RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' +
                                                  channelName+'_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESPONSE_STAT1_DOWNbin'+str(i)+'.root'))

            for i in range(1, 15):
                print('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName +
                      '_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESOLUTION_STAT0_DOWNbin'+str(i)+'.root')
                print('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' + channelName +
                      '_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESOLUTION_STAT1_DOWNbin'+str(i)+'.root')
                RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' +
                                                  channelName+'_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESOLUTION_STAT0_DOWNbin'+str(i)+'.root'))
                RecoilSystFiles.append(ROOT.TFile('/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w' +
                                                  channelName+'_MC_13TeV/RecoilVar/merge/mc16_13TeV.varRESOLUTION_STAT1_DOWNbin'+str(i)+'.root'))

        for i in range(0, len(RecoilSystFiles)):
            print(RecoilSystFiles[i])
            # print("Var  : ",i,"      ",   (RecoilSystFiles[i].Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")).GetMean())
            # print("Var  : ",i,"      ",  RecoilSystFiles[i].GetName(),  (RecoilSystFiles[i].Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")).GetMean())
            RecoilSystVariation.append(histtoarray(RecoilSystFiles[i].Get(
                channel+"Selection/Lepton_"+var+"_Reco_cut7")))

        for i in range(0, len(RecoilSystVariation)):
            RecoilSystVariation[i] = RecoilSystVariation[i] - Signalarray
            # print("Var  : ",i,"      ",RecoilSystVariation[i])

        RecoilSystVariation[0] = RecoilSystVariation[0]*RecoilSystVariation[0]
        for i in range(1, len(RecoilSystVariation)):
            RecoilSystVariation[0] = RecoilSystVariation[0] + \
                RecoilSystVariation[i]*RecoilSystVariation[i]

        RecoilTotal = RecoilSystVariation[0]
        # for i in range(0, sig_hist.GetNbinsX()):
        #    if(sig_hist.GetBinContent(i+1) != 0):
        #        RecoilTotal[i] = 100.*sqrt(RecoilTotal[i])/sig_hist.GetBinContent(i+1)

        return RecoilTotal

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

    def PlotTotalUncerEl(self, Signal, data, arr_Bk, arr_SF, arr_Ca, arr_Re, Indice, channel, lepton, var, multi, Energy):

        sig_hist        = Signal.Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")
        data_hist       = data.Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")
        TotalUncer_hist = sig_hist.Clone("TotalUncer_hist")
        
        # convert hist to numpy array
        list_sig = []
        list_data = []
        Total_unce = []
        Total_root = []
        Total_root.append(0)

        n = sig_hist.GetNbinsX()
        for i in range(0, n):
            if(sig_hist.GetBinContent(i+1) != 0):
                list_sig.append(100.*sig_hist.GetBinError(i+1) / sig_hist.GetBinContent(i+1))
                Total_unce.append(100.*sqrt(arr_Bk[i] + arr_SF[i] + arr_Ca[i] + arr_Re[i] + data_hist.GetBinError(i+1)*data_hist.GetBinError(i+1)) / sig_hist.GetBinContent(i+1))
                Total_root.append(     sqrt(arr_Bk[i] + arr_SF[i] + arr_Ca[i] + arr_Re[i] + data_hist.GetBinError(i+1)*data_hist.GetBinError(i+1)) / sig_hist.GetBinContent(i+1))
                arr_SF[i] = 100. * sqrt(arr_SF[i]) / sig_hist.GetBinContent(i+1)
                arr_Bk[i] = 100. * sqrt(arr_Bk[i]) / sig_hist.GetBinContent(i+1)
                arr_Ca[i] = 100. * sqrt(arr_Ca[i]) / sig_hist.GetBinContent(i+1)
                arr_Re[i] = 100. * sqrt(arr_Re[i]) / sig_hist.GetBinContent(i+1)
            if(sig_hist.GetBinContent(i+1) == 0):
                Total_unce.append(0)
                Total_root.append(0)
                arr_SF[i] = 0
                arr_Bk[i] = 0
                arr_Ca[i] = 0
                arr_Re[i] = 0
                list_sig.append(0)
            if(data_hist.GetBinContent(i+1) != 0):
                list_data.append(100.*data_hist.GetBinError(i+1) / data_hist.GetBinContent(i+1))
            if(data_hist.GetBinContent(i+1) == 0):
                list_data.append(0)

        for i in range(0, len(arr_SF)):
            print(i, arr_SF[i], Total_unce[i])


        arr_sig     = np.array(list_sig)
        arr_data    = np.array(list_data)

        if(var == "pT"):
            xlabel = np.array([12.5, 27.5, 32.5, 37.5, 42.5, 47.5, 55.0, 70.0, 540.0])
        if(var == "Eta"):
            if(lepton == "el"):
                xlabel = np.array([-2.42, -2.19, -1.91, -1.665, -1.445, -1.26, -0.975, -0.7, -0.35, -0.05, 0.05, 0.35, 0.7, 0.975, 1.26, 1.445, 1.665, 1.91, 2.19, 2.42])
            if(lepton == "mu"):
                xlabel = np.array([-2.159, -1.633, -1.24795, -1.09895, -0.979, -0.692, -0.238, 0.238, 0.692, 0.979, 1.09895, 1.24795, 1.633, 2.159])

        font = {'family': 'serif','weight': 'normal','size': 12,}

        plt.show()
        if(var == "pT"):    plt.ylim(0, 4)
        if(var == "Eta"):   plt.ylim(0, 4)
        dim = len(xlabel)
        first = 0
        if(var == "pT"):
            dim = dim-1
            first = 1

        plt.plot(xlabel[first:dim], arr_sig[first:dim],     label="Statistics (MC)")
        plt.plot(xlabel[first:dim], arr_data[first:dim],    label="Statistics (Data)")
        plt.plot(xlabel[first:dim], arr_Bk[first:dim],      label="Syst. Background")
        plt.plot(xlabel[first:dim], arr_SF[first:dim],      label="Syst. Sf")
        if (lepton == "el"):
            plt.plot(xlabel[first:dim], arr_Ca[first:dim],  label="Syst. lepton calibration")
        plt.plot(xlabel[first:dim], arr_Re[first:dim],      label="Syst. recoil calibration")
        plt.plot(xlabel[first:dim], Total_unce[first:dim],  label="Total Uncertainty")
        if(var == "pT"):
            atlasify("Internal", r"$"+Indice+"$")
            plt.text(1, 13, r'$ '+Indice+'$', fontdict=font)
        if(var == "Eta"):
            atlasify("Internal", r"$"+Indice+"$")

        if(var == "pT"):                        plt.xlabel(r"$p_{T, lepton}$")
        if(var == "Eta"):                       plt.xlabel(r"$\eta_{lepton}$")

        plt.ylabel("Relative Uncertainties (%)")
        plt.legend(loc='upper right')
        plt.savefig("Output/Uncertainties/"+var+"_"+channel+"_"+Energy+".pdf")
        savetxt("Output/UncertaintyBand/"  +var+"_"+channel+"_"+Energy+".csv", Total_root, delimiter=',')
