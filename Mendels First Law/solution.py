# see https://stackoverflow.com/questions/25119106/rosalind-mendels-first-law-iprb


def solution(inputFile):
    with open(inputFile, 'r') as f:
        #dataset = [line for line in f.readlines()]
        dataset = f.readline().split(" ")
        k = int(dataset[0])
        m = int(dataset[1])
        n = int(dataset[2])
    population = k + m + n
    
    events = ['AA+Aa', 'AA+aa', 'Aa+aa', 'AA+AA', 'Aa+Aa', 'aa+aa']

    # get the probability of dominant traits (set up Punnett square)
    punnett_probabilities = {
        'AA+Aa': 1,
        'AA+aa': 1,
        'Aa+aa': .5,
        'AA+AA': 1,
        'Aa+Aa': .75,
        'aa+aa': 0,
    }
    event_probabilities = {}

    # Event: AA+Aa -> P(X=k, Y=m) + P(X=m, Y=k):
    P_km = k / population * m / (population - 1)
    P_mk = m / population * k / (population - 1)
    event_probabilities['AA+Aa'] = P_km + P_mk

    # Event: AA+aa -> P(X=k, Y=n) + P(X=n, Y=k):
    P_kn = k / population * n / (population - 1)
    P_nk = n / population * k / (population - 1)
    event_probabilities['AA+aa'] = P_kn + P_nk

    # Event: Aa+aa -> P(X=m, Y=n) +P(X=n, Y=m):
    P_mn = m / population * n / (population - 1)
    P_nm = n / population * m / (population - 1)
    event_probabilities['Aa+aa'] = P_mn + P_nm

    # Event: AA+AA -> P(X=k, Y=k):
    P_kk = k / population * (k - 1) / (population - 1)
    event_probabilities['AA+AA'] = P_kk

    # Event: Aa+Aa -> P(X=m, Y=m):
    P_mm = m / population * (m - 1) / (population - 1)
    event_probabilities['Aa+Aa'] = P_mm

    # Event: aa+aa -> P(X=n, Y=n) + P(X=n, Y=n) = 0 (will be * 0, so just don't use it)
    event_probabilities['aa+aa'] = 0

    # Total probability is the sum of (prob of dominant factor * prob of the event)
    total_probability = 0
    for event in events:
        total_probability += punnett_probabilities[event] * event_probabilities[event]
    print(round(total_probability, 5))




solution('/Users/ramibenchouia/Documents/CODE/BIOINFORMATICS/ROSALINDA/Bioinformatics Stronghold/Mendels First Law/input.txt')