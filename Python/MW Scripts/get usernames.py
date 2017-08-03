OFile = input("What File? ")
OpenFile = open(OFile)
print("Please be patient while the file is being processed")

userList = []
for line in OpenFile:
    strip = line.strip()

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthFinder = ""
    for i in months:
        if strip.find(i) != -1:
            monthFinder = i

    Start = strip.find(monthFinder) + len(monthFinder) + 9
    End = 0
    if strip.find("wall") != -1:
        End = strip.find("wall") - 2
    else:
        End = strip.find("Talk") - 2
    user = strip[Start:End].strip()
    userList.append(user)

OpenFile.close()

WFile = input("what is the return file: ")
WriteFile = open(WFile, "w")

for i in userList:
    WriteFile.write(i)
    WriteFile.write("\n")
    
WriteFile.close()

print("Thanks for waiting, file has been processed :)")
