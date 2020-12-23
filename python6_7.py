#!/usr/bin/python3


#fo=open('Python_06_uc.txt',"w")
with open("Python_06.seq.txt","r") as file_object:
    for line in file_object:
        seqComp = {}
        line = line.rstrip().upper()
        fields = line.split("\t")
        for nt in set(fields[1]):
            seqComp[nt] = fields[1].count(nt)
        if( 'C' in seqComp.keys() and 'G' in seqComp.keys() ):
            GCcontent='{:.2f}'.format(((seqComp['G']+seqComp['C'])*100)/len(fields[1]))
#            print(seqComp)
            print(f'sequence {fields[0]} composition')
            print(f'\tA:{seqComp["A"]}\tC:{seqComp["C"]}\tG:{seqComp["G"]}\tT:{seqComp["T"]}\n\tGC%:{GCcontent}')
