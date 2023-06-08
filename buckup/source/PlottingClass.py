#!/usr/bin/env python
# -*-coding:Latin-1 -*

from math import *

import ROOT
import ROOT as root
import matplotlib.pyplot as plt
import numpy as np
import atlasplots as aplt
import sys

from random import random
import numpy as np
import matplotlib.pyplot as plt

from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TH1, TGraph, TGraphErrors
from array import array
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TLatex, TChain


def rebinTheMultiJetBackground(nominal, histogram_MJ):

    nominal.SetBinContent(1, 0)
    nominal.SetBinContent(2, histogram_MJ.GetBinContent(26) + histogram_MJ.GetBinContent(27) +
                          histogram_MJ.GetBinContent(28) + histogram_MJ.GetBinContent(29) + histogram_MJ.GetBinContent(30))
    nominal.SetBinContent(3, histogram_MJ.GetBinContent(31) + histogram_MJ.GetBinContent(32) +
                          histogram_MJ.GetBinContent(33) + histogram_MJ.GetBinContent(34) + histogram_MJ.GetBinContent(35))
    nominal.SetBinContent(4, histogram_MJ.GetBinContent(36) + histogram_MJ.GetBinContent(37) +
                          histogram_MJ.GetBinContent(38) + histogram_MJ.GetBinContent(39) + histogram_MJ.GetBinContent(40))
    nominal.SetBinContent(5, histogram_MJ.GetBinContent(41) + histogram_MJ.GetBinContent(42) +
                          histogram_MJ.GetBinContent(43) + histogram_MJ.GetBinContent(44) + histogram_MJ.GetBinContent(45))
    nominal.SetBinContent(6, histogram_MJ.GetBinContent(46) + histogram_MJ.GetBinContent(47) +
                          histogram_MJ.GetBinContent(48) + histogram_MJ.GetBinContent(49) + histogram_MJ.GetBinContent(50))

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
    nominal.SetBinError(2, sqrt(pow(histogram_MJ.GetBinError(26), 2) + pow(histogram_MJ.GetBinError(27), 2) + pow(
        histogram_MJ.GetBinError(28), 2) + pow(histogram_MJ.GetBinError(29), 2) + pow(histogram_MJ.GetBinError(30), 2)))
    nominal.SetBinError(3, sqrt(pow(histogram_MJ.GetBinError(31), 2) + pow(histogram_MJ.GetBinError(32), 2) + pow(
        histogram_MJ.GetBinError(33), 2) + pow(histogram_MJ.GetBinError(34), 2) + pow(histogram_MJ.GetBinError(35), 2)))
    nominal.SetBinError(4, sqrt(pow(histogram_MJ.GetBinError(36), 2) + pow(histogram_MJ.GetBinError(37), 2) + pow(
        histogram_MJ.GetBinError(38), 2) + pow(histogram_MJ.GetBinError(39), 2) + pow(histogram_MJ.GetBinError(40), 2)))
    nominal.SetBinError(5, sqrt(pow(histogram_MJ.GetBinError(41), 2) + pow(histogram_MJ.GetBinError(42), 2) + pow(
        histogram_MJ.GetBinError(43), 2) + pow(histogram_MJ.GetBinError(44), 2) + pow(histogram_MJ.GetBinError(45), 2)))
    nominal.SetBinError(6, sqrt(pow(histogram_MJ.GetBinError(46), 2) + pow(histogram_MJ.GetBinError(47), 2) + pow(
        histogram_MJ.GetBinError(48), 2) + pow(histogram_MJ.GetBinError(49), 2) + pow(histogram_MJ.GetBinError(50), 2)))

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


