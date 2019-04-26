#!/usr/bin/python3

from urllib.request import urlopen
import math
import subprocess

ps_dock = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                              '-ExecutionPolicy',
                              'Unrestricted',
                              './first_script.ps1',
                              ])
result = ps_dock.wait()
with urlopen('https://rgw-msu.osris.org/OsirisAdmin-keenandr/test-input') as mydata:
    sorted = []
    fourcol = []
    threecol = []
    sevcol = {}
    # get each line and the item in the 3rd, 4th, and 7th columns
    for line in mydata:
        columns = line.decode().split(':')
        sorted.append(line)
        fourcol.append(columns[3])
        threecol.append(columns[2])
        try:
            if sevcol[columns[6]]:
                sevcol[columns[6]] += 1
        except:
            sevcol[columns[6]] = 1
    # selection sort
    for i in range(len(sorted)-1):
        min_index = i
        for j in range(i+1, len(sorted)):
            # find minimum item
            if int(fourcol[j]) == int(fourcol[min_index]):
                if int(threecol[j]) < int(threecol[min_index]):
                    min_index = j
            if int(fourcol[j]) < int(fourcol[min_index]):
                min_index = j
        # Swap 
        sorted[i], sorted[min_index] = sorted[min_index], sorted[i]
        fourcol[i], fourcol[min_index] = fourcol[min_index], fourcol[i]
        threecol[i], threecol[min_index] = threecol[min_index], threecol[i]
    file = open("sorted-file.txt", "w")
    for line in sorted:
        file.write(line.decode('utf-8'))
    file.write("\n \n")
    file.write("-----Here are the shells and their # of entries-----")
    file.write("\n")
    for shell in sevcol:
        output = str(sevcol[shell]) + " " + shell
        file.write(output)
        
    file.close()
