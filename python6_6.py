#!/usr/bin/python3

import sys

allGenesFile=sys.argv[1]
stemSetProlFile=sys.argv[2]
pigmentationFile=sys.argv[3]
TFsFile=sys.argv[4]
allGenesSet=set()
stemSetProlGenesSet=set()
pigmentationGenesSet=set()
TFsGenesSet=set()

with open(allGenesFile,"r") as allGenesFile_object:
    for line in allGenesFile_object:
        line = line.rstrip()
        if(line.startswith("Gene stable ID")):
            continue
        else:
            fields=line.split("\t")
            allGenesSet.add(fields[0])

with open(stemSetProlFile,"r") as stemSetProlFile_object:
    for line in stemSetProlFile_object:
        line = line.rstrip()
        if(line.startswith("Gene stable ID")):
            continue
        else:
            fields=line.split("\t")
            stemSetProlGenesSet.add(fields[0])


with open(pigmentationFile,"r") as pigmentationFile_object:
    for line in pigmentationFile_object:
        line = line.rstrip()
        if(line.startswith("Gene stable ID")):
            continue
        else:
            fields=line.split("\t")
            pigmentationGenesSet.add(fields[0])


with open(TFsFile,"r") as TFsFile_object:
    for line in TFsFile_object:
        line = line.rstrip()
        if(line.startswith("Gene stable ID")):
            continue
        else:
            fields=line.split("\t")
            TFsGenesSet.add(fields[0])




notCellProlSet = allGenesSet - stemSetProlGenesSet
cellProlAndPigmSet = stemSetProlGenesSet & pigmentationGenesSet
cellProlAndTFsSet = stemSetProlGenesSet & TFsGenesSet
print(f'There are {len(allGenesSet)} genes in total')
print(f'There are {len(stemSetProlGenesSet)} genes that belong to the Stem cell proliferations GO term')
print(f'There are {len(pigmentationGenesSet)} genes that belong to the pigmentation GO term')
print(f'There are {len(notCellProlSet)} genes that to no belong to the Stem cell proliferations GO term')
print(f'There are {len(cellProlAndPigmSet)} genes that are both Stem cell proliferation and Pigmentation')
print(f'There are {len(cellProlAndTFsSet)} genes that are both Stem cell proliferation and TFs')
