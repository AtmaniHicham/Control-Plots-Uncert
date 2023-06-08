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

from source.UncertaintyClass_2D import UncertClass

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


def CrossSectionNormalisa(channel, NormalisationPath):
    lepton = "ee"
    if "munu" in channel: lepton = "mumu"
    NameVector = ["ttbar", "singletop", "Wtop", "Wminusenu", "Wplusenu", "Wminusmunu", "Wplusmunu", "Wplustaunu", "Wminustaunu", "Z"+lepton, "Ztautau", "ZZ", "WZ", "WW", "multijet"]

    # --------------- pt1 
    Variation1   = []
    DireName    = channel + "Selection_NormVariations"
    files       = os.listdir(NormalisationPath)
    for i in files:
        rootFile    = ROOT.TFile.Open(NormalisationPath+"/"+i)
        HistNominal = rootFile.Get(DireName+"/Lepton_Eta_Reco_pt1_cut7_Nom")
        for j in NameVector:
            HistVaried   = rootFile.Get(DireName+"/Lepton_Eta_Reco_pt1_cut7_Xsec_up_"+j)
            if HistVaried == None: continue
            else: break
        Variation1.append(   histtoarray(HistVaried) -  histtoarray(HistNominal)   )

    # --------------- pt2
    Variation2   = []
    DireName    = channel + "Selection_NormVariations"
    files       = os.listdir(NormalisationPath)
    for i in files:
        rootFile    = ROOT.TFile.Open(NormalisationPath+"/"+i)
        HistNominal = rootFile.Get(DireName+"/Lepton_Eta_Reco_pt2_cut7_Nom")
        for j in NameVector:
            HistVaried   = rootFile.Get(DireName+"/Lepton_Eta_Reco_pt2_cut7_Xsec_up_"+j)
            if HistVaried == None: continue
            else: break
        Variation2.append(   histtoarray(HistVaried) -  histtoarray(HistNominal)   )

    # --------------- pt3
    Variation3   = []
    DireName    = channel + "Selection_NormVariations"
    files       = os.listdir(NormalisationPath)
    for i in files:
        rootFile    = ROOT.TFile.Open(NormalisationPath+"/"+i)
        HistNominal = rootFile.Get(DireName+"/Lepton_Eta_Reco_pt3_cut7_Nom")
        for j in NameVector:
            HistVaried   = rootFile.Get(DireName+"/Lepton_Eta_Reco_pt3_cut7_Xsec_up_"+j)
            if HistVaried == None: continue
            else: break
        Variation3.append(   histtoarray(HistVaried) -  histtoarray(HistNominal)   )

    # --------------- pt4
    Variation4   = []
    DireName    = channel + "Selection_NormVariations"
    files       = os.listdir(NormalisationPath)
    for i in files:
        rootFile    = ROOT.TFile.Open(NormalisationPath+"/"+i)
        HistNominal = rootFile.Get(DireName+"/Lepton_Eta_Reco_pt4_cut7_Nom")
        for j in NameVector:
            HistVaried   = rootFile.Get(DireName+"/Lepton_Eta_Reco_pt4_cut7_Xsec_up_"+j)
            if HistVaried == None: continue
            else: break
        Variation4.append(   histtoarray(HistVaried) -  histtoarray(HistNominal)   )

    # --------------- pt5 
    Variation5   = []
    DireName    = channel + "Selection_NormVariations"
    files       = os.listdir(NormalisationPath)
    for i in files:
        rootFile    = ROOT.TFile.Open(NormalisationPath+"/"+i)
        HistNominal = rootFile.Get(DireName+"/Lepton_Eta_Reco_pt5_cut7_Nom")
        for j in NameVector:
            HistVaried   = rootFile.Get(DireName+"/Lepton_Eta_Reco_pt5_cut7_Xsec_up_"+j)
            if HistVaried == None: continue
            else: break
        Variation5.append(   histtoarray(HistVaried) -  histtoarray(HistNominal)   )

    # --------------- pt6 
    Variation6   = []
    DireName    = channel + "Selection_NormVariations"
    files       = os.listdir(NormalisationPath)
    for i in files:
        rootFile    = ROOT.TFile.Open(NormalisationPath+"/"+i)
        HistNominal = rootFile.Get(DireName+"/Lepton_Eta_Reco_pt6_cut7_Nom")
        for j in NameVector:
            HistVaried   = rootFile.Get(DireName+"/Lepton_Eta_Reco_pt6_cut7_Xsec_up_"+j)
            if HistVaried == None: continue
            else: break
        Variation6.append(   histtoarray(HistVaried) -  histtoarray(HistNominal)   )

    Variation1[0] = Variation1[0]*Variation1[0]
    for i in range(1, len(Variation1)):
        Variation1[0] = Variation1[0] + Variation1[i]*Variation1[i]
    Variation1[0] = np.sqrt(Variation1[0])

    Variation2[0] = Variation2[0]*Variation2[0]
    for i in range(1, len(Variation2)):
        Variation2[0] = Variation2[0] + Variation2[i]*Variation2[i]
    Variation2[0] = np.sqrt(Variation2[0])

    Variation3[0] = Variation3[0]*Variation3[0]
    for i in range(1, len(Variation3)):
        Variation3[0] = Variation3[0] + Variation3[i]*Variation3[i]
    Variation3[0] = np.sqrt(Variation3[0])

    Variation4[0] = Variation4[0]*Variation4[0]
    for i in range(1, len(Variation4)):
        Variation4[0] = Variation4[0] + Variation4[i]*Variation4[i]
    Variation4[0] = np.sqrt(Variation4[0])

    Variation5[0] = Variation5[0]*Variation5[0]
    for i in range(1, len(Variation5)):
        Variation5[0] = Variation5[0] + Variation5[i]*Variation5[i]
    Variation5[0] = np.sqrt(Variation5[0])

    Variation6[0] = Variation6[0]*Variation6[0]
    for i in range(1, len(Variation6)):
        Variation6[0] = Variation6[0] + Variation6[i]*Variation6[i]
    Variation6[0] = np.sqrt(Variation6[0])

    NormalisationTotal  = np.concatenate((Variation1[0], Variation2[0], Variation3[0], Variation4[0], Variation5[0], Variation6[0]))

    return NormalisationTotal

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Define inputs
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Data   = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_DATA_" + sys.argv[3]+"/Nominal/DATA.root")
Signal = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_MC_"   + sys.argv[3]+"/Nominal/MC.root")
Bkg_W  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_MC_"   + sys.argv[3]+"/Nominal/merge/Nominal_W.root")
Bkg_T  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_MC_"   + sys.argv[3]+"/Nominal/merge/Nominal_Top.root")
Bkg_Z  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_MC_"   + sys.argv[3]+"/Nominal/merge/Nominal_Z.root")
Bkg_D  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_MC_"   + sys.argv[3]+"/Nominal/merge/Nominal_dilepton.root")

