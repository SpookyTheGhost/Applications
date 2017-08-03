OFile = input("What File? ")

print("""Options
---------------------------------------
File Upload: upload
User Contributions: user
Restored Page: RP
Deleted Page:DP
Restored or Deleted File: RDF
Quit:Q
""")
Option = input("file upload or user contribution?: ")
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

elif Option.lower() == "user": # check if delete/restored page technique is faster
    FileType = input("Is the file jpeg, png, jpg?: ")
    default = 4
    print("Please be patient while the file is being processed")
    for line in OpenFile:
        Strip = line.strip()
        if FileType.lower() == "jpeg":
            Start = Strip.find("File:")
            End = Strip.find(".jpeg")
            Processed = Strip[Start:End+5]
            WriteList.append(Processed)
        elif FileType.lower() == "jpg":
            Start = Strip.find("File:")
            End = Strip.find(".jpg")
            Processed = Strip[Start:End+4]
            WriteList.append(Processed)
        elif FileType.lower() == "png":
            Start = Strip.find("File:")
            End = Strip.find(".png")
            Processed = Strip[Start:End+4]
            WriteList.append(Processed)
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

##x = "00:53, January 7, 2016 Nerfmaster8 (wall | contribs | block) deleted page Ahuihigodg456 (content was: {{delete|spam}}sdfg (and the only contributor was Nerfmaster8))"
##strip = x.strip()
##Start = strip.find("page") + 5 # find page name
##Temp = strip[Start:] # temporary
##TrailingSpace = strip[Start:].find(" ") # find trailing space after page name
##PageName = Temp[:TrailingSpace]
##print(PageName.strip())

elif Option.lower() == "RDF": # filter for delete/restoring files from log
    for line in OpenFile:
        Strip = line.strip()
        FileExtension = input("What is the file extension? ")
        Start = Strip.find("File:")
        default = 4
        if FileExtension == ".jpg" or FileExtension == ".png":
            pass
        elif FileExtension == ".jpeg":
            default = 5
        End = Strip.find(FileExtension) + default
##        processedPage = Strip[Start:End]
##        WriteList.append(Processed)
        WriteList.append(Strip[Start:End])

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