class PlottingCla:
    """Classe représentant une personne"""

    def __init__(self):
        """Constructeur de notre classe"""

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def PlottingMigration(self, data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, lepton, var, multi, Energy):
        # Set the ATLAS Style
        aplt.set_atlas_style()

        # Migration Matrix
        Migration_hist = Signal.Get(
            channel+"Selection/Lepton_"+var+"_Reco_v_Truth_cut7")

        # Create a figure and axes
        fig, ax = aplt.subplots(1, 1, name="fig1", figsize=(800, 600))

        if "minus" in channel:
            Migration_hist.GetZaxis().SetRange(10, 7700)
        # Draw the histogram on these axes
        ax.plot2d(Migration_hist, "COLZ")

        if var == "pT":
            ax.set_xlim(25, 80)
            ax.set_ylim(25, 80)

        # Change pad margins to allow space for z-axis colour bar and for ATLAS label
        ax.set_pad_margins(right=0.20, top=0.08)

        # Set axis titles
        if var == "pT":
            ax.set_xlabel("p^{l}_{T}, Detector-level")
            ax.set_ylabel("p^{l}_{T}, Particle-level")
            ax.set_xlim(25, 80)
            ax.set_ylim(25, 80)
        if var == "Eta":
            ax.set_xlabel("\eta^{l}, Detector-level")
            ax.set_ylabel("\eta^{l}, Particle-level")
        ax.set_zlabel("", titleoffset=1.2)

        # Add the ATLAS Label
        aplt.atlas_label(ax.pad.GetLeftMargin(), 0.97,
                         text="Internal", align=13)
        ax.text(1 - ax.pad.GetRightMargin(), 0.97, Indice, size=22, align=33)

        if var == "pT":
            ax.set_xlim(25, 80)
            ax.set_ylim(25, 80)
        # Save the plot as a PDF
        fig.savefig("Output/Backgrounds/Migration_"+var +
                    "_"+Energy+"_lepton_"+channel+".pdf")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def Plotting(self, data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, lepton, var, multi, Energy, bandUncer):

        # Set the ATLAS Style
        aplt.set_atlas_style()

        # Create a figure and axes
        fig, (ax1, ax2) = aplt.ratio_plot(
            name="fig1", figsize=(800, 800), hspace=0.05)

        # define signal, data and background
        data_histO = data.Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")
        sig_histO = Signal.Get(channel+"Selection/Lepton_"+var+"_Reco_cut7")
        bkg_hist1O = Background_Top.Get(
            channel+"Selection/Lepton_"+var+"_Reco_cut7")
        bkg_hist2O = Background_diboson.Get(
            channel+"Selection/Lepton_"+var+"_Reco_cut7")
        bkg_hist3O = Background_W.Get(
            channel+"Selection/Lepton_"+var+"_Reco_cut7")
        bkg_hist4O = Background_Z.Get(
            channel+"Selection/Lepton_"+var+"_Reco_cut7")

        bin_boundaries = [0, 25, 30, 35, 40, 45, 50, 60, 80, 100]

        data_hist = TH1F("data_hist", "data_hist", len(
            bin_boundaries)-1, array('d', bin_boundaries))
        sig_hist = TH1F("sig_hist",  "sig_hist",  len(
            bin_boundaries)-1, array('d', bin_boundaries))
        bkg_hist1 = TH1F("bkg_hist1", "bkg_hist1", len(
            bin_boundaries)-1, array('d', bin_boundaries))
        bkg_hist2 = TH1F("bkg_hist2", "bkg_hist2", len(
            bin_boundaries)-1, array('d', bin_boundaries))
        bkg_hist3 = TH1F("bkg_hist3", "bkg_hist3", len(
            bin_boundaries)-1, array('d', bin_boundaries))
        bkg_hist4 = TH1F("bkg_hist4", "bkg_hist4", len(
            bin_boundaries)-1, array('d', bin_boundaries))

        for i in range(0, len(bin_boundaries)):
            data_hist.SetBinContent(i+1, data_histO.GetBinContent(i+1))
            sig_hist.SetBinContent(i+1,  sig_histO.GetBinContent(i+1))
            bkg_hist1.SetBinContent(i+1, bkg_hist1O.GetBinContent(i+1))
            bkg_hist2.SetBinContent(i+1, bkg_hist2O.GetBinContent(i+1))
            bkg_hist3.SetBinContent(i+1, bkg_hist3O.GetBinContent(i+1))
            bkg_hist4.SetBinContent(i+1, bkg_hist4O.GetBinContent(i+1))

            data_hist.SetBinError(i+1, data_histO.GetBinError(i+1))
            sig_hist.SetBinError(i+1,  sig_histO.GetBinError(i+1))
            bkg_hist1.SetBinError(i+1, bkg_hist1O.GetBinError(i+1))
            bkg_hist2.SetBinError(i+1, bkg_hist2O.GetBinError(i+1))
            bkg_hist3.SetBinError(i+1, bkg_hist3O.GetBinError(i+1))
            bkg_hist4.SetBinError(i+1, bkg_hist4O.GetBinError(i+1))

        print("hist/"+lepton+multi)

        bkg_MJ = (Background_MiltiJet.Get(
            "hist/"+lepton+multi)).Clone("bkg_MJ")
        if("pT" in var):
            histbg = (rebinTheMultiJetBackground(
                sig_hist.Clone(), bkg_MJ.Clone())).Clone("histbg")
        if("Eta" in var):
            histbg = bkg_MJ.Clone("histbg")

        bkg_hist5 = histbg.Clone("bkg_hist5")

        for i in range(0, bkg_hist5.GetNbinsX()):
            print(i+1, bkg_hist5.GetBinContent(i+1))
        print("channel : ", channel, bkg_hist5.Integral())
        print(bkg_hist5.GetNbinsX())

        # for i in range(0, bkg_hist5.GetNbinsX()):
        #    bkg_hist5.SetBinContent(i+1, histbg.GetBinContent(i+1))
        #    bkg_hist5.SetBinError(i+1, histbg.GetBinError(i+1))

        # Stack the background and signal histogra
        bkg_hist2.GetXaxis().SetRange(0, 70)
        bkg_hist1.GetXaxis().SetRange(0, 70)
        bkg_hist5.GetXaxis().SetRange(0, 70)
        bkg_hist4.GetXaxis().SetRange(0, 70)
        bkg_hist5.GetXaxis().SetRange(0, 70)
        sig_hist.GetXaxis().SetRange(0, 70)
        data_hist.GetXaxis().SetRange(0, 70)

        bkg_and_sig = root.THStack("bkg_and_sig", "")
        bkg_and_sig.Add(bkg_hist2)
        bkg_and_sig.Add(bkg_hist1)
        bkg_and_sig.Add(bkg_hist5)
        bkg_and_sig.Add(bkg_hist4)
        bkg_and_sig.Add(bkg_hist3)
        bkg_and_sig.Add(sig_hist)

        bkg_hist1.SetFillColor(root.kRed+1)
        bkg_hist2.SetFillColor(root.kGreen+1)
        bkg_hist3.SetFillColor(root.kMagenta+2)
        bkg_hist4.SetFillColor(root.kOrange+7)
        bkg_hist5.SetFillColor(root.kGray+1)

        sig_hist.SetFillColor(root.kAzure+1)

        # Draw the stacked histogram on these axes
        ax1.plot(bkg_and_sig)
        #bkg_and_sig.GetXaxis().SetLimits(0, 70)

        # Plot the MC stat error as a hatched band
        err_band = aplt.root_helpers.hist_to_graph(
            bkg_and_sig.GetStack().Last(),
            show_bin_width=True
        )

        ax1.set_yscale("log")
        ax1.plot(err_band, "2", fillcolor=1, fillstyle=3254, linewidth=0)

        # Plot the data as a graph
        ax1.set_ylim(10, 3400000)
        data_graph = aplt.root_helpers.hist_to_graph(data_hist)
        ax1.plot(data_graph, "P")

        if(var == "pT"):
            ax1.set_xlim(25, 100)

        # Use same x-range in lower axes as upper axes
        ax2.set_xlim(ax1.get_xlim())

        # Draw line at y=1 in ratio panel
        line = root.TLine(ax1.get_xlim()[0], 1, ax1.get_xlim()[1], 1)
        ax2.plot(line)

        # Plot the relative error on the ratio axes *******************************************************************************************************
        bkg_and_sigBand = bkg_and_sig.Clone("bkg_and_sigBand")

        err_band_ratio = aplt.root_helpers.hist_to_graph(
            bkg_and_sig.GetStack().Last(),
            show_bin_width=True,
            norm=True
        )

        x = []
        y = []
        errx = []
        erry = []

        print(len(bandUncer), sig_hist.GetNbinsX())
        for i in range(0, sig_hist.GetNbinsX()):
            x.append(sig_hist.GetBinCenter(i+1))
            y.append(1)
            errx.append(sig_hist.GetBinWidth(i+1)/2)
            erry.append(bandUncer[i])

        errgraph = root.TGraphErrors(len(x), array('d', x), array(
            'd', y), array('d', errx), array('d', erry))

        # *************************************************************************************************************************************************

        ax2.plot(errgraph, "2", fillcolor=1, fillstyle=3254)
        #  ddddd ax2.set_xlim(0, 90)
        # Calculate and draw the ratio
        ratio_hist = data_hist.Clone("ratio_hist")
        ratio_hist.Divide(bkg_and_sig.GetStack().Last())
        ratio_graph = aplt.root_helpers.hist_to_graph(ratio_hist)
        ax2.plot(ratio_graph, "P0")

        # Add extra space at top of plot to make room for labels
        ax1.add_margins(top=0.16)

        # Set axis titles
        # Set axis titles
        if var == "pT":
            ax2.set_xlabel("p_{T}^{l} [GeV]")
        elif var == "Eta":
            ax2.set_xlabel("\eta^{l}")

        ax1.set_ylabel("Events")
        ax2.set_ylabel("Data / Pred.", loc="centre")
        ax2.set_ylim(0.89, 1.11)
        ax2.draw_arrows_outside_range(ratio_graph)
        if(var == "pT"):
            ax2.set_xlim(25, 100)

        # Go back to top axes to add labels
        ax1.cd()

        # Add the ATLAS Label
        aplt.atlas_label(text="Internal", loc="upper left")
        ax1.text(0.2, 0.84, Indice, size=22, align=13)

        # Add legend
        legend = ax1.legend(loc=(0.58, 0.65, 1 - root.gPad.GetRightMargin() -
                                 0.03, 1 - root.gPad.GetTopMargin() - 0.03), textsize=22, ncol=2)

        legend.AddEntry(data_graph, "Data", "EP")
        legend.AddEntry(sig_hist, "Signal", "F")
        legend.AddEntry(bkg_hist1, "Top", "F")
        legend.AddEntry(bkg_hist2, "Diboson", "F")
        legend.AddEntry(bkg_hist3, "W, Bg", "F")
        legend.AddEntry(bkg_hist4, "Z, Bg", "F")
        legend.AddEntry(bkg_hist5, "Multijet", "F")
        legend.AddEntry(err_band, "Total. Unc.", "F")

        fig.savefig("Output/Backgrounds/"+var+"_" +
                    Energy+"_lepton_"+channel+".pdf")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def Plotting1GeV(self, data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, lepton, var, multi, Energy):
        # Set the ATLAS Style
        aplt.set_atlas_style()

        # Create a figure and axes
        fig, (ax1, ax2) = aplt.ratio_plot(
            name="fig1", figsize=(800, 800), hspace=0.05)

        # define signal, data and background
        data_hist = (data.Get(channel+"Selection/Lepton_" +
                              var+"_Reco_1GeV_cut7")).Clone("data_hist")
        sig_hist = (Signal.Get(channel+"Selection/Lepton_" +
                               var+"_Reco_1GeV_cut7")).Clone("sig_hist")
        bkg_hist1 = (Background_Top.Get(
            channel+"Selection/Lepton_"+var+"_Reco_1GeV_cut7")).Clone("bkg_hist1")
        bkg_hist2 = (Background_diboson.Get(
            channel+"Selection/Lepton_"+var+"_Reco_1GeV_cut7")).Clone("bkg_hist2")
        bkg_hist3 = (Background_W.Get(channel+"Selection/Lepton_" +
                                      var+"_Reco_1GeV_cut7")).Clone("bkg_hist3")
        bkg_hist4 = (Background_Z.Get(channel+"Selection/Lepton_" +
                                      var+"_Reco_1GeV_cut7")).Clone("bkg_hist4")

        bkg_MJ = (Background_MiltiJet.Get(
            "hist/"+lepton+multi)).Clone("bkg_MJ")
        bkg_hist5 = sig_hist.Clone("bkg_hist5")
        for i in range(0, bkg_hist5.GetNbinsX()):
            bkg_hist5.SetBinContent(i+1, bkg_MJ.GetBinContent(i+1))
            bkg_hist5.SetBinError(i+1,   bkg_MJ.GetBinError(i+1))

        # Stack the background and signal histogra
        bkg_and_sig = root.THStack("bkg_and_sig", "")
        bkg_and_sig.Add(bkg_hist2)
        bkg_and_sig.Add(bkg_hist1)
        bkg_and_sig.Add(bkg_hist5)
        bkg_and_sig.Add(bkg_hist4)
        bkg_and_sig.Add(bkg_hist3)
        bkg_and_sig.Add(sig_hist)

        print(bkg_hist1.GetNbinsX(), bkg_hist2.GetNbinsX(), bkg_hist3.GetNbinsX(
        ), bkg_hist4.GetNbinsX(), bkg_hist5.GetNbinsX(), sig_hist.GetNbinsX())

        for i in range(0, 30):
            print(i+1, bkg_hist4.GetBinLowEdge(i+1),
                  bkg_hist5.GetBinLowEdge(i+1), sig_hist.GetBinLowEdge(i+1), )

        bkg_hist1.SetFillColor(root.kRed+1)
        bkg_hist2.SetFillColor(root.kGreen+1)
        bkg_hist3.SetFillColor(root.kMagenta+2)
        bkg_hist4.SetFillColor(root.kOrange+7)
        bkg_hist5.SetFillColor(root.kGray+1)
        sig_hist.SetFillColor(root.kAzure+1)

        # Draw the stacked histogram on these axes
        ax1.plot(bkg_and_sig)
        #bkg_and_sig.GetXaxis().SetLimits(0, 70)

        # Plot the MC stat error as a hatched band
        err_band = aplt.root_helpers.hist_to_graph(
            bkg_and_sig.GetStack().Last(),
            show_bin_width=True
        )

        ax1.set_yscale("log")
        ax1.plot(err_band, "2", fillcolor=1, fillstyle=3254, linewidth=0)

        # Plot the data as a graph
        ax1.set_ylim(0, 100)
        data_graph = aplt.root_helpers.hist_to_graph(data_hist)
        ax1.plot(data_graph, "P")
        if(var == "pT"):
            ax1.set_xlim(0, 100)
        # Use same x-range in lower axes as upper axes
        ax2.set_xlim(ax1.get_xlim())

        # Draw line at y=1 in ratio panel
        line = root.TLine(ax1.get_xlim()[0], 1, ax1.get_xlim()[1], 1)
        ax2.plot(line)

        # Plot the relative error on the ratio axes
        err_band_ratio = aplt.root_helpers.hist_to_graph(
            bkg_and_sig.GetStack().Last(),
            show_bin_width=True,
            norm=True
        )

        ax2.plot(err_band_ratio, "2", fillcolor=1, fillstyle=3254)
        #  ddddd ax2.set_xlim(0, 90)
        # Calculate and draw the ratio
        ratio_hist = data_hist.Clone("ratio_hist")
        ratio_hist.Divide(bkg_and_sig.GetStack().Last())
        ratio_graph = aplt.root_helpers.hist_to_graph(ratio_hist)
        ax2.plot(ratio_graph, "P0")

        # Add extra space at top of plot to make room for labels
        ax1.add_margins(top=0.16)

        # Set axis titles
        # Set axis titles
        if var == "pT":
            ax2.set_xlabel("$p_{T}^{\ell}$ [GeV]")
        elif var == "Eta":
            ax2.set_xlabel("$\eta_{\ell}$")

        ax1.set_ylabel("Events")
        ax2.set_ylabel("Data / Pred.", loc="centre")
        ax2.set_ylim(0.89, 1.11)
        ax2.draw_arrows_outside_range(ratio_graph)
        if(var == "pT"):
            ax2.set_xlim(0, 100)

        # Go back to top axes to add labels
        ax1.cd()

        # Add the ATLAS Label
        aplt.atlas_label(text="Internal", loc="upper left")
        ax1.text(0.2, 0.84, Indice, size=22, align=13)

        # Add legend
        legend = ax1.legend(
            loc=(0.68, 0.55, 1 - root.gPad.GetRightMargin() -
                 0.03, 1 - root.gPad.GetTopMargin() - 0.03),
            textsize=22
        )

        legend.AddEntry(data_graph, "Data", "EP")
        legend.AddEntry(sig_hist, "Signal", "F")
        legend.AddEntry(bkg_hist1, "Top", "F")
        legend.AddEntry(bkg_hist2, "Diboson", "F")
        legend.AddEntry(bkg_hist3, "W, Bg", "F")
        legend.AddEntry(bkg_hist4, "Z, Bg", "F")
        legend.AddEntry(bkg_hist5, "Multijet", "F")
        legend.AddEntry(err_band, "MC Stat. Unc.", "F")

        fig.savefig("Output/Backgrounds/"+var+"_" +
                    Energy+"_lepton_1GeV_"+channel+".pdf")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ReadHistogramMJ(self, MJFile, Indice, channel, lepton, var, multi, Energy):

        if "enu" in channel:
            ETA_MJHistogram = histtoarray(MJFile.Get("hist/elEta"))
            ElPt_MJHistogram = histtoarray(MJFile.Get("hist/elPt"))
        if "munu" in channel:
            ETA_MJHistogram = histtoarray(MJFile.Get("hist/muEta"))
            ElPt_MJHistogram = histtoarray(MJFile.Get("hist/muPt"))

        sum1 = ElPt_MJHistogram[25] + ElPt_MJHistogram[26] + \
            ElPt_MJHistogram[27] + ElPt_MJHistogram[28] + ElPt_MJHistogram[29]
        sum2 = ElPt_MJHistogram[30] + ElPt_MJHistogram[31] + \
            ElPt_MJHistogram[32] + ElPt_MJHistogram[33] + ElPt_MJHistogram[34]
        sum3 = ElPt_MJHistogram[35] + ElPt_MJHistogram[36] + \
            ElPt_MJHistogram[37] + ElPt_MJHistogram[38] + ElPt_MJHistogram[39]
        sum4 = ElPt_MJHistogram[40] + ElPt_MJHistogram[41] + \
            ElPt_MJHistogram[42] + ElPt_MJHistogram[43] + ElPt_MJHistogram[44]
        sum5 = ElPt_MJHistogram[45] + ElPt_MJHistogram[46] + \
            ElPt_MJHistogram[47] + ElPt_MJHistogram[48] + ElPt_MJHistogram[49]
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

        ETA1_MJHistogram = ETA1_MJHistogram[int(len(ETA1_MJHistogram)/2)::]
        ETA2_MJHistogram = ETA2_MJHistogram[int(len(ETA2_MJHistogram)/2)::]
        ETA3_MJHistogram = ETA3_MJHistogram[int(len(ETA3_MJHistogram)/2)::]
        ETA4_MJHistogram = ETA4_MJHistogram[int(len(ETA4_MJHistogram)/2)::]
        ETA5_MJHistogram = ETA5_MJHistogram[int(len(ETA5_MJHistogram)/2)::]
        ETA6_MJHistogram = ETA6_MJHistogram[int(len(ETA6_MJHistogram)/2)::]

        listFinal = np.concatenate((ETA1_MJHistogram, ETA2_MJHistogram,
                                    ETA3_MJHistogram, ETA4_MJHistogram, ETA5_MJHistogram, ETA6_MJHistogram))
        return listFinal

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def Plotting2dim(self, data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, lepton, var, multi, Energy, bandUncer):

        # Set the ATLAS Style
        aplt.set_atlas_style()

        # Create a figure and axes
        fig, (ax1, ax2) = aplt.ratio_plot(
            name="fig1", figsize=(1800, 800), hspace=0.05)

        Nsignal, Ndata, NBkg_top, NBkg_diboson, NBkg_w, NBkg_z = (
            [] for i in range(6))

        for i in range(1, 7):
            Nsignal.append(Signal.Get(
                channel+'Selection/Lepton_Eta_Reco_pt'+str(i)+'_cut7'))
            Ndata.append(
                data.Get(channel+'Selection/Lepton_Eta_Reco_pt'+str(i)+'_cut7'))
            NBkg_top.append(Background_Top.Get(
                channel+'Selection/Lepton_Eta_Reco_pt'+str(i)+'_cut7'))
            NBkg_diboson.append(Background_diboson.Get(
                channel+'Selection/Lepton_Eta_Reco_pt'+str(i)+'_cut7'))
            NBkg_w.append(Background_W.Get(
                channel+'Selection/Lepton_Eta_Reco_pt'+str(i)+'_cut7'))
            NBkg_z.append(Background_Z.Get(
                channel+'Selection/Lepton_Eta_Reco_pt'+str(i)+'_cut7'))

        if "enu" in channel:
            xlabel = ["0", " ", " ", " ", " ", " ", " ", " ", " ", "2.47", "", " ", " ", " ", " ", " ", " ", " ", " ", "2.47", "", " ", " ", " ", " ", " ", " ", " ", " ",
                      "2.47", "", " ", " ", " ", " ", " ", " ", " ", " ", "2.47", "", " ", " ", " ", " ", " ", " ", " ", " ", "2.47", "", " ", " ", " ", " ", " ", " ", " ", " ", "2.47"]
            RecoBin = [0., 0.1, 0.6, 0.8, 1.15, 1.37, 1.52, 1.81, 2.01, 2.37, 2.47, 2.57, 3.07, 3.27, 3.62, 3.84, 3.99, 4.28, 4.48, 4.84, 4.94, 5.04, 5.54, 5.74, 6.09, 6.31, 6.46, 6.75, 6.95, 7.31, 7.41, 7.51,
                       8.01, 8.21, 8.56, 8.78, 8.93, 9.22, 9.42, 9.78, 9.88, 9.98, 10.48, 10.68, 11.03, 11.25, 11.4,  11.69, 11.89, 12.25, 12.35, 12.45, 12.95, 13.15, 13.5,  13.72, 13.87, 14.16, 14.36, 14.72, 14.82]
            # Binning   = [0., 0.1, 0.46, 0.66, 0.95, 1.1, 1.32, 1.67, 1.87, 2.37, 2.47, 2.57, 3.07, 3.27, 3.62, 3.84, 3.99, 4.28, 4.48, 4.84, 4.94, 5.04, 5.4, 5.6, 5.89, 6.04, 6.26, 6.61, 6.81, 7.31, 7.41, 7.51,
            #             8.01, 8.21, 8.56, 8.78, 8.93, 9.22, 9.42, 9.78, 9.88, 9.98, 10.34, 10.54, 10.83, 10.98, 11.2, 11.55, 11.75, 12.25, 12.35, 12.45, 12.95, 13.15, 13.5, 13.72, 13.87, 14.16, 14.36, 14.72, 14.82]

        if "munu" in channel:
            xlabel = ["0", " ", " ", " ", " ", " ", "2.4", " ", " ", " ", " ", " ", " ", "2.4", " ", " ", " ", " ", " ", " ",
                      "2.4", " ", " ", " ", " ", " ", " ", "2.4", " ", " ", " ", " ", " ", " ", "2.4", " ", " ", " ", " ", " ", " ", "2.4"]
            RecoBin = [0., 0.482, 1.052, 1.2521, 1.35, 1.492, 1.924, 2.4, 2.876, 3.308, 3.45, 3.5479, 3.748, 4.318, 4.8, 5.282, 5.852, 6.0521, 6.15, 6.292, 6.724, 7.2,
                       7.676, 8.108, 8.25, 8.3479, 8.548, 9.118, 9.6, 10.082, 10.652, 10.8521, 10.95, 11.092, 11.524, 12., 12.476, 12.908, 13.05, 13.1479, 13.348, 13.918, 14.4]
            # Binning   = [0., 0.482, 1.052, 1.2521, 1.35, 1.492, 1.924, 2.4, 2.876, 3.308, 3.45, 3.5479, 3.748, 4.318, 4.8, 5.282, 5.852, 6.0521, 6.15, 6.292, 6.724, 7.2,
            #             7.676, 8.108, 8.25, 8.3479, 8.548, 9.118, 9.6, 10.082, 10.652, 10.8521, 10.95, 11.092, 11.524, 12., 12.476, 12.908, 13.05, 13.1479, 13.348, 13.918, 14.4]

        if "munu" in channel:
            line1 = TLine(2.4,  0,    2.4,   60000)
            line2 = TLine(4.8,  0,    4.8,   60000)
            line3 = TLine(7.2,  0,    7.2,   60000)
            line4 = TLine(9.6,  0,    9.6,   60000)
            line5 = TLine(12,   0,    12,    60000)
            line6 = TLine(14.4, 0,    14.4,  60000)

        if "enu" in channel:
            line1 = TLine(2.47,  0,   2.47, 60000)
            line2 = TLine(4.94,  0,   4.94, 60000)
            line3 = TLine(7.41,  0,   7.41, 60000)
            line4 = TLine(9.88,  0,   9.88, 60000)
            line5 = TLine(12.35, 0,  12.35, 60000)
            line6 = TLine(14.82, 0,  14.82, 60000)

        # Make a Clone of hists
        data_hist = TH1F("data_hist", "data_hist", len(
            RecoBin)-1, array('d', RecoBin))  # data
        sig_hist = TH1F("sig_hist",  "sig_hist",  len(
            RecoBin)-1, array('d', RecoBin))  # Signal
        bkg_hist1 = TH1F("bkg_hist1", "bkg_hist1", len(
            RecoBin)-1, array('d', RecoBin))  # Top
        bkg_hist2 = TH1F("bkg_hist2", "bkg_hist2", len(
            RecoBin)-1, array('d', RecoBin))  # diboson
        bkg_hist3 = TH1F("bkg_hist3", "bkg_hist3", len(
            RecoBin)-1, array('d', RecoBin))  # diboson
        bkg_hist4 = TH1F("bkg_hist4", "bkg_hist4", len(
            RecoBin)-1, array('d', RecoBin))  # diboson
        bkg_hist5 = TH1F("bkg_hist5", "bkg_hist5", len(
            RecoBin)-1, array('d', RecoBin))  # diboson
        histbg = TH1F("histbg", "histbg", len(RecoBin) -
                      1, array('d', RecoBin))  # diboson

        for i in range(0, len(Background_MiltiJet)):
            bkg_hist5.SetBinContent(i+1, Background_MiltiJet[i])

        k = 0
        for i in range(0, len(Ndata)):
            for j in range(0, Ndata[i].GetNbinsX()):
                data_hist.SetBinContent(k+1, Ndata[i].GetBinContent(j+1))
                data_hist.SetBinError(k+1, Ndata[i].GetBinError(j+1))

                sig_hist.SetBinContent(k+1,  Nsignal[i].GetBinContent(j+1))
                sig_hist.SetBinError(k+1,  Nsignal[i].GetBinError(j+1))

                bkg_hist1.SetBinContent(k+1,  NBkg_top[i].GetBinContent(j+1))
                bkg_hist1.SetBinError(k+1,  NBkg_top[i].GetBinError(j+1))

                bkg_hist2.SetBinContent(
                    k+1,  NBkg_diboson[i].GetBinContent(j+1))
                bkg_hist2.SetBinError(k+1,  NBkg_diboson[i].GetBinError(j+1))

                bkg_hist3.SetBinContent(k+1,  NBkg_w[i].GetBinContent(j+1))
                bkg_hist3.SetBinError(k+1,  NBkg_w[i].GetBinError(j+1))

                bkg_hist4.SetBinContent(k+1,  NBkg_z[i].GetBinContent(j+1))
                bkg_hist4.SetBinError(k+1,  NBkg_z[i].GetBinError(j+1))

                k = k+1


        fig.savefig("Output/Backgrounds/Lepton_vs_Eta_""_" +
                    Energy+"_"+channel+".pdf")


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def PlottingMigration2dim(self, data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, lepton, var, multi, Energy):

        # Set the ATLAS Style
        aplt.set_atlas_style()

        # Create a figure and axes
        fig, (ax1, ax2) = aplt.ratio_plot(
            name="fig1", figsize=(1600, 800), hspace=0.05)

        Nmigration = []

        for i in range(1, 7):
            for j in range(1, 7):
                Nmigration.append(Signal.Get(
                    channel+'Selection/Lepton_Eta_Reco_v_Truth_pt'+str(i)+'pt'+str(j)+'_cut7'))
                print('Lepton_Eta_Reco_v_Truth_pt'+str(i)+'pt'+str(j)+'_cut7')
        if "enu" in channel:
            RecoBin = [0., 0.1, 0.6, 0.8, 1.15, 1.37, 1.52, 1.81, 2.01, 2.37, 2.47, 2.57, 3.07, 3.27, 3.62, 3.84, 3.99, 4.28, 4.48, 4.84, 4.94, 5.04, 5.54, 5.74, 6.09, 6.31, 6.46, 6.75, 6.95, 7.31, 7.41, 7.51,
                       8.01, 8.21, 8.56, 8.78, 8.93, 9.22, 9.42, 9.78, 9.88, 9.98, 10.48, 10.68, 11.03, 11.25, 11.4,  11.69, 11.89, 12.25, 12.35, 12.45, 12.95, 13.15, 13.5,  13.72, 13.87, 14.16, 14.36, 14.72, 14.82]
            binningr = [0., 0.1, 0.6, 0.8, 1.15, 1.37, 1.52, 1.81, 2.01, 2.37, 2.47, 2.57, 3.07, 3.27, 3.62, 3.84, 3.99, 4.28, 4.48, 4.84, 4.94, 5.04, 5.54, 5.74, 6.09, 6.31, 6.46, 6.75, 6.95, 7.31, 7.41, 7.51,
                        8.01, 8.21, 8.56, 8.78, 8.93, 9.22, 9.42, 9.78, 9.88, 9.98, 10.48, 10.68, 11.03, 11.25, 11.4,  11.69, 11.89, 12.25, 12.35, 12.45, 12.95, 13.15, 13.5,  13.72, 13.87, 14.16, 14.36, 14.72, 14.82]
            binningt = np.array([0., 0.65, 1.14, 1.45, 1.65, 2., 2.5, 3., 3.35, 3.55, 3.86, 4.35, 5., 5.65,  6.14, 6.45, 6.65, 7.,
                                 7.5, 8., 8.35, 8.55, 8.86, 9.35, 10., 10.65, 11.14, 11.45, 11.65, 12., 12.5, 13., 13.35, 13.55, 13.86, 14.35, 15.])
        if "munu" in channel:
            RecoBin = [0., 0.482, 1.052, 1.2521, 1.35, 1.492, 1.924, 2.4, 2.876, 3.308, 3.45, 3.5479, 3.748, 4.318, 4.8, 5.282, 5.852, 6.0521, 6.15, 6.292, 6.724, 7.2,
                       7.676, 8.108, 8.25, 8.3479, 8.548, 9.118, 9.6, 10.082, 10.652, 10.8521, 10.95, 11.092, 11.524, 12., 12.476, 12.908, 13.05, 13.1479, 13.348, 13.918, 14.4]
            binningr = [0., 0.482, 1.052, 1.2521, 1.35, 1.492, 1.924, 2.4, 2.876, 3.308, 3.45, 3.5479, 3.748, 4.318, 4.8, 5.282, 5.852, 6.0521, 6.15, 6.292, 6.724, 7.2,
                        7.676, 8.108, 8.25, 8.3479, 8.548, 9.118, 9.6, 10.082, 10.652, 10.8521, 10.95, 11.092, 11.524, 12., 12.476, 12.908, 13.05, 13.1479, 13.348, 13.918, 14.4]
            binningt = np.array([0., 0.65, 1.14, 1.45, 1.65, 2., 2.5, 3., 3.35, 3.55, 3.86, 4.35, 5., 5.65,  6.14, 6.45, 6.65, 7.,
                                 7.5, 8., 8.35, 8.55, 8.86, 9.35, 10., 10.65, 11.14, 11.45, 11.65, 12., 12.5, 13., 13.35, 13.55, 13.86, 14.35, 15.])

        nRbins = len(binningr)-1
        nTbins = len(binningt)-1

        print(array('d', binningr))
        print(array('d', binningt))
        Migration_Matr = ROOT.TH2D(
            "Migration_Matr", "Migration_Matr", nRbins, array('d', binningr), nTbins, array('d', binningt))

        for i in range(0, len(Nmigration)):
            print(Nmigration[i].GetName())
        # --------------------------------------------------------------------------------------------------------------------------------

        indice = 0
        for l in range(0, 6):
            for k in range(0, 6):
                for i in range(0, Nmigration[0].GetNbinsX()):
                    for j in range(0, Nmigration[0].GetNbinsY()):
                        Migration_Matr.SetBinContent(i+1+l*Nmigration[0].GetNbinsX(
                        ), j+1+k*Nmigration[0].GetNbinsY(), Nmigration[indice].GetBinContent(i+1, j+1))
                print(indice)
                indice = indice + 1
        # --------------------------------------------------------------------------------------------------------------------------------

        if "munu" in channel:
            line1 = TLine(2.4,  0,    2.4,   15)
            line2 = TLine(4.8,  0,    4.8,   15)
            line3 = TLine(7.2,  0,    7.2,   15)
            line4 = TLine(9.6,  0,    9.6,   15)
            line5 = TLine(12,   0,    12,    15)
            line6 = TLine(14.4, 0,    14.4,  15)

            line1p = TLine(0,  2.5,    	14.4,   2.5)
            line2p = TLine(0,  5,    	14.4,   5)
            line3p = TLine(0,  7.5,    	14.4,   7.5)
            line4p = TLine(0,  10,    	14.4,   10)
            line5p = TLine(0,  12.5,    14.4,   12.5)
            line6p = TLine(0,  15,   	14.4,   15)

        if "enu" in channel:
            line1 = TLine(2.47,  0,   2.47, 15)
            line2 = TLine(4.94,  0,   4.94, 15)
            line3 = TLine(7.41,  0,   7.41, 15)
            line4 = TLine(9.88,  0,   9.88, 15)
            line5 = TLine(12.35, 0,  12.35, 15)
            line6 = TLine(14.82, 0,  14.82, 15)

            line1p = TLine(0,  2.5,  	14.82,   2.5)
            line2p = TLine(0,  5,  	14.82,   5.0)
            line3p = TLine(0,  7.5,  	14.82,   7.5)
            line4p = TLine(0,  10,  	14.82,   10.)
            line5p = TLine(0,  12.5, 	14.82,  12.5)
            line6p = TLine(0,  15, 	14.82,  15.0)

        # --------------------------------------------------------------------------------------------------------------------------------

        #print(Migration_Matr.GetNbinsX(), Migration_Matr.GetNbinsY())

        fig, ax = aplt.subplots(1, 1, name="fig1", figsize=(800, 600))

        ax.set_xlim(0, 15)
        ax.set_ylim(0, 15)
        Migration_Matr.GetZaxis().SetRange(1, 7900)
        ax.plot2d(Migration_Matr, "COLZ")

        line1.Draw("same")
        line2.Draw("same")
        line3.Draw("same")
        line4.Draw("same")
        line5.Draw("same")
        line6.Draw("same")
        line1p.Draw("same")
        line2p.Draw("same")
        line3p.Draw("same")
        line4p.Draw("same")
        line5p.Draw("same")
        line6p.Draw("same")

        # Change pad margins to allow space for z-axis colour bar and for ATLAS label
        ax.set_pad_margins(right=0.20, top=0.08)

        # Set axis titles
        ax.set_xlabel("$\eta^{\ell}$, Detector-level")
        ax.set_ylabel("$\eta^{\ell}$, Particle-level")
        ax.set_zlabel("", titleoffset=1.2)

        # Add the ATLAS Label
        aplt.atlas_label(ax.pad.GetLeftMargin(), 0.97,
                         text="Internal", align=13)
        ax.text(1 - ax.pad.GetRightMargin(), 0.97, Indice, size=22, align=33)

        # Save the plot as a PDF
        fig.savefig("Output/Backgrounds/Migration_2D " +
                    "_"+Energy+"_lepton_"+channel+".pdf")
