#!/usr/bin/python2

import sys
import die
import fasta

FileName = sys.argv[1]		# metaxa2 output
FastaFileName = sys.argv[2]	# Original fasta file with utax2 annotations
Ranks = "dpcofgs"

AccToTax = {}
DomainRank = '?'

def OnSeq(Label, Seq):
	global AccToTax
	global DomainRank
	global Ranks

	Acc = fasta.GetAccFromLabel(Label)
	Tax = fasta.GetTaxFromLabel(Label)

	Acc = Acc.upper()
	AccToTax[Acc] = Tax

	if DomainRank == '?':
		DomainRank = Tax[0]
		Ranks = DomainRank + Ranks[1:]
		assert Ranks[1] == 'p'

fasta.ReadSeqsOnSeq(FastaFileName, OnSeq)

f = open(FileName)
while 1:
	Line = f.readline()
	if len(Line) == 0:
		break

# gi_1018196556     Bacteria;Proteobacteria;Gammaproteobacteria;Oceanospirillales;Halomonadaceae;   96.58   292     91.03
	Fields = Line[:-1].split('\t')

	Label = Fields[0]
	Acc = fasta.GetAccFromLabel(Label)
	Acc = Acc.upper()

	QTax = AccToTax[Acc]

	Tax = Fields[1]
	Fields2 = Tax.split(";")
	n = len(Fields2) - 1
	assert n <= len(Ranks)
	Pred = ""
	for i in range(0, n):
		if i > 0:
			Pred += ","
		Rank = Ranks[i]
		Pred += Rank + ":" + Fields2[i]

	print(Acc + ";tax=" + QTax + ";" + "\t" + Pred)
