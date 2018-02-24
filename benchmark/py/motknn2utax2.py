#!/usr/bin/python

import sys
import utax2
import fasta
import die

Levels = [ 'd', 'p', 'c', 'o', 'f', 'g' ]

def FixQueryLabel(Label):
	Acc = fasta.GetAccFromLabel(Label)
	Tax = fasta.GetTaxFromLabel(Label)
	s = Acc + ";tax="
	Fields = Tax.split(',')
	n = len(Fields)
	for i in range(0, n):
		Field = Fields[i]
		if i > 0:
			s += ","
		s += Field[0] + ":" + Field[2:]
	s += ";"
	return s

File = open(sys.argv[1])
while 1:
	Line = File.readline()
	if len(Line) == 0:
		break

# Tabbed, 2 fields, x: inserted by mothur_make_taxtrainfiles.py
# QueryLabel d:Bacteria;p:Proteobacteria;c:Epsilonproteobacteria;o:Campylobacterales;f:Helicobacteraceae;g:Helicobacter;unclassified;
	Fields = Line.strip().split('\t')
	assert len(Fields) == 2

	QueryLabel = Fields[0]
	MotPred = Fields[1]
	if not MotPred.endswith(";"):
		die.Die("doesn't end with ; '" + MotPred + "'")

	QueryLabel = FixQueryLabel(QueryLabel)

	PredStr = ""
	Fields2 = MotPred.split(';')
	for Field in Fields2:
		if Field == "" or Field.find("unclassified") >= 0 or Field.find("unknown") >= 0:
			continue
		if PredStr != "":
			PredStr += ","
		PredStr += Field
		
	print QueryLabel + '\t' + PredStr
