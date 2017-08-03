OFile = input("What File? ")
OpenFile = open(OFile)
subpage = input("What is the subpage prefix? ")
print("Please be patient while the file is being processed")

pageList = []

for line in OpenFile:
    line = line.replace(" ","_")
    split = line.split()
    for page in split:
        if subpage == "": # just append everything
            pageList.append(file.strip())
        else:
            if page.find(subpage) != -1:
                pageList.append(file.strip()) # only output specific subpages
            else:
                pass
    
OpenFile.close()

WFile = input("what is the return file: ")
WriteFile = open(WFile, "w")

for i in pageList:
    WriteFile.write(i)
    WriteFile.write("\n")
    
WriteFile.close()

print("Thanks for waiting, file has been processed :)")
