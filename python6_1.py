#!/usr/bin/python3

with open("Python_06.txt","r") as file_object:
    for line in file_object:
            line = line.rstrip()
            print(line.upper())
