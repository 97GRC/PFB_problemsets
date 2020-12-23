#!/usr/bin/python3
import sys

infile=sys.argv[1]
fastaDict={}
seqName=''
newData=''
with open(infile,"r") as file_object:
    for line in file_object:
        line = line.rstrip()
        if(line.startswith(">")):
            seqName=line.split(' ')[0]
            seqName=seqName.replace('>','')
            newData=''
#            print(seqName)
        else:
#            print(line)
            newData += line
            fastaDict[seqName] = newData

print(fastaDict)
