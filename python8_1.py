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

composition={}
for seqId in fastaDict.keys():
    if seqId not in composition.keys():
        composition[seqId]={}
    for nt in set(fastaDict[seqId]):
        if nt not in composition[seqId].keys():
            composition[seqId][nt]=0
        composition[seqId][nt] = fastaDict[seqId].count(nt)

for seqId in composition.keys():
    print(f'{seqId}\t{composition[seqId]["A"]}\t{composition[seqId]["T"]}\t{composition[seqId]["G"]}\t{composition[seqId]["C"]}')
