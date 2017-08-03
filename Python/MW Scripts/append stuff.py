OFile = input("What File? ")
OpenFile = open(OFile)
append = input("Add what to end of each line? ")
print("Please be patient while the file is being processed")

pageList = []

for line in OpenFile:
    line = line.replace(" ","_")
    split = line.split()
    for page in split:
        new = page.strip() + append
        pageList.append(new)
    
OpenFile.close()

WFile = input("what is the return file: ")
WriteFile = open(WFile, "w")

for i in pageList:
    WriteFile.write(i)
    WriteFile.write("\n")
    
WriteFile.close()

print("Thanks for waiting, file has been processed :)")
