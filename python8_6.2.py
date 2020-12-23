#!/usr/bin/python3
import sys
import re

infile=sys.argv[1]
fastaDict={}
seqName=''
newData=''

translation_table = {
        'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
        'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
        'AAT':'N', 'AAC':'N',
        'GAT':'D', 'GAC':'D',
        'TGT':'C', 'TGC':'C',
        'CAA':'Q', 'CAG':'Q',
        'GAA':'E', 'GAG':'E',
        'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
        'CAT':'H', 'CAC':'H',
        'ATT':'I', 'ATC':'I', 'ATA':'I',
        'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
        'AAA':'K', 'AAG':'K',
        'ATG':'M',
        'TTT':'F', 'TTC':'F',
        'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
        'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
        'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
        'TGG':'W',
        'TAT':'Y', 'TAC':'Y',
        'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
        'TAA':'*', 'TGA':'*', 'TAG':'*'
        }

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
    revseq=fastaDict[seqId]
    revseq=revseq[::-1]
    revseq=revseq.replace('A','W')
    revseq=revseq.replace('C','X')
    revseq=revseq.replace('G','Y')
    revseq=revseq.replace('T','Z')
    revseq=revseq.replace('W','T')
    revseq=revseq.replace('X','G')
    revseq=revseq.replace('Y','C')
    revseq=revseq.replace('Z','A')
    if seqId not in codons.keys():
        codons[seqId]={}
    for frame in [0, 1, 2]:
        if frame not in codons[seqId]:
            codons[seqId][frame]=[]
            codons[seqId][frame+3]=[]
        for pos in list(range(frame,len(fastaDict[seqId]),3)):
            codon=fastaDict[seqId][pos:pos+3]
            revCodon=revseq[pos:pos+3]
            if len(codon) == 3:
                codons[seqId][frame].append(codon)
            if len(revCodon) == 3:
                codons[seqId][frame+3].append(revCodon)

codonsFile = open('Python_08.codons-6frames.nt','w')
aminoaFile = open('Python_08.translated.aa','w')
for seqId in codons:
    longestPeptideLength=0
    longestPeptideSequen=''
    for frame in sorted(codons[seqId]):
        aaList=[]
        codonsString=' '.join(codons[seqId][frame])
        for codon in codons[seqId][frame]:
            aaList.append(translation_table[codon])
        aaString=''.join(aaList)
        for peptide in re.finditer(r"(M.+?\*)", aaString):
            if len(peptide.group(1)) > longestPeptideLength:
                longestPeptideLength=len(peptide.group(1))
                longestPeptideSequen=peptide.group(1)
#            print(f'{seqId} frame-{frame+1} {peptide.group(1)}')
    print(f'SeqID:{seqId} LongestPeptide:{longestPeptideSequen}')
#        print(f'{seqId}-frame-{frame+1}-codons\n{codonsString}\n{aaString}')
#        codonsFile.write(f'{seqId}-frame-{frame+1}-codons\n{codonsString}\n')
#        aminoaFile.write(f'{seqId}-frame-{frame+1}-codons\n{aaString}\n')
