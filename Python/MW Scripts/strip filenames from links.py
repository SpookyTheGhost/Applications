OFile = input("What File? ")
OpenFile = open(OFile)
print("Please be patient while the file is being processed")

fileList = []
for line in OpenFile:
    fileName = line.find("File:")
    fileList.append(line[fileName:].strip())

OpenFile.close()

WFile = input("what is the return file: ")
WriteFile = open(WFile, "w")

writelist = []
for i in fileList:
    WriteFile.write(i)
    WriteFile.write("\n")
    
WriteFile.close()

print("Thanks for waiting, file has been processed :)")
