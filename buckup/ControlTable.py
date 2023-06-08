#!/usr/bin/env python
# -*-coding:Latin-1 -*
from math import *

import ROOT
import ROOT as root
import matplotlib.pyplot as plt
import numpy as np

from ROOT 			import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TH1
from source.TableClasse 	import TableClasse

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------  5 TeV  -----------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

channel             = "Wplusenu"
Energy              = "5TeV"
Indice              = "$W^{+}$ $\\rightarrow$ $e^{+}$ $\\nu$, 5TeV"
data                = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_DATA_5TeV/Nominal/DATA.root")
Signal              = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_5TeV/Nominal/MC.root")
Background_Top      = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_5TeV/Background/merge/Background_Top.root")
Background_diboson  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_5TeV/Background/merge/Background_dilepton.root")
Background_W        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_5TeV/Background/merge/Background_W.root")
Background_Z        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_5TeV/Background/merge/Background_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/5TeV/Wep.root")
TableClasse1         = TableClasse()
print(Energy, "  ",channel)
TableClasse1.TablepTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)


channel             = "Wminusenu"
Energy              = "5TeV"
Indice              = "W^{-}#rightarrow e^{-}#nu, 5TeV"
Indice              = "$W^{-}$ $\\rightarrow$ $e^{-}$ $\\nu$, 5TeV"
data                = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_DATA_5TeV/Nominal/DATA.root")
Signal              = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_5TeV/Nominal/MC.root")
Background_Top      = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_5TeV/Background/merge/Background_Top.root")
Background_diboson  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_5TeV/Background/merge/Background_dilepton.root")
Background_W        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_5TeV/Background/merge/Background_W.root")
Background_Z        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_5TeV/Background/merge/Background_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/5TeV/Wem.root")
TableClasse2         = TableClasse()
print(Energy, "  ",channel)
TableClasse2.TablepTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)


channel             = "Wminusmunu"
Energy              = "5TeV"
Indice              = "$W^{-}$ $\\rightarrow$ $\\mu^{-}$ $\\nu$, 5TeV"
data                = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_DATA_5TeV/Nominal/DATA.root")
Signal              = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_5TeV/Nominal/MC.root")
Background_Top      = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_5TeV/Background/merge/Background_Top.root")
Background_diboson  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_5TeV/Background/merge/Background_dilepton.root")
Background_W        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_5TeV/Background/merge/Background_W.root")
Background_Z        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_5TeV/Background/merge/Background_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/5TeV/Wmum.root")
TableClasse3         = TableClasse()
print(Energy, "  ",channel)
TableClasse3.TablepTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)


channel             = "Wplusmunu"
Energy              = "5TeV"
Indice              = "$W^{+}$ $\\rightarrow$ $\\mu^{+}$ $\\nu$, 5TeV"
data                = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_DATA_5TeV/Nominal/DATA.root")
Signal              = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_5TeV/Nominal/MC.root")
Background_Top      = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_5TeV/Background/merge/Background_Top.root")
Background_diboson  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_5TeV/Background/merge/Background_dilepton.root")
Background_W        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_5TeV/Background/merge/Background_W.root")
Background_Z        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_5TeV/Background/merge/Background_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/5TeV/Wmup.root")
TableClasse4         = TableClasse()
print(Energy, "  ",channel)
TableClasse4.TablepTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------  13 TeV  ----------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

channel             = "Wplusenu"
Energy              = "13TeV"
Indice              = "$W^{+}$ $\\rightarrow$ $e^{+}$ $\\nu$, 13TeV"
data                = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_DATA_13TeV/Nominal/DATA.root")
Signal              = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_13TeV/Nominal/MC.root")
Background_Top      = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_13TeV/Background/merge/Background_Top.root")
Background_diboson  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_13TeV/Background/merge/Background_dilepton.root")
Background_W        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_13TeV/Background/merge/Background_W.root")
Background_Z        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusenu_MC_13TeV/Background/merge/Background_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/13TeV/Wep.root")
TableClasse1         = TableClasse()
TableClasse1.TablepTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)


channel             = "Wminusenu"
Energy              = "13TeV"
Indice              = "W^{-}#rightarrow e^{-}#nu, 13TeV"
Indice              = "$W^{-}$ $\\rightarrow$ $e^{-}$ $\\nu$, 13TeV"
data                = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_DATA_13TeV/Nominal/DATA.root")
Signal              = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_13TeV/Nominal/MC.root")
Background_Top      = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_13TeV/Background/merge/Background_Top.root")
Background_diboson  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_13TeV/Background/merge/Background_dilepton.root")
Background_W        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_13TeV/Background/merge/Background_W.root")
Background_Z        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusenu_MC_13TeV/Background/merge/Background_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/13TeV/Wem.root")
TableClasse2         = TableClasse()
TableClasse2.TablepTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)


channel             = "Wminusmunu"
Energy              = "13TeV"
Indice              = "$W^{-}$ $\\rightarrow$ $\\mu^{-}$ $\\nu$, 13TeV"
data                = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_DATA_13TeV/Nominal/DATA.root")
Signal              = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_13TeV/Nominal/MC.root")
Background_Top      = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_13TeV/Background/merge/Background_Top.root")
Background_diboson  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_13TeV/Background/merge/Background_dilepton.root")
Background_W        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_13TeV/Background/merge/Background_W.root")
Background_Z        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wminusmunu_MC_13TeV/Background/merge/Background_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/13TeV/Wmum.root")
TableClasse3         = TableClasse()
TableClasse3.TablepTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)


channel             = "Wplusmunu"
Energy              = "13TeV"
Indice              = "$W^{+}$ $\\rightarrow$ $\\mu^{+}$ $\\nu$, 13TeV"
data                = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_DATA_13TeV/Nominal/DATA.root")
Signal              = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_13TeV/Nominal/MC.root")
Background_Top      = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_13TeV/Background/merge/Background_Top.root")
Background_diboson  = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_13TeV/Background/merge/Background_dilepton.root")
Background_W        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_13TeV/Background/merge/Background_W.root")
Background_Z        = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/DATA_Xs/WCrossSections_wplusmunu_MC_13TeV/Background/merge/Background_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/sps/atlas/h/hatmani/DATA/MJbkg/13TeV/Wmup.root")
TableClasse4         = TableClasse()
TableClasse4.TablepTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)






























