import csv
from operator import itemgetter, pos

max = 500
possibilities = []
numbers = []
somme = []
actions = []
percentage_sum = []
total = 0
rewards = 0

with open('actions.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar=',')
    for row in reader:
        if row[0] != '' and row[1] != 'price':
            row[2] = int(row[2])
            row[1] = int(row[1])
            row.append(round(row[1]*row[2]/100,2))
            actions.append(row)

actions = sorted(actions, key=itemgetter(2),reverse=True)

def all_sums(numbers, max, liste=[]):
    somme = sum(liste)
    if somme <= max and liste != [] and somme > max - max/2: 
        possibilities.append(liste)

    if somme > max:
        return

    for i in range(len(numbers)):
        number = numbers[i]
        rest = numbers[i+1:]
        all_sums(rest, max, liste + [number]) 

def replace():
    i = 0
    while i != len(possibilities)-1:
        all = []
        j = 0
        while j != len(possibilities[i]) and len(possibilities[i]) != 0:
            for action in actions:
                if action[1] == possibilities[i][j]:
                    possibilities[i][j] = action[2]
                    all.append(action[0])
                    break
            j+= 1
        percentage_sum.append([possibilities[i],somme[i],all])
        i += 1



for action in actions:
    numbers.append(action[1])

for action in actions:
    numbers.remove(action[1])
    if total + action[1] <= 500:
        total += action[1]
        rewards += action[3]
    else:
        all_sums(numbers, max-total)
        for possibility in possibilities:
            somme.append(sum(possibility))
        replace()
        break

for ps in percentage_sum:
    ps[0] = sum(ps[0])/len(ps[0])

res = sorted(percentage_sum,key=itemgetter(0),reverse=True)[0]

for action in actions:
    for act in res[2]:
        if action[0] == act:
            rewards += action[3]

print(round(rewards,2))