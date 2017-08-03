OFile = input("What File? ")
OpenFile = open(OFile)
print("Please be patient while the file is being processed")

fileList = []

for line in OpenFile:
    line = line.replace(" ","_")
    split = line.split("	")
    for file in split:
        fileList.append(file.strip())
    
OpenFile.close()

#Writing links to output file#
WFile = input("what is the return file: ")
WriteFile = open(WFile, "w")

for i in fileList:
    WriteFile.write(i)
    WriteFile.write("\n")
    
WriteFile.close()

print("Thanks for waiting, file has been processed :)")
