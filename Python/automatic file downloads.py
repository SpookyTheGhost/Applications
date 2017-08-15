"""
Allows for downloading files from Wikipedia, wikis running recent MediaWiki software release or Wikia.
Feed the application a text file and it will automatically do the rest
Videos will be skipped. Pictures, PDFs, audio files will download.
Unicode in filenames will cause download failure, application will print out files that failed for manual downloads.
"""

import urllib
import urllib.request
import urllib.error
import shutil
import time
import winsound

print("Welcome")
fileList = open(input("filename? "), "r", -1, "utf-8") # better file opening should be implemented

files = []
for i in fileList:
    line = str(i)
    line = i.replace(" ","_")
    split = i.split("\t")

    for k in split:
        files.append(k.strip())
fileList.close()

# full url path
url = "http://yugioh.wikia.com/wiki/Special:FilePath/"

urls = []
fileNames = []

for file in files:
    if ((file != "") and (file.find(".jpg") != -1 or file.find(".JPG") != -1 or file.find(".jpeg") != -1 or file.find(".png") != -1 or file.find(".PNG")  != -1 or file.find(".gif") != -1 or file.find(".pdf") != -1 or file.find(".ogg")) ):
        removeNS = file.find("File:")
        url += file[removeNS+5:].replace(" ","_")
        urls.append(url)
        fileNames.append( file[removeNS+5:].replace(" ","_") ) # get all filenames
    # reset url builder
        url = "http://yugioh.wikia.com/wiki/Special:FilePath/"
        
count = 0 # accurately get which file is being downloaded
URLE = []
HTTPE = []
ConnectionE = []
notFound = []
UnicodeEncode = []
print("DOWNLOADING IMAGES")
#Download the file
for u, f in zip(urls, fileNames): # takes in 2 lists to operate on
    try:
        #u is to generate an url request, f is the filename to save it under as
        with urllib.request.urlopen(u) as response, open(f, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        
    # all error handling
    except urllib.error.URLError as e:
        URLE.append(f)
        pass
    except urllib.error.HTTPError as e:
        HTTPE.append(f)
        pass
    except FileNotFoundError:
        notFound.append(f)
        pass
    except ConnectionAbortedError:
        ConnectionE.append(f)
        pass
    except UnicodeEncodeError:
        UnicodeEncode.append(f)
        pass
    count+= 1

    if (count % 1000 == 0):
        winsound.Beep(500,1000)
    
    print("finished downloading file", f, "-", count)


    
print("Done downloading!")

time.sleep(2)

winsound.Beep(500,3000)



print("-------------------------------------------------------------------------")
print()

print("URL ERRORS")
for e1 in URLE:
    print("File:" + e1)
print("-------------------------------------------------------------------------")

print("HTTP ERRORS")
for e2 in HTTPE:
    print("File:" + e2)
print("-------------------------------------------------------------------------")

print("File not found ERRORS")
for e3 in notFound:
    print("File:" + e3)
print("-------------------------------------------------------------------------")
   
print("Connection ERRORS")
for e4 in ConnectionE:
    print("File:" + e4)
print("-------------------------------------------------------------------------")

print("Unicode Encode ERRORS")
for e5 in UnicodeEncode:
    print("File:" + e5)
print("-------------------------------------------------------------------------")
