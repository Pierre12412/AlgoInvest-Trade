import csv
from operator import itemgetter, pos

max = 500
possibilities = []
costs = []
somme = []
actions = []
percentage_sum = []
total = 0
interests = 0

# Brute force only the rest: (500 - (sum of costs of best percentages))
# and gives list of possibilities to do it
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

# Replace each action cost by percentage of interest
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


# Open file with data and put it in 'actions'
with open('actions.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar=',')
    for row in reader:
        if row[0] != '' and row[1] != 'price':
            row[2] = int(row[2])
            row[1] = int(row[1])
            row.append(round(row[1]*row[2]/100,2))
            actions.append(row)

# Sort actions with their percentage of interests
actions = sorted(actions, key=itemgetter(2),reverse=True)

# Put all costs in a list 'costs'
for action in actions:
    costs.append(action[1])

# While we can add costs of actions with best interests
# we do it, when it become impossible, we brute force the remaining
# actions to obtain the best interests of the rest
for action in actions:
    costs.remove(action[1])
    if total + action[1] <= 500:
        total += action[1]
        interests += action[3]
    else:
        all_sums(costs, max-total)
        for possibility in possibilities:
            somme.append(sum(possibility))
        replace()
        break

# percentage_sum is a list of [[percentage of each action in this possibility],sum of costs, names of actions]
for percentages in percentage_sum:
    percentages[0] = sum(percentages[0])/len(percentages[0])

# Sort the best results of interests for the rest
res = sorted(percentage_sum,key=itemgetter(0),reverse=True)[0]

# Add interests of the rest to global interests
for action in actions:
    for act in res[2]:
        if action[0] == act:
            interests += action[3]

# Show the best interests
print(round(interests,2))