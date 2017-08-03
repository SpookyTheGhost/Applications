file1 = input("What is the first file name?")
file2 = input("What is the second file name?")
try :
	file1Content = open("test.txt", "r", -1, "utf-8")
	file2Content = open("test.txt", "r", -1, "utf-8")
except FileNotFoundError:
	print("File was not found, please check file name and that current directory matches where the file is located")

fileList1 = []
fileList2 = []
for f1, f2 in zip(file1Content, file2Content):
	split1 = f1.split("\t")
	split2 = f2.split("\t")
	for x in split1:
		fileList1.append(str(f1).strip())

	for y in split1:
		fileList2.append(str(f2).strip())

removeDups = []
for s1, s2 in zip(fileList1, fileList2):
	if s1 != s2 and (!(s1 in removeDups) or ! (s2 in removeDups)):
		removeDups.append(s1)
		removeDups.append(s2)

file1Content.close()
file2Content.close()

o = open("output.txt", "w", -1, "utf-8")
for line in removeDups:
	o.write(line)
o.close()