if   ("plusenu"   in sys.argv[1]):  MJvar = "Wep"
elif ("minusenu"  in sys.argv[1]):  MJvar = "Wem"
elif ("plusmunu"  in sys.argv[1]):  MJvar = "Wmup"
else:                               MJvar = "Wmum"

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
#  Define Class for Uncertainties
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ObjectClass    = UncertClass()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Read Histograms for data and simulation
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

DataContent   = ObjectClass.ReadHistogramData(        Data,   sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
SignalContent = ObjectClass.ReadHistogramSignal(      Signal, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )

DataError     = ObjectClass.ReadHistogramDataError(   Data,   sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
SignalError   = ObjectClass.ReadHistogramSignalError( Signal, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Read Histograms for background uncertainties
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

MJBackgrodHist      = ObjectClass.ReadHistogramMJ(        Bkg_MJ, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
MJBackgrodHistStat  = ObjectClass.ReadHistogramMJStat(    Bkg_MJ, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
MJBackgrodShape     = ObjectClass.ReadHistogramMJShape(   Bkg_MJ, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
MJBackgrodExtra     = ObjectClass.ReadHistogramMJExtrap(  Bkg_MJ, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
MJBackgroduTSli     = ObjectClass.ReadHistogramMJuTSlice( Bkg_MJ, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )


# MJ Uncertainties
Error1          = np.array(MJBackgrodShape - MJBackgrodHist)
Error2          = np.array(MJBackgrodExtra - MJBackgrodHist)
Error3          = np.array(MJBackgroduTSli - MJBackgrodHist)
Error4          = np.array(MJBackgrodHistStat)
MJUncertainty   = np.sqrt(Error1*Error1 + Error2*Error2 + Error3*Error3 + Error4*Error4)

#define the normalisation systematics
NormalisationPath  = "/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_MC_"+sys.argv[3]+"/Normalization/"
NormalisationSyst  = CrossSectionNormalisa(sys.argv[1], NormalisationPath)

# total Uncertainties:
BackUncertainty    = np.sqrt(   NormalisationSyst*NormalisationSyst +  MJUncertainty*MJUncertainty  )

#MJUncertainty   = ObjectClass.MJHistUncertainties(    MJBackgrodHist, MJBackgrodShape, MJBackgrodExtra, MJBackgroduTSli)
#MJBackUncerta   = ObjectClass.BackgroundUncer(        Bkg_W, Bkg_T, Bkg_Z, Bkg_D, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
#MJLumiUncerta   = ObjectClass.LuminosityUncer(        SignalContent, Bkg_W, Bkg_T, Bkg_Z, Bkg_D, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )

#BackUncertainty = MJUncertainty + MJBackUncerta + MJLumiUncerta

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Read Histograms for electron and muon calibration
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if sys.argv[5] == "el":
    CalibrationUncer = ObjectClass.ReadHistogramCalibratiion( Signal, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6], "Pt",  sys.argv[3] )
if sys.argv[5] == "mu":
    CalibrationUncer = ObjectClass.ReadHistogramCalibratiionMuons( Signal, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6], "Pt",  sys.argv[3] )

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Read Histograms for recoil calibration
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

RecoilUncer = ObjectClass.ReadHistogramRecoil( Signal, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6], "Pt",  sys.argv[3] )

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Read Histograms for SF
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

UncertIso       = ObjectClass.ReadHistogramSF( Signal, Signal_Iso,      sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
UncertTrig      = ObjectClass.ReadHistogramSF( Signal, Signal_Trig,     sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
UncertrecoSF    = ObjectClass.ReadHistogramSF( Signal, Signal_recoSF,   sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )

if sys.argv[5] == "el":
    UncertID    = ObjectClass.ReadHistogramSF( Signal, Signal_Id,       sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
if sys.argv[5] == "mu":
    Uncertttva  = ObjectClass.ReadHistogramSF( Signal, Signal_ttva,     sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )


if sys.argv[5] == "el":     
    SFUncertainty = UncertIso + UncertTrig + UncertrecoSF + UncertID
else:                  
    SFUncertainty = UncertIso + UncertTrig + UncertrecoSF + Uncertttva

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Plotting for 2D
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Indice  = sys.argv[4]
channel = sys.argv[1]
lepton  = sys.argv[5]
var     = sys.argv[6]
multi   = "Pt"
Energy  = sys.argv[3]

ObjectClass.PlotTotalUncer(DataError, DataContent, SignalError, SignalContent, BackUncertainty, SFUncertainty, CalibrationUncer, RecoilUncer, Indice, channel, lepton, var, multi, Energy)

print("end")
os._exit(0)
