import csv
from operator import itemgetter

actions = []
total = 0
rewards = 0

with open('actions.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar=',')
    for row in reader:
        if row[0] != '' and row[1] != 'price':
            row[2] = int(row[2])
            row[1] = int(row[1])
            actions.append(row)

actions = sorted(actions, key=itemgetter(2),reverse=True)

for action in actions:
    if total + action[1] <= 500:
        total += action[1]
        rewards += round((action[1]*(action[2]/100)),2)
    
print(round(rewards,2))