file1 = input("First file? ")
openFile1 = open(file1)

file2 = input("Second file? ")
openFile2 = open(file2)

print("Processing now, please wait")
dups = []

for file1 in openFile1:
    for file2 in openFile2:
        if ((file1 == file 2) and ((file1.find("concept_art") == -1) or (file2.find("concept_art") == -1))):
            dups.append(file1)

returnFile = input("return file? ")
OFile = open(returnFile,"w")
for item in dups:
    ORFile.write(item)
    ORFile.write("\n")
OFile.close()
print("finished, thanks for waiting")
