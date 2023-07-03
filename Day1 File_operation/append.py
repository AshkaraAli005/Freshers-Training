import os
inpFolder = input("Enter the path of Folder : ")
outFile = input("Enter the output file : ")
file = open(outFile , 'a')
for i in os.listdir(inpFolder):
    if i.endswith(".txt"):
        file2 = open(inpFolder + '\\' + i,'r')
        file.write(file2.read())
        file2.close()
        