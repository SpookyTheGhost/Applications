file = input("What file? ")
openFile = open(file)

print("Processing now, please wait")
removeDup = []
for line in openFile:
    strip = line.strip()
    if strip not in removeDup:
        removeDup.append(strip)
openFile.close()

returnFile = input("return file? ")
ORFile = open(returnFile,"w")
for item in removeDup:
    ORFile.write(item)
    ORFile.write("\n")
ORFile.close()
print("finished, thanks for waiting")
