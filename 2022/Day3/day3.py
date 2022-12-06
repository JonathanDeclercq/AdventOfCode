"""
AoC Day 3 : Rucksacks
"""

def _parseInput(input):
    rucksacks = []
    with open(input) as lines:
        for line in lines:
            line = line.strip()
            if line:
                rucksacks.append(line)
    return rucksacks

def _sliceInHalf(string):
    return [string[:len(string)//2],string[len(string)//2:]]

def part1():
    sum = 0
    for line in _parseInput('input.txt'):
        a = list(set(_sliceInHalf(line)[0])&set(_sliceInHalf(line)[1]))
        for i in a:
            sum += (ord(i)-64)+26 if ord(i)<97 else ord(i)-96
    print(sum)

def part2():
    sum = 0
    sacks = _parseInput('input.txt')

    for i,x in enumerate(sacks):
        if i % 3 == 0:
            # print(sacks[i], sacks[i+1], sacks[i+2])
            a = list(set(sacks[i])&set(sacks[i+1])&set(sacks[i+2]))
            for b in a:
                sum += (ord(b)-64)+26 if ord(b)<97 else ord(b)-96
    print(sum)
# part1()
part2()