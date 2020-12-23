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
        codons[seqId]={}
    for frame in [0, 1, 2]:
        codonList=[]
        for pos in list(range(frame,len(fastaDict[seqId]),3)):
            codon=fastaDict[seqId][pos:pos+3]
#            codons[seqId][frame].append(codon)
            codonList.append(codon)
        codonString=' '.join(codonList)
        codons[seqId][frame]=codonList
#        print(f'{seqId}-frame-{frame+1}-codons\n{codonString}')
#            print(f'{seqId} {frame} {pos} {codon}')

for s in codons.keys():
    for f in codons[s].keys():
        c=' '.join(codons[s][f])
        print(f'{s}-frame-{f+1}-codons\n{c}')
