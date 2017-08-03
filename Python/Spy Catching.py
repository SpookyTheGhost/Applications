sample = ['GTA','GGG','CAC']
def readDNA(dnaFile):
  DNAData = ""
  with open(dnaFile, "r") as f:
    for line in f:
      DNAData += line
  return DNAData

def dnaCodons(dna):
  codons = []
  for x in range(0, len(dna), 3):
      if ( x+3 <= len(dna) ):
          codons.append(dna[x:x+3])
  return codons

def matchDNA(suspectDNA):
  matches = 0
  for i in suspectDNA:
    if (i in sample):
      matches += 1
  return matches

def isCriminal():
  suspects = ["suspect1.txt", "suspect2.txt", "suspect3.txt"]
  for i in range( len(suspects) ):
    suspectFile = readDNA(suspects[i])
    suspectDNA = dnaCodons(suspectFile)
    suspectMatches = matchDNA(suspectDNA)
    
    if (suspectMatches >= 3):
      print("The spy is suspect " + str(i + 1))
      print("Matches %d" % suspectMatches)
    
    else:
      print("Suspect " + str(i + 1) + " is free to go")
      
isCriminal()
