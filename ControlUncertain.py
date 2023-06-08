#!/usr/bin/env python
# -*-coding:Latin-1 -*

from math import sqrt
import ROOT
import ROOT as root
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import time
import gc

from ROOT import gROOT
from array import array
from source.UncertaintyClass import UncertClass

def CrossSectionMJ(Bkg_MJ_rebinned_hist, Bkg_MJ_rebinned_shape_uphist, Bkg_MJ_rebinned_ExtrapErr_uphist, Bkg_MJ_rebinned_uTSliceErr_uphist, channel, Energy, DirectoName):

    Hist_Nom        = histtoarray(Bkg_MJ_rebinned_hist)
    Hist_uTSliceErr = histtoarray(Bkg_MJ_rebinned_shape_uphist)
    Hist_ExtrapErr  = histtoarray(Bkg_MJ_rebinned_ExtrapErr_uphist)
    Hist_shape      = histtoarray(Bkg_MJ_rebinned_uTSliceErr_uphist)

    ErrorStat = []
    for i in range(0, Bkg_MJ_rebinned_hist.GetNbinsX()):
        ErrorStat.append(Bkg_MJ_rebinned_hist.GetBinError(i+1))
    
    Error1 = Hist_uTSliceErr - Hist_Nom
    Error2 = Hist_ExtrapErr  - Hist_Nom
    Error3 = Hist_shape      - Hist_Nom
    Error4 = np.array(ErrorStat)

    ErrorTotal = Error1*Error1 + Error2*Error2 + Error3*Error3 + Error4*Error4
    return ErrorTotal

def histtoarray(hist):
    vector = []
    for i in range(0, hist.GetNbinsX()):
        vector.append(hist.GetBinContent(i+1))

    array = np.array(vector)
    return array

def CrossSectionNormalisa(channel, NormalisationPath, var):

    lepton = "ee"
    if "munu" in channel: lepton = "mumu"
    NameVector = ["ttbar", "singletop", "Wtop", "Wminusenu", "Wplusenu", "Wminusmunu", "Wplusmunu", "Wplustaunu", "Wminustaunu", "Z"+lepton, "Ztautau", "ZZ", "WZ", "WW", "multijet"]

    Variation   = []
    DireName    = channel + "Selection_NormVariations"
    files       = os.listdir(NormalisationPath)
    for i in files:
        rootFile    = ROOT.TFile.Open(NormalisationPath+"/"+i)
        HistNominal = rootFile.Get(DireName+"/Lepton_"+var+"_Reco_cut7_Nom")
        for j in NameVector:
            HistVaried   = rootFile.Get(DireName+"/Lepton_"+var+"_Reco_cut7_Xsec_up_"+j)
            if HistVaried == None: continue
            else: break
        Variation.append(   (histtoarray(HistVaried) - histtoarray(HistNominal))   )

    Variation[0] = Variation[0]*Variation[0]
    for i in range(1, len(Variation)):
        Variation[0] = Variation[0] + Variation[i]*Variation[i]
    NormalisationTotal = Variation[0]

    return NormalisationTotal

