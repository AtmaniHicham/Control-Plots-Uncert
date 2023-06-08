#!/usr/bin/env python
# -*-coding:Latin-1 -*
from math import *

import ROOT
import ROOT as root
import csv
import matplotlib.pyplot as plt
import numpy as np
import atlasplots as aplt
import pandas as pd
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TH1
from array import array
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TLatex, TChain

from source.PlottingClass import PlottingCla


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Wminusmunu  -- 5 TeV
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

channel				= "Wminusmunu"
Energy 				= "5TeV"
Indice 				= "W^{-}#rightarrow #mu^{-}#nu, 5.02 TeV, 258.4 pb^{-1}"
Indic 				= "W^{-}#rightarrow #mu^{-}#nu"
data 				= ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_DATA_5TeV/Nominal/DATA.root")
Signal 				= ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_5TeV/Nominal/MC.root")
Background_Top 		= ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_5TeV/Nominal/merge/Nominal_Top.root")
Background_diboson 	= ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_5TeV/Nominal/merge/Nominal_dilepton.root")
Background_W 		= ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_5TeV/Nominal/merge/Nominal_W.root")
Background_Z 		= ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_5TeV/Nominal/merge/Nominal_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/5TeV/Wmum.root")

ClassPlotting = PlottingCla()

pTBand              = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/pT_Wminusmunu_5TeV.csv").values.flatten().tolist()
EtaBand             = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/Eta_Wminusmunu_5TeV.csv").values.flatten().tolist()
EtaBand_2D          = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/2D_Eta_Wminusmunu_5TeV.csv").values.flatten().tolist()
MJBackgrodHist      = ClassPlotting.ReadHistogramMJ(   Background_MiltiJet, Indice, channel, "mu", "pT",  "Pt",   Energy)

ClassPlotting.PlottingMigration(     data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "pT",  "Pt",   Energy)
ClassPlotting.PlottingMigration(     data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "Eta", "Pt",   Energy)
ClassPlotting.Plotting(              data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "pT",  "Pt",   Energy, pTBand)
ClassPlotting.Plotting(              data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "Eta", "Eta",  Energy, EtaBand)
ClassPlotting.Plotting2dim(          data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, MJBackgrodHist, Indice, channel, "mu", "Eta", "Eta",  Energy, EtaBand_2D)
ClassPlotting.PlottingMigration2dim( data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "Eta", "Eta",  Energy)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Wplusmunu  -- 5 TeV
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

channel             = "Wplusmunu"
Energy              = "5TeV"
Indice              = "W^{+}#rightarrow #mu^{+}#nu, 5.02 TeV, 258.4 pb^{-1}"
Indic               = "W^{+}#rightarrow #mu^{+}#nu"
data                = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_DATA_5TeV/Nominal/DATA.root")
Signal              = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_5TeV/Nominal/MC.root")
Background_Top      = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_5TeV/Nominal/merge/Nominal_Top.root")
Background_diboson  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_5TeV/Nominal/merge/Nominal_dilepton.root")
Background_W        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_5TeV/Nominal/merge/Nominal_W.root")
Background_Z        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_5TeV/Nominal/merge/Nominal_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/5TeV/Wmup.root")

ClassPlotting       = PlottingCla()

pTBand              = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/pT_Wplusmunu_5TeV.csv").values.flatten().tolist()
EtaBand             = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/Eta_Wplusmunu_5TeV.csv").values.flatten().tolist()
EtaBand_2D          = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/2D_Eta_Wplusmunu_5TeV.csv").values.flatten().tolist()
MJBackgrodHist      = ClassPlotting.ReadHistogramMJ(   Background_MiltiJet, Indice, channel, "mu", "pT",  "Pt",   Energy)


ClassPlotting.PlottingMigration(       data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "pT",  "Pt",  Energy)
ClassPlotting.PlottingMigration(       data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "Eta",  "Pt",  Energy)
ClassPlotting.Plotting(                 data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "pT",  "Pt",   Energy, pTBand)
ClassPlotting.Plotting(                 data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "Eta", "Eta",  Energy, EtaBand)
ClassPlotting.Plotting2dim(		        data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, MJBackgrodHist, Indice, channel, "mu", "Eta", "Eta",  Energy, EtaBand_2D)
ClassPlotting.PlottingMigration2dim(   data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "Eta", "Eta",  Energy)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Wplusenu  -- 5 TeV
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

