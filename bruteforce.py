import csv
from operator import itemgetter

possibilities = []
actions = []
costs = []
rewards = []
sum_action = []


with open('actions.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar=',')
    for row in reader:
        if row[0] != '' and row[1] != 'price':
            actions.append(row)


def all_sums(numbers, max, liste=[]):
    somme = sum(liste)
    if somme <= max: 
        possibilities.append(liste)

    if somme > max:
        return

    for i in range(len(numbers)):
        number = numbers[i]
        rest = numbers[i+1:]
        all_sums(rest, max, liste + [number]) 

for action in actions:
    costs.append(int(action[1]))
    rewards.append((int(action[1])*int(action[2]))/100)

all_sums(costs,500)

first = []
for ind, possibility in enumerate(possibilities):
    first = []
    for index, item in enumerate(possibility):
        for act_index, action in enumerate(actions):
            if int(action[1]) == item:
                possibilities[ind][index] = rewards[act_index]
                first.append(action[0])
                break
    sum_action.append([first,round(sum(possibility),2)])

sum_action = sorted(sum_action, key=itemgetter(1),reverse=True)

for i in range(10):
    print('Les actions ',end='')
    for j in range(len(sum_action[i][0])):
        print('/' + sum_action[i][0][j], end='')
    print(' donnent un rendement de {} € \n'.format(sum_action[i][1]))