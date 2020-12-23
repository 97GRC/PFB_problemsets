#!/usr/bin/python3
import sys
import re

infile=sys.argv[1]
fastaDict={}
seqName=''
newData=''
with open(infile,"r") as file_object:
    for line in file_object:
        line = line.rstrip()
        if re.search(r'^>',line):
            seqName=line.split(' ')[0]
            seqName=seqName.replace('>','')
            newData=''
        else:
            newData += line.upper()
            fastaDict[seqName] = newData

codons={}
for seqId in fastaDict.keys():
    if seqId not in codons.keys():
        codons[seqId]=[]
    for pos in list(range(0,len(fastaDict[seqId]),3)):
        codon=fastaDict[seqId][pos:pos+3]
        codons[seqId].append(codon)
    codonsString=' '.join(codons[seqId])
    print(f'{seqId}-frame-1-codons\n{codonsString}')
