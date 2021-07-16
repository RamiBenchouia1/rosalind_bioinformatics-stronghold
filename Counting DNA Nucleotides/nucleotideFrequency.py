def readFile(txtFile):
    f = open(txtFile, 'r')
    outputString = f.readline().rstrip('\n')
    f.close()
    return outputString


def createDictionary(strSequence):
    #instantiate new empty dictionary to populate, should only have 4 key-value pairs, with each key representing the nucleotide, and its value representing its frequency in the input string
    ntDict = {}
    
    #loop through each index of input string (each index = a single nucleotide) and if character already in dictionary, increment its value (which serves as a counter) by one; otherwise add it to the dictionary and initialize its value at 1
    for i in range(len(strSequence)):
        nt = strSequence[i]
        if nt in ntDict:
            ntDict[nt]+=1
        else:
            ntDict[nt]=1
    print(ntDict)


createDictionary(readFile('/Users/ramibenchouia/Documents/CODE/BIOINFORMATICS/ROSALINDA/Bioinformatics Stronghold/Counting DNA Nucleotides/rosalind_dna.txt'))


