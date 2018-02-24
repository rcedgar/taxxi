#!/usr/bin/python

import sys
import utax2
import fasta

FileName = sys.argv[1]

# >S001294039     Actinomyces_hominis     Actinomyces     NA
#           0                       1               2      3
#         Acc                      s:              g:     f: ("group")
Missing = 0
def OnSeq(Label, Seq):
	global Missing

	Acc = utax2.GetAccFromLabel(Label)	
	Family = utax2.GetNameFromLabel(Label, 'f')
	Genus = utax2.GetNameFromLabel(Label, 'g')
	Species = utax2.GetNameFromLabel(Label, 's')

	if Genus == "" or Species == "":
		Missing += 1
		return

	if Family == "":
		Family = "NA"

	Family = Family.replace("f:", "")
	Genus = Genus.replace("g:", "")
	Species = Species.replace("s:", "")

	NewLabel = Acc + "\t" + Species + "\t" + Genus + "\t" + Family

	fasta.WriteSeq(sys.stdout, Seq, NewLabel)

fasta.ReadSeqsOnSeq(FileName, OnSeq)

if Missing > 0:
	print >> sys.stderr, "%u seqs missing genus or species" % Missing
