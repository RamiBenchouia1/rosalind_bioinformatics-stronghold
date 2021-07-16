def readFile(txtFile):
    f = open(txtFile, 'r')
    outputString = f.readline().rstrip('\n')
    f.close()
    return outputString

def transcription(codingStrand):
    transcript = ""

    for i in range(len(codingStrand)):
        if codingStrand[i] == 'T':
            transcript += 'U'
        else:
            transcript += codingStrand[i]
    
    print(transcript)


transcription(readFile('/Users/ramibenchouia/Documents/CODE/BIOINFORMATICS/ROSALINDA/Bioinformatics Stronghold/Transcribing DNA into RNA/rosalind_rna.txt'))
