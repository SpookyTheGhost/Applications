OFile = input("What File? ")
OpenFile = open(OFile)
prepend = input("Add what to front of each line? ")
print("Please be patient while the file is being processed")

pageList = []

for line in OpenFile:
    line = line.replace(" ","_")
    split = line.split()
    for page in split:
        new = prepend + page.strip()
        pageList.append(new)
    
OpenFile.close()

pageList.sort()

WFile = input("what is the return file: ")
WriteFile = open(WFile, "w")

for i in pageList:
    WriteFile.write(i)
    WriteFile.write("\n")
    
WriteFile.close()

print("Thanks for waiting, file has been processed :)")
