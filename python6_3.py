#!/usr/bin/python3


#fo=open('Python_06_uc.txt',"w")
with open("Python_06.seq.txt","r") as file_object:
    for line in file_object:
            line = line.rstrip()
            fields = line.split("\t")
            revseq=fields[1]
            revseq=revseq[::-1]
            revseq=revseq.replace('A','W')
            revseq=revseq.replace('C','X')
            revseq=revseq.replace('G','Y')
            revseq=revseq.replace('T','Z')
            revseq=revseq.replace('W','T')
            revseq=revseq.replace('X','G')
            revseq=revseq.replace('Y','C')
            revseq=revseq.replace('Z','A')
            print(f'>{fields[0]} reverse complement sequence\n{revseq}\n')
#            print(line.upper())
#            fo.write(line.upper() + "\n")
