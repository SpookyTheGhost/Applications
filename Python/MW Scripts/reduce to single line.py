OFile = input("What File? ")
OpenFile = open(OFile)
print("Please be patient while the file is being processed")

fileList = []

for line in OpenFile:
    fileList.append(line)
    
OpenFile.close()

#Writing links to output file#
WFile = input("what is the return file: ")
WriteFile = open(WFile, "w")

temp = ""
for i in fileList:
    temp += i.strip()
WriteFile.write(temp) 
WriteFile.close()

print("Thanks for waiting, file has been processed :)")
