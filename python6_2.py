#!/usr/bin/python3


fo=open('Python_06_uc2.txt',"w")
with open("Python_06.txt","r") as file_object:
    for line in file_object:
            line = line.rstrip()
#            print(line.upper())
            fo.write(line.upper() + "\n")
