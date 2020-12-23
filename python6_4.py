#!/usr/bin/python3


#fo=open('Python_06_uc.txt',"w")
count_lines=0
character_count=0
with open("Python_06.fastq","r") as file_object:
    for line in file_object:
        count_lines += 1
        line = line.rstrip()
        character_count += len(line)

meanCharsPerLine=character_count/count_lines
print(f'The total number of lines is {count_lines}')
print(f'The total number of characters is {character_count}')
print(f'The average number of characters per line is {meanCharsPerLine}')