channel             = "Wplusenu"
Energy              = "5TeV"
Indice              = "W^{+}#rightarrow e^{+}#nu, 5.02 TeV, 258.4 pb^{-1}"
Indic               = "W^{+}#rightarrow e^{+}#nu"
data                = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_DATA_5TeV/Nominal/DATA.root")
Signal              = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_5TeV/Nominal/MC.root")
Background_Top      = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_5TeV/Nominal/merge/Nominal_Top.root")
Background_diboson  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_5TeV/Nominal/merge/Nominal_dilepton.root")
Background_W        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_5TeV/Nominal/merge/Nominal_W.root")
Background_Z        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_5TeV/Nominal/merge/Nominal_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/5TeV/Wep.root")

ClassPlotting       = PlottingCla()

pTBand              = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/pT_Wplusenu_5TeV.csv").values.flatten().tolist()
EtaBand             = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/Eta_Wplusenu_5TeV.csv").values.flatten().tolist()
EtaBand_2D          = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/2D_Eta_Wplusenu_5TeV.csv").values.flatten().tolist()
MJBackgrodHist      = ClassPlotting.ReadHistogramMJ(   Background_MiltiJet, Indice, channel, "mu", "pT",  "Pt",   Energy)

ClassPlotting.PlottingMigration(       data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "el", "pT",  "Pt",  Energy)
ClassPlotting.PlottingMigration(       data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "el", "Eta",  "Pt",  Energy)
ClassPlotting.Plotting(                 data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "el", "pT",  "Pt",   Energy, pTBand)
ClassPlotting.Plotting(                 data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "el", "Eta", "Eta",  Energy, EtaBand)
ClassPlotting.Plotting2dim(		    data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, MJBackgrodHist, Indice, channel, "mu", "Eta", "Eta",  Energy, EtaBand_2D)
ClassPlotting.PlottingMigration2dim(  	data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "Eta", "Eta",  Energy)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Wminusenu  -- 5 TeV
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

channel             = "Wminusenu"
Energy              = "5TeV"
Indice              = "W^{-}#rightarrow e^{-}#nu, 5.02 TeV, 258.4 pb^{-1}"
Indic               = "W^{-}#rightarrow e^{-}#nu"
data                = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_DATA_5TeV/Nominal/DATA.root")
Signal              = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_5TeV/Nominal/MC.root")
Background_Top      = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_5TeV/Nominal/merge/Nominal_Top.root")
Background_diboson  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_5TeV/Nominal/merge/Nominal_dilepton.root")
Background_W        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_5TeV/Nominal/merge/Nominal_W.root")
Background_Z        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_5TeV/Nominal/merge/Nominal_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/5TeV/Wem.root")

ClassPlotting       = PlottingCla()

pTBand              = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/pT_Wminusenu_5TeV.csv").values.flatten().tolist()
EtaBand             = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/Eta_Wminusenu_5TeV.csv").values.flatten().tolist()
EtaBand_2D          = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/2D_Eta_Wminusenu_5TeV.csv").values.flatten().tolist()
MJBackgrodHist      = ClassPlotting.ReadHistogramMJ(   Background_MiltiJet, Indice, channel, "mu", "pT",  "Pt",   Energy)

ClassPlotting.PlottingMigration(       data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "el", "pT",  "Pt",  Energy)
ClassPlotting.PlottingMigration(       data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "el", "Eta",  "Pt",  Energy)
ClassPlotting.Plotting(                 data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "el", "pT",  "Pt",   Energy, pTBand)
ClassPlotting.Plotting(                 data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "el", "Eta", "Eta",  Energy, EtaBand)
ClassPlotting.Plotting2dim(		    data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, MJBackgrodHist, Indice, channel, "mu", "Eta", "Eta",  Energy, EtaBand_2D)
ClassPlotting.PlottingMigration2dim(  	data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "Eta", "Eta",  Energy)

