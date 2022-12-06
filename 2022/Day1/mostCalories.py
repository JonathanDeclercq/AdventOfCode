from collections import defaultdict

calories = []
elves = defaultdict(list)
totals = []
i = 0
j = 0
with open("input.txt") as f:
    for line in f:
        calories.append([int(x) for x in line.split()])
for x in calories:
    if (x):
        # print(x)
        elves[i] += x
    else:
        # print('empty')
        i += 1
for x in elves:
    totals.append(sum(elves[x]))
    j += 1
print(max(totals))