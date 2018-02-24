#!/usr/bin/python2

import sys
import fasta
import utax2

InputFileName = sys.argv[1]
FastaOutFileName = sys.argv[2]
TaxOutFileName = sys.argv[3]

fFa = open(FastaOutFileName, "w")
fTax = open(TaxOutFileName, "w")

def AppendRank(Tax, TaxStr, Rank):
	Name = utax2.GetNameFromTaxStr(TaxStr, Rank)
	return Tax + Name[2:] + ";"

def OnSeq(Label, Seq):
	Acc = fasta.GetAccFromLabel(Label)
	TaxStr = utax2.GetTaxFromLabel(Label)

	k = 'k'
	if TaxStr.find("d:") >= 0:
		k = 'd'

# DQ200983.1.1404.B       Bacteria;Actinobacteria;Actinobacteria;Frankiales;Geodermatophilaceae;Blastococcus;Blastococcus jejuensis;
	Tax = ""
	Tax = AppendRank(Tax, TaxStr, k)
	Tax = AppendRank(Tax, TaxStr, 'p')
	Tax = AppendRank(Tax, TaxStr, 'c')
	Tax = AppendRank(Tax, TaxStr, 'o')
	Tax = AppendRank(Tax, TaxStr, 'f')
	Tax = AppendRank(Tax, TaxStr, 'g')
	Tax = AppendRank(Tax, TaxStr, 's')

	Acc = Acc.upper()	
	fasta.WriteSeq(fFa, Seq, Acc)

	print >> fTax, "%s\t%s" % (Acc, Tax)

fasta.ReadSeqsOnSeq(InputFileName, OnSeq)
