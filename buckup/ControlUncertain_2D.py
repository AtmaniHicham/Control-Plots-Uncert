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

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Define inputs
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Data   = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_DATA_" + sys.argv[3]+"/Nominal/DATA.root")
Signal = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_MC_"   + sys.argv[3]+"/Nominal/MC.root")
Bkg_W  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_MC_"   + sys.argv[3]+"/Background/merge/Background_W.root")
Bkg_T  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_MC_"   + sys.argv[3]+"/Background/merge/Background_Top.root")
Bkg_Z  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_MC_"   + sys.argv[3]+"/Background/merge/Background_Z.root")
Bkg_D  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_MC_"   + sys.argv[3]+"/Background/merge/Background_dilepton.root")

if   ("plusenu"   in sys.argv[1]):  MJvar = "Wep"
elif ("minusenu"  in sys.argv[1]):  MJvar = "Wem"
elif ("plusmunu"  in sys.argv[1]):  MJvar = "Wmup"
else:                               MJvar = "Wmum"

Bkg_MJ = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/"+sys.argv[3]+"/"+MJvar+".root")

# define the different sources of uncert:
Signal_Iso    = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_MC_" + sys.argv[3]+"/IsoSF/MC.root")
Signal_Trig   = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_MC_" + sys.argv[3]+"/TrigSF/MC.root")
Signal_recoSF = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_MC_" + sys.argv[3]+"/recoSF/MC.root")

if sys.argv[5] == "el":
    Signal_Id = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_w"+sys.argv[2]+"_MC_" + sys.argv[3]+"/IdSF/MC.root")

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

MJBackgrodHist  = ObjectClass.ReadHistogramMJ(        Bkg_MJ, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
MJBackgrodShape = ObjectClass.ReadHistogramMJShape(   Bkg_MJ, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
MJBackgrodExtra = ObjectClass.ReadHistogramMJExtrap(  Bkg_MJ, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
MJBackgroduTSli = ObjectClass.ReadHistogramMJuTSlice( Bkg_MJ, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )

MJUncertainty   = ObjectClass.MJHistUncertainties(    MJBackgrodHist, MJBackgrodShape, MJBackgrodExtra, MJBackgroduTSli)
MJBackUncerta   = ObjectClass.BackgroundUncer(        Bkg_W, Bkg_T, Bkg_Z, Bkg_D, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
MJLumiUncerta   = ObjectClass.LuminosityUncer(        SignalContent, Bkg_W, Bkg_T, Bkg_Z, Bkg_D, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )

BackUncertainty = MJUncertainty + MJBackUncerta + MJLumiUncerta

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Read Histograms for electron calibration
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if sys.argv[5] == "el":
    CalibrationUncer = ObjectClass.ReadHistogramCalibratiion( Signal, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6], "Pt",  sys.argv[3] )
if sys.argv[5] == "mu":
    IdUncertai = np.zeros(42)
    CalibrationUncer = np.zeros(42)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Read Histograms for recoil calibration
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

RecoilUncer = ObjectClass.ReadHistogramRecoil( Signal, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6], "Pt",  sys.argv[3] )

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Read Histograms for SF
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

UncertIso     = ObjectClass.ReadHistogramSF( Signal, Signal_Iso,    sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
UncertTrig    = ObjectClass.ReadHistogramSF( Signal, Signal_Trig,   sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
UncertrecoSF  = ObjectClass.ReadHistogramSF( Signal, Signal_recoSF, sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )
if sys.argv[5] == "el":
    UncertID  = ObjectClass.ReadHistogramSF( Signal, Signal_Id,     sys.argv[4], sys.argv[1], sys.argv[5], sys.argv[6],  "Pt",  sys.argv[3] )

if sys.argv[5] == "el":     
    SFUncertainty = UncertIso + UncertTrig + UncertrecoSF + UncertID
else:                       
    SFUncertainty = UncertIso + UncertTrig + UncertrecoSF

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
