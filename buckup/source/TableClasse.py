#!/usr/bin/env python
# -*-coding:Latin-1 -*

import ROOT
import ROOT as root
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine,TChain

from array import array

class TableClasse:
	def TablepTlepton(self, data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy):

		if(channel == "Wplusmunu" or channel == "Wminusmunu"):
			lepton = "mu"
		else:
			lepton = "el"
	
		Ndata, Nsignal, NBkW, NBkZ, NDiboson, NTop, NMultijet = ([] for _ in range(7))
		keys = ["No Cut","Lepton charge","One lepton", "trigger", "Isolation", "$p_{T}^{l}$ $>$ 25 GeV", "$E_{T}^{miss}$ $>$ 25 GeV", "$m_{T}$ $>$ 50 GeV"]

		for i in range(0, len(keys)): Ndata.append((data.Get(channel+'SelectionCutFlow')).GetBinContent(i+1))
		for i in range(0, len(keys)): Nsignal.append((Signal.Get(channel+'SelectionCutFlow')).GetBinContent(i+1))
		for i in range(0, len(keys)): NBkW.append((Background_W.Get(channel+'SelectionCutFlow')).GetBinContent(i+1))
		for i in range(0, len(keys)): NBkZ.append((Background_Z.Get(channel+'SelectionCutFlow')).GetBinContent(i+1))
		for i in range(0, len(keys)): NDiboson.append((Background_diboson.Get(channel+'SelectionCutFlow')).GetBinContent(i+1))
		for i in range(0, len(keys)): NTop.append((Background_Top.Get(channel+'SelectionCutFlow')).GetBinContent(i+1)) 
		for i in range(0, len(keys)): NMultijet.append( "-")
		NMultijet[-1] = str(int((Background_MiltiJet.Get('hist/'+lepton+'Pt')).Integral()))


		latexFile = open("Output/Tables/table_"+channel+"_"+Energy+".tex","w+")
		latexFile.write("\\documentclass[10pt]{article} 								\n")
		latexFile.write("\\usepackage{amsmath}  									\n")
		latexFile.write("\\usepackage{multicol}										\n")
		latexFile.write("\\usepackage{graphicx} 									\n")
		latexFile.write("\\usepackage{hyperref} 									\n")
		latexFile.write("\\usepackage{hyperref} 									\n")
		latexFile.write("\\usepackage[latin1]{inputenc} 								\n")
		latexFile.write("\\usepackage[margin={3cm,0cm},twocolumn, layouthoffset=0pt]{geometry} 				\n")
		latexFile.write("\\begin{document} 										\n")
		latexFile.write("\\begin{center}										\n")
		latexFile.write("\\begin{table}[H] 										\n")
		latexFile.write("\\begin{adjustbox}{width=1\\textwidth}								\n")
		latexFile.write("\\begin{tabular}{cccccccc} 									\n")
		latexFile.write("\\\ \\hline \\hline  										\n")
		latexFile.write("\\multicolumn{8}{c}{%s}  									\n"%Indice)
		latexFile.write("\\\ \\hline \\hline                            						\n")
		latexFile.write("\\multicolumn{1}{|c|}{}   & \multicolumn{1}{l|}{Data} & \multicolumn{1}{l|}{Signal} & \multicolumn{1}{l|}{$W^{\pm}$ $\\rightarrow$ $l^{\pm}$ $\\nu$, BG} & \multicolumn{1}{l|}{$Z^{\pm}$ $\\rightarrow$ $l^{\pm}$ $l^{\pm}$, BG} & \multicolumn{1}{l|}{Diboson} & \multicolumn{1}{l|}{Top} & \multicolumn{1}{l|}{Multijet} \\\ \\hline \n")
		NBkW[0] == 1
		for i in range(0, len(keys)):
			latexFile.write("\\multicolumn{1}{|c|}{%s}  & \multicolumn{1}{c|}{%d} & \multicolumn{1}{c|}{%d} & \multicolumn{1}{c|}{%d} & \multicolumn{1}{c|}{%d} & \multicolumn{1}{c|}{%d} & \multicolumn{1}{c|}{%d} & \multicolumn{1}{c|}{%s}  \\\ \\hline \n" %(keys[i], int(Ndata[i]), int(Nsignal[i]), int(NBkW[i]), int(NBkZ[i]), int(NDiboson[i]), int(NTop[i]), NMultijet[i]))
		latexFile.write("\\end{tabular} 										\n")
		latexFile.write("\\end{adjustbox}										\n")
		latexFile.write("\\end{table} 											\n")
		latexFile.write("\\end{center}											\n")
		latexFile.write("\\end{document}                              							\n")
	


