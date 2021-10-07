import csv
from operator import itemgetter
import time
start_time = time.time()

possibilities = []
actions = []
costs = []
rewards = []
sum_action = []

# Open file with data and put it in 'actions'
with open('actions.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar=',')
    for row in reader:
        if row[0] != '' and row[1] != 'price':
            actions.append(row)

# Brute force all possibilities to do 500 with actions costs (in list of lists of costs) (with a min of 450)
def all_sums(numbers, max, liste=[]):
    somme = sum(liste)

    # Put a min of 450 allows a faster algorithm
    if somme <= max and somme >= 450 and liste != []: 
        possibilities.append(liste)

    if somme > max:
        return

    for i in range(len(numbers)):
        number = numbers[i]
        rest = numbers[i+1:]
        all_sums(rest, max, liste + [number]) 


for action in actions:
    # retrieve cost of each action
    costs.append(int(action[1]))
    # retrieve interest of each action
    rewards.append((int(action[1])*int(action[2]))/100)

all_sums(costs,500)

# replace each posibility list to do 500 by their interest
# and save the sum of each list of interest (making total interests)
total_actions_name = []
for ind, possibility in enumerate(possibilities):
    total_actions_name = []
    for index, item in enumerate(possibility):
        for act_index, action in enumerate(actions):
            if int(action[1]) == item:
                possibilities[ind][index] = rewards[act_index]
                total_actions_name.append(action[0])
                break
    sum_action.append([total_actions_name,round(sum(possibility),2)])

# Sort sum_action to have the best interests in first
sum_action = sorted(sum_action, key=itemgetter(1),reverse=True)

# Show ten first results
for i in range(10):
    print('Les actions ',end='')
    for j in range(len(sum_action[i][0])):
        print('/' + sum_action[i][0][j], end='')
    print(' donnent un rendement de {} € \n'.format(sum_action[i][1]))

print("--- %s seconds ---" % (time.time() - start_time))