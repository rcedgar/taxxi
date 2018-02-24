#!/usr/bin/python

import sys

FileName = sys.argv[1]

File = open(FileName)
Cutoff = 0.8
if len(sys.argv) > 2:
	Cutoff = float(sys.argv[2])

# S003805392:Ferrimicrobium_acidiphilum	1.00	NA	1.00	Ferrimicrobium	1.00	Ferrimicrobium_acidiphilum	1.00   (optional list of tied species)
#                                     0    1     2     3                 4     5                             6     7
#                                   Acc Score   Grp Boot             Genus  Boot                            Sp   Boot
while 1:
	Line = File.readline()
	if len(Line) == 0:
		break

	Fields = Line[:-1].split('\t')
	assert len(Fields) >= 8

	Acc = Fields[0]
	Score = float(Fields[1])

	Fam = Fields[2]
	FamBoot = float(Fields[3])

	Genus = Fields[4]
	GenusBoot = float(Fields[5])

	Sp = Fields[6]
	SpBoot = float(Fields[7])

	if float(Score) < 0.5:
		print(Acc + "\t*")
		continue

	if Cutoff >= 0:
		if FamBoot < Cutoff:
			print(Acc + "\t*")
			continue

		s = Acc + "\t"
		s += "f:" + Fam
		if GenusBoot >= Cutoff:
			s += ",g:" + Genus
			if SpBoot >= Cutoff:
				s += ",s:" + Sp
		print(s)
	else:
		s = Acc
		s += "f:" + Fam + "(" + FamBoot + "),"
		s += "g:" + Genus + "(" + GenusBoot + ")"
		s += ",s:" + Sp + "(" + SpBoot + ")"
		print(s)
