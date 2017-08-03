OFile = input("What File? ")
OpenFile = open(OFile, "r", -1, "utf-8")
print("Please be patient while the file is being processed")

fileList = []

for line in OpenFile:
    line = str(line)
    line = line.replace(" ","_")
    split = line.split()
    for file in split:
        fileList.append(file.strip())
    
OpenFile.close()

links = []
for i in fileList:
    if i.find(".jpg") != -1 or i.find(".png") != -1 or i.find(".PNG"):
        links.append(i)

#Writing links to output file#
WFile = input("what is the return file: ")
WriteFile = open(WFile, "w", -1, "utf-8")

for i in links:
    WriteFile.write(i)
    WriteFile.write("\n")
    
WriteFile.close()

print("Thanks for waiting, file has been processed :)")
