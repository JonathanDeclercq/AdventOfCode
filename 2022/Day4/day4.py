"""
AoC Day 4 : Cleaning
"""

def _parseInput(input):
    pairs = []
    with open(input) as lines:
        for line in lines:
            line = line.strip()
            if line:
                pairs.append(line)
    return pairs

def part1():
    count = 0
    for pair in _parseInput('input.txt'):
        pair = pair.split(',')
        a = int(pair[0].split('-')[0])
        b = int(pair[0].split('-')[1])
        c = int(pair[1].split('-')[0])
        d = int(pair[1].split('-')[1])
        if (a <= c and b >= d) or (c <= a and d >= b):
            count += 1
    print(count)

def part2():
    count = 0
    for pair in _parseInput('input.txt'):
        pair = pair.split(',')
        a = int(pair[0].split('-')[0])
        b = int(pair[0].split('-')[1])
        c = int(pair[1].split('-')[0])
        d = int(pair[1].split('-')[1])
        if (a >= c and a <= d) or (c >= a and c <= b) or (b >= c and b <= d) or (d >= a and d <= b):
            count += 1
    print(count)
part2()