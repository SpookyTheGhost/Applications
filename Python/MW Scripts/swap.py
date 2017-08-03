file = input("What file? ")
openFile = open(file)

writeList = []
for line in openFile:
    strip = line.strip()
    findPeriod = strip.find(".") + 2
    swap = "# " + strip[findPeriod:]
    writeList.append(swap)

openFile.close()

WFile = input("what is the return file: ")
WriteFile = open(WFile, "w")

for i in writeList:
    WriteFile.write(i)
    WriteFile.write("\n")
    
WriteFile.close()

print("Thanks for waiting, file has been processed :)")
