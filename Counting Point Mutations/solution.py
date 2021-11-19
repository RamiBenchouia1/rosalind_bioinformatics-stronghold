def answer(inputFile):
    #read input file
    with open(inputFile,'r') as f:
        dataset = [line.strip() for line in f.readlines()]

    firstSeq = dataset[0]
    secondSeq = dataset[1]

    hammingDistance = 0
    for chInd in range(len(firstSeq)):
        if firstSeq[chInd] != secondSeq[chInd]:
            hammingDistance += 1
    
    print(hammingDistance)


answer('/Users/ramibenchouia/Documents/CODE/BIOINFORMATICS/ROSALINDA/Bioinformatics Stronghold/Counting Point Mutations/input.txt')