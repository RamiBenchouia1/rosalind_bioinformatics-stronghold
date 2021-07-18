from Bio import SeqIO

def gc_composition(inputString):
    total_bases = len(inputString)
    gc_amount = 0
    for ch in inputString:
        if ch == 'G' or ch == 'C':
            gc_amount += 1
    
    gc_comp = (gc_amount/total_bases)*100
    return gc_comp


def answer(inputFile):
    seq_dict = {rec.id : rec.seq for rec in SeqIO.parse(inputFile, "fasta")}
    comparator = 0
    target = ""
    for key in seq_dict:
        value = seq_dict[key]
        gc_ratio = gc_composition(value)
        if gc_ratio > comparator: 
            comparator = gc_ratio
            target = key
    print(target)
    print(comparator)



answer('/Users/ramibenchouia/Documents/CODE/BIOINFORMATICS/ROSALINDA/Bioinformatics Stronghold/Computing GC Content/input.txt')