# ***************************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************************

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Wminusmunu  -- 13TeV
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

channel             = "Wminusmunu"
Energy              = "13TeV"
Indice              = "W^{-}#rightarrow #mu^{-}#nu, 13 TeV, 335 pb^{-1}"
Indic               = "W^{-}#rightarrow #mu^{-}#nu"
data                = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_DATA_13TeV/Nominal/DATA.root")
Signal              = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_13TeV/Nominal/MC.root")
Background_Top      = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_13TeV/Nominal/merge/Nominal_Top.root")
Background_diboson  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_13TeV/Nominal/merge/Nominal_dilepton.root")
Background_W        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_13TeV/Nominal/merge/Nominal_W.root")
Background_Z        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_13TeV/Nominal/merge/Nominal_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/13TeV/Wmum.root")

ClassPlotting       = PlottingCla()

pTBand              = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/pT_Wminusmunu_13TeV.csv").values.flatten().tolist()
EtaBand             = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/Eta_Wminusmunu_13TeV.csv").values.flatten().tolist()
EtaBand_2D          = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/2D_Eta_Wminusmunu_13TeV.csv").values.flatten().tolist()
MJBackgrodHist      = ClassPlotting.ReadHistogramMJ(   Background_MiltiJet, Indice, channel, "mu", "pT",  "Pt",   Energy)

ClassPlotting.PlottingMigration(       data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "pT",  "Pt",  Energy)
ClassPlotting.PlottingMigration(       data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "Eta",  "Pt",  Energy)
ClassPlotting.Plotting(                 data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "pT",  "Pt",   Energy, pTBand)
ClassPlotting.Plotting(                 data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "Eta", "Eta",  Energy, EtaBand)
ClassPlotting.Plotting2dim(		    data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, MJBackgrodHist, Indice, channel, "mu", "Eta", "Eta",  Energy, EtaBand_2D)
ClassPlotting.PlottingMigration2dim(  	data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "Eta", "Eta",  Energy)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Wplusmunu  -- 13TeV
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

channel             = "Wplusmunu"
Energy              = "13TeV"
Indice              = "W^{+}#rightarrow #mu^{+}#nu, 13 TeV, 335 pb^{-1}"
Indic               = "W^{+}#rightarrow #mu^{+}#nu"
data                = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_DATA_13TeV/Nominal/DATA.root")
Signal              = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_13TeV/Nominal/MC.root")
Background_Top      = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_13TeV/Nominal/merge/Nominal_Top.root")
Background_diboson  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_13TeV/Nominal/merge/Nominal_dilepton.root")
Background_W        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_13TeV/Nominal/merge/Nominal_W.root")
Background_Z        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_13TeV/Nominal/merge/Nominal_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/13TeV/Wmup.root")

ClassPlotting       = PlottingCla()

pTBand              = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/pT_Wplusmunu_13TeV.csv").values.flatten().tolist()
EtaBand             = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/Eta_Wplusmunu_13TeV.csv").values.flatten().tolist()
EtaBand_2D          = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/2D_Eta_Wplusmunu_13TeV.csv").values.flatten().tolist()
MJBackgrodHist      = ClassPlotting.ReadHistogramMJ(   Background_MiltiJet, Indice, channel, "mu", "pT",  "Pt",   Energy)

ClassPlotting.PlottingMigration(       data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "pT",  "Pt",  Energy)
ClassPlotting.PlottingMigration(       data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "Eta",  "Pt",  Energy)
ClassPlotting.Plotting(                 data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "pT",  "Pt",   Energy, pTBand)
ClassPlotting.Plotting(                 data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "Eta", "Eta",  Energy, EtaBand)
ClassPlotting.Plotting2dim(		    data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, MJBackgrodHist, Indice, channel, "mu", "Eta", "Eta",  Energy, EtaBand_2D)
ClassPlotting.PlottingMigration2dim(  	data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "Eta", "Eta",  Energy)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Wplusenu  -- 13TeV
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

channel             = "Wplusenu"
Energy              = "13TeV"
Indice              = "W^{+}#rightarrow e^{+}#nu, 13 TeV, 335 pb^{-1}"
Indic               = "W^{+}#rightarrow e^{+}#nu"
data                = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_DATA_13TeV/Nominal/DATA.root")
Signal              = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_13TeV/Nominal/MC.root")
Background_Top      = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_13TeV/Nominal/merge/Nominal_Top.root")
Background_diboson  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_13TeV/Nominal/merge/Nominal_dilepton.root")
Background_W        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_13TeV/Nominal/merge/Nominal_W.root")
Background_Z        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_13TeV/Nominal/merge/Nominal_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/13TeV/Wep.root")

ClassPlotting       = PlottingCla()

pTBand              = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/pT_Wplusenu_13TeV.csv").values.flatten().tolist()
EtaBand             = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/Eta_Wplusenu_13TeV.csv").values.flatten().tolist()
EtaBand_2D          = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/2D_Eta_Wplusenu_13TeV.csv").values.flatten().tolist()
MJBackgrodHist      = ClassPlotting.ReadHistogramMJ(   Background_MiltiJet, Indice, channel, "mu", "pT",  "Pt",   Energy)

ClassPlotting.PlottingMigration(       data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "el", "pT",  "Pt",  Energy)
ClassPlotting.PlottingMigration(       data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "el", "Eta",  "Pt",  Energy)
ClassPlotting.Plotting(                 data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "el", "pT",  "Pt",   Energy, pTBand)
ClassPlotting.Plotting(                 data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "el", "Eta", "Eta",  Energy, EtaBand)
ClassPlotting.Plotting2dim(		    data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, MJBackgrodHist, Indice, channel, "mu", "Eta", "Eta",  Energy, EtaBand_2D)
ClassPlotting.PlottingMigration2dim(  	data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "Eta", "Eta",  Energy)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Wminusenu  -- 13TeV
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

channel             = "Wminusenu"
Energy              = "13TeV"
Indice              = "W^{-}#rightarrow e^{-}#nu, 13 TeV, 335 pb^{-1}"
Indic               = "W^{-}#rightarrow e^{-}#nu"
data                = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_DATA_13TeV/Nominal/DATA.root")
Signal              = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_13TeV/Nominal/MC.root")
Background_Top      = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_13TeV/Nominal/merge/Nominal_Top.root")
Background_diboson  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_13TeV/Nominal/merge/Nominal_dilepton.root")
Background_W        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_13TeV/Nominal/merge/Nominal_W.root")
Background_Z        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs_Origin/WCrossSections_wminusenu_MC_13TeV/Nominal/merge/Nominal_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/13TeV/Wem.root")

ClassPlotting       = PlottingCla()

pTBand              = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/pT_Wminusenu_13TeV.csv").values.flatten().tolist()
EtaBand             = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/Eta_Wminusenu_13TeV.csv").values.flatten().tolist()
EtaBand_2D          = pd.read_csv("/sps/atlas/h/hatmani/W_xs/ControlPlots/Output/UncertaintyBand/2D_Eta_Wminusenu_13TeV.csv").values.flatten().tolist()
MJBackgrodHist      = ClassPlotting.ReadHistogramMJ(   Background_MiltiJet, Indice, channel, "mu", "pT",  "Pt",   Energy)

ClassPlotting.PlottingMigration(       data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "el", "pT",  "Pt",  Energy)
ClassPlotting.PlottingMigration(       data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "el", "Eta",  "Pt",  Energy)
ClassPlotting.Plotting(                 data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "el", "pT",  "Pt",   Energy, pTBand)
ClassPlotting.Plotting(                 data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "el", "Eta", "Eta",  Energy, EtaBand)
ClassPlotting.Plotting2dim(		    data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, MJBackgrodHist, Indice, channel, "mu", "Eta", "Eta",  Energy, EtaBand_2D)
ClassPlotting.PlottingMigration2dim(  	data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, "mu", "Eta", "Eta",  Energy)

