def readFile(inputTxt):
    f = open(inputTxt,'r')
    outputString = f.readline().rstrip('\n')
    f.close()
    return outputString


def reverseComplement(inputString):
    reverseString = inputString[::-1]
    revComp = ""
    for i in range(len(reverseString)):
        if reverseString[i] == 'A':
            revComp += 'T'
        elif reverseString[i] == 'T':
            revComp += 'A'
        elif reverseString[i] == 'G':
            revComp += 'C'
        else: 
            revComp += 'G'
    
    print(revComp)


reverseComplement(readFile('/Users/ramibenchouia/Documents/CODE/BIOINFORMATICS/ROSALINDA/Bioinformatics Stronghold/Complementing a Strand of DNA/rosalind_revc.txt'))