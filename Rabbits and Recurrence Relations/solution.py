def recurrence(inputFile):
    with open(inputFile, 'r') as f:
        line = f.readline()
        arr = line.split(" ")
        n = int(arr[0])
        k = int(arr[1])
    pop = [0]*n
    pop[0] = 1
    pop[1] = 1
    current_generation = 2
    while (current_generation < n):
        pop[current_generation] = k*pop[current_generation-2] + pop[current_generation-1]
        current_generation+=1
    print(pop)





recurrence('/Users/ramibenchouia/Documents/CODE/BIOINFORMATICS/ROSALINDA/Bioinformatics Stronghold/Rabbits and Recurrence Relations/rosalind_fib.txt')