def TheMultiJetBackground(Signal, Bkg_MJ, channel, var, directory, lepton, multi):
    nominal      = (Signal.Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")).Clone("nominal")
    histogram_MJ = (Bkg_MJ.Get(directory+"/"+lepton+multi)).Clone("histogram_MJ")

    return histogram_MJ

def rebinTheMultiJetBackground(nominalFile, MJFile, channel, var, directory, lepton, multi):

    nominal = (nominalFile.Get(channel+"Selection/Lepton_" +var+"_Reco_cut7")).Clone("nominal")
    histogram_MJ = (MJFile.Get(directory+"/"+lepton+multi)).Clone("histogram_MJ")

    nominal.SetBinContent(1, 0)
    nominal.SetBinContent(2, histogram_MJ.GetBinContent(26) + histogram_MJ.GetBinContent(27) + histogram_MJ.GetBinContent(28) + histogram_MJ.GetBinContent(29) + histogram_MJ.GetBinContent(30))
    nominal.SetBinContent(3, histogram_MJ.GetBinContent(31) + histogram_MJ.GetBinContent(32) + histogram_MJ.GetBinContent(33) + histogram_MJ.GetBinContent(34) + histogram_MJ.GetBinContent(35))
    nominal.SetBinContent(4, histogram_MJ.GetBinContent(36) + histogram_MJ.GetBinContent(37) + histogram_MJ.GetBinContent(38) + histogram_MJ.GetBinContent(39) + histogram_MJ.GetBinContent(40))
    nominal.SetBinContent(5, histogram_MJ.GetBinContent(41) + histogram_MJ.GetBinContent(42) + histogram_MJ.GetBinContent(43) + histogram_MJ.GetBinContent(44) + histogram_MJ.GetBinContent(45))
    nominal.SetBinContent(6, histogram_MJ.GetBinContent(46) + histogram_MJ.GetBinContent(47) + histogram_MJ.GetBinContent(48) + histogram_MJ.GetBinContent(49) + histogram_MJ.GetBinContent(50))

    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(51, 61):
        sum1 = sum1 + histogram_MJ.GetBinContent(i)
    for i in range(61, 81):
        sum2 = sum2 + histogram_MJ.GetBinContent(i)
    for i in range(81, 101):
        sum3 = sum3 + histogram_MJ.GetBinContent(i)

    nominal.SetBinContent(7, sum1)
    nominal.SetBinContent(8, sum2)
    nominal.SetBinContent(9, sum3)

    nominal.SetBinError(1, 0)
    nominal.SetBinError(2, sqrt(pow(histogram_MJ.GetBinError(26), 2) + pow(histogram_MJ.GetBinError(27), 2) + pow(histogram_MJ.GetBinError(28), 2) + pow(histogram_MJ.GetBinError(29), 2) + pow(histogram_MJ.GetBinError(30), 2)))
    nominal.SetBinError(3, sqrt(pow(histogram_MJ.GetBinError(31), 2) + pow(histogram_MJ.GetBinError(32), 2) + pow(histogram_MJ.GetBinError(33), 2) + pow(histogram_MJ.GetBinError(34), 2) + pow(histogram_MJ.GetBinError(35), 2)))
    nominal.SetBinError(4, sqrt(pow(histogram_MJ.GetBinError(36), 2) + pow(histogram_MJ.GetBinError(37), 2) + pow(histogram_MJ.GetBinError(38), 2) + pow(histogram_MJ.GetBinError(39), 2) + pow(histogram_MJ.GetBinError(40), 2)))
    nominal.SetBinError(5, sqrt(pow(histogram_MJ.GetBinError(41), 2) + pow(histogram_MJ.GetBinError(42), 2) + pow(histogram_MJ.GetBinError(43), 2) + pow(histogram_MJ.GetBinError(44), 2) + pow(histogram_MJ.GetBinError(45), 2)))
    nominal.SetBinError(6, sqrt(pow(histogram_MJ.GetBinError(46), 2) + pow(histogram_MJ.GetBinError(47), 2) + pow(histogram_MJ.GetBinError(48), 2) + pow(histogram_MJ.GetBinError(49), 2) + pow(histogram_MJ.GetBinError(50), 2)))

    errsum1 = 0
    errsum2 = 0
    errsum3 = 0
    for i in range(51, 61):
        errsum1 = errsum1 + pow(histogram_MJ.GetBinError(i), 2)
    for i in range(61, 81):
        errsum2 = errsum2 + pow(histogram_MJ.GetBinError(i), 2)
    for i in range(81, 101):
        errsum3 = errsum3 + pow(histogram_MJ.GetBinError(i), 2)

    nominal.SetBinError(7, sqrt(errsum1))
    nominal.SetBinError(8, sqrt(errsum2))
    nominal.SetBinError(9, sqrt(errsum3))

    return nominal

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Define inputs
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

data   = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w" + sys.argv[2] + "_DATA_" + sys.argv[3]+ "/Nominal/DATA.root")
Signal = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w" + sys.argv[2] + "_MC_"   + sys.argv[3]+ "/Nominal/MC.root")
Bkg_W  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w" + sys.argv[2] + "_MC_"   + sys.argv[3]+ "/Nominal/merge/Nominal_W.root")
Bkg_T  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w" + sys.argv[2] + "_MC_"   + sys.argv[3]+ "/Nominal/merge/Nominal_Top.root")
Bkg_Z  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w" + sys.argv[2] + "_MC_"   + sys.argv[3]+ "/Nominal/merge/Nominal_Z.root")
Bkg_D  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w" + sys.argv[2] + "_MC_"   + sys.argv[3]+ "/Nominal/merge/Nominal_dilepton.root")

if ("plusenu" in sys.argv[1]):    MJvar = "Wep"
if ("minusenu" in sys.argv[1]):   MJvar = "Wem"
if ("plusmunu" in sys.argv[1]):   MJvar = "Wmup"
if ("minusmunu" in sys.argv[1]):  MJvar = "Wmum"

Bkg_MJ = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/"+sys.argv[3]+"/"+MJvar+".root")

# define the different sources of uncert:
if sys.argv[5] == "mu":
    Signal_Iso    = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w" + sys.argv[2] + "_MC_" + sys.argv[3]+"/MuonSF_iso/MC.root")
    Signal_Trig   = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w" + sys.argv[2] + "_MC_" + sys.argv[3]+"/MuonSF_trig/MC.root")
    Signal_recoSF = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w" + sys.argv[2] + "_MC_" + sys.argv[3]+"/MuonSF_reco/MC.root")
    Signal_ttva   = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w" + sys.argv[2] + "_MC_" + sys.argv[3]+"/MuonSF_ttva/MC.root")

if sys.argv[5] == "el":
    Signal_Iso    = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w" + sys.argv[2] + "_MC_" + sys.argv[3]+"/ElecSF_iso/MC.root")
    Signal_Trig   = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w" + sys.argv[2] + "_MC_" + sys.argv[3]+"/ElecSF_trig/MC.root")
    Signal_recoSF = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w" + sys.argv[2] + "_MC_" + sys.argv[3]+"/ElecSF_reco/MC.root")
    Signal_Id     = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w" + sys.argv[2] + "_MC_" + sys.argv[3]+"/ElecSF_id/MC.root")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Rebin Histograms
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# rebinning of MJ histogram:
if "enu"  in sys.argv[1]:     leptonn = "el"
if "pT"   in sys.argv[6]:     multii  = "Pt"
if "munu" in sys.argv[1]:     leptonn = "mu"
if "Eta"  in sys.argv[6]:     multii  = "Eta"

if "pT" in sys.argv[6]:
    Bkg_MJ_rebinned_hist                = rebinTheMultiJetBackground(Signal, Bkg_MJ, sys.argv[1], sys.argv[6], "hist"			, leptonn, multii)
    Bkg_MJ_rebinned_shape_uphist        = rebinTheMultiJetBackground(Signal, Bkg_MJ, sys.argv[1], sys.argv[6], "shape_uphist"		, leptonn, multii)
    Bkg_MJ_rebinned_ExtrapErr_uphist    = rebinTheMultiJetBackground(Signal, Bkg_MJ, sys.argv[1], sys.argv[6], "ExtrapErr_uphist"	, leptonn, multii)
    Bkg_MJ_rebinned_uTSliceErr_uphist   = rebinTheMultiJetBackground(Signal, Bkg_MJ, sys.argv[1], sys.argv[6], "uTSliceErr_uphist"	, leptonn, multii)

if "Eta" in sys.argv[6]:
    Bkg_MJ_rebinned_hist                = TheMultiJetBackground(Signal, Bkg_MJ, sys.argv[1], sys.argv[6], "hist"			, leptonn, multii)
    Bkg_MJ_rebinned_shape_uphist        = TheMultiJetBackground(Signal, Bkg_MJ, sys.argv[1], sys.argv[6], "shape_uphist"		, leptonn, multii)
    Bkg_MJ_rebinned_ExtrapErr_uphist    = TheMultiJetBackground(Signal, Bkg_MJ, sys.argv[1], sys.argv[6], "ExtrapErr_uphist"		, leptonn, multii)
    Bkg_MJ_rebinned_uTSliceErr_uphist   = TheMultiJetBackground(Signal, Bkg_MJ, sys.argv[1], sys.argv[6], "uTSliceErr_uphist"		, leptonn, multii)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Define the uncertainties class
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# define the class for uncertainties
ClassUncer      = UncertClass()

# define the background uncertainties
#BackUncert      = np.array(ClassUncer.BackgroundUncer(Bkg_W,  Bkg_T, Bkg_Z, Bkg_D,sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3]))				# Background Unc
#LumiUncert      = np.array(ClassUncer.LuminosityUncer(Signal, Bkg_W,  Bkg_T, Bkg_Z, Bkg_D,sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3]))				# Lumi Uncertin
#TotalMJ_Uncer   = np.array(ClassUncer.MJUncertainties(Bkg_MJ_rebinned_hist,  Bkg_MJ_rebinned_shape_uphist,Bkg_MJ_rebinned_ExtrapErr_uphist,  Bkg_MJ_rebinned_uTSliceErr_uphist))  # MJ uncertaint

#define the normalisation systematics
NormalisationPath   = "/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_MC_"+sys.argv[3]+"/Normalization/"
NormalisationSyst   = CrossSectionNormalisa(sys.argv[1], NormalisationPath, sys.argv[6])

# define the Multijet systematic:
MultiJetCalibrea    = CrossSectionMJ(Bkg_MJ_rebinned_hist, Bkg_MJ_rebinned_shape_uphist, Bkg_MJ_rebinned_ExtrapErr_uphist, Bkg_MJ_rebinned_uTSliceErr_uphist, sys.argv[2], sys.argv[3], sys.argv[1])

# Total Background Uncerta
BackUncert          = NormalisationSyst + MultiJetCalibrea

# define the uncertainties for pT
if(sys.argv[6] == "pT"):
    if sys.argv[5] == "el":
        IdUncertai       = ClassUncer.UncertSF(data, Signal, Signal_Id,     sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3])
        CalibrationUncer = ClassUncer.CalibrationVariat(Signal, sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[6])
    if sys.argv[5] == "mu":
        IdUncertai       = ClassUncer.UncertSF(data, Signal, Signal_ttva,     sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3])
        CalibrationUncer = ClassUncer.CalibrationVariatmu(Signal, sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[6])

# define the uncertainties for Eta
if(sys.argv[6] == "Eta"):
    if sys.argv[5] == "el":
        IdUncertai       = ClassUncer.UncertSF(data, Signal, Signal_Id,     sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3])
        CalibrationUncer = ClassUncer.CalibrationVariat(Signal, sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[6])
    if sys.argv[5] == "mu":
        IdUncertai       = ClassUncer.UncertSF(data, Signal, Signal_ttva,     sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3])
        CalibrationUncer = ClassUncer.CalibrationVariatmu(Signal, sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[6])

# define the different source of uncertainties:
IsoUncertai       = ClassUncer.UncertSF(data, Signal, Signal_Iso,    sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3])
TrigUncertai      = ClassUncer.UncertSF(data, Signal, Signal_Trig,   sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3])
RecoUncertai      = ClassUncer.UncertSF(data, Signal, Signal_recoSF, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3])
SFUncertainty     = ClassUncer.TotalScaleFacUnceEl(Signal, IsoUncertai, TrigUncertai, RecoUncertai, IdUncertai, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3])
RecoilUncertainty = ClassUncer.Recoil(Signal, 		   sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[6])

# define the total uncertainties plot:
ClassUncer.PlotTotalUncerEl(Signal, data, BackUncert, SFUncertainty, CalibrationUncer, RecoilUncertainty, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3])

print("end")
os._exit(0)
