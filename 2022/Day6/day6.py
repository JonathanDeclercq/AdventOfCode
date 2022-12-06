"""
AoC Day 6 : Tuning Trouble
"""
def _parseInput(input):
    frequencies = ''
    with open(input) as lines:
        for line in lines:
            line = line.strip()
            if line:
                frequencies += line
    return frequencies

def part1():
    frequencies = _parseInput('input.txt')
    for i in range(0, len(frequencies)):
        # print(frequencies[i])
        if i<=3:
            pass
        elif len(set(frequencies[i-4:i])) == len(frequencies[i-4:i]):
            return(i)
        
def part2():
    frequencies = _parseInput('input.txt')
    for i in range(0, len(frequencies)):
        # print(frequencies[i])
        if i<=13:
            pass
        elif len(set(frequencies[i-14:i])) == len(frequencies[i-14:i]):
            return(i)

print(part2())