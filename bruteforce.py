possibilities = []
numbers = [1,5,4,2,3,6,11,22]


def all_sums(numbers, max, liste):
    somme = sum(liste)
    if somme <= max: 
        possibilities.append(liste)

    if somme > max:
        return

    for i in range(len(numbers)):
        number = numbers[i]
        rest = numbers[i+1:]
        all_sums(rest, max, liste + [number]) 

all_sums(numbers=numbers,max=10,liste=[])
for possibility in possibilities:
    print(possibility)