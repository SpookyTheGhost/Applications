print("""Options
---------------------------------------
File Upload: upload
All Files: files
Restored Page: RP
Deleted Page:DP
Quit:Q
---------------------------------------
""")
Option = input("Choose an option?: ")
OFile = input("What File? ")
OpenFile = open(OFile)

WFile = input("what is the return file: ")
WriteFile = open(WFile, "w")

WriteList = []
if Option.lower() == "upload":
    print("Please be patient while the file is being processed")
    for line in OpenFile:
        strip = line.strip()
        Start = strip.find("File:")
        End = strip.find(": File uploaded.")
        Processed = strip[Start:End]
        WriteList.append(Processed)

elif Option.lower() == "files": 
    FileType = input("Is the file jpeg, png, jpg, JPG?: ")
    default = 4
    print("Please be patient while the file is being processed")
    for line in OpenFile:
        Strip = line.strip()
        if FileType.lower() == "jpeg":
            Start = Strip.find("File:")
            End = Strip.find(".jpeg")
            Processed = Strip[Start:End+5]
            WriteList.append(Processed.replace(" ","_"))
        elif FileType == "jpg":
            Start = Strip.find("File:")
            End = Strip.find(".jpg")
            Processed = Strip[Start:End+4]
            WriteList.append(Processed.replace(" ","_"))
        elif FileType == "JPG":
            Start = Strip.find("File:")
            End = Strip.find(".JPG")
            Processed = Strip[Start:End+4]
            WriteList.append(Processed.replace(" ","_"))
        elif FileType.lower() == "png":
            Start = Strip.find("File:")
            End = Strip.find(".png")
            Processed = Strip[Start:End+4]
            WriteList.append(Processed.replace(" ","_"))
        else:
            continue

elif Option.lower() == "RP": # filter for restoring pages from log
    for line in OpenFile:
        Strip = line.strip()
        Start = Strip.find("page") + 5
        End = Strip.find("revisions") - 3
        
        processedPage = Strip[Start:End]

        if processedPage.find(" (") != -1:
            o = processedPage.find(" (")
            WriteList.append(Processed[:o])
        else:
            WriteList.append(Processed)

elif Option.lower() == "DP": # filter for deleting pages from log
    for line in OpenFile:
        strip = line.strip()
        Start = strip.find("page") + 5 # find page name
        Temp = strip[Start:] # temporary
        TrailingSpace = strip[Start:].find(" ") # find trailing space after page name
        PageName = Temp[:TrailingSpace]
        processedPage = strip[Start:End]
        WriteList.append(Processed.strip())

elif Option.lower() == "q": #quiting
    print("Have a nice day :)")
    quit()

OpenFile.close()

WriteList.sort()
for i in WriteList:
    WriteFile.write(i)
    WriteFile.write("\n")

WriteFile.close()

print("Thanks for waiting, file has been processed :)")
