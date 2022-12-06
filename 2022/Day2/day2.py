"""
AoC Day2 : Rock Paper Scissors
"""

def _parseInput(input):
    pairs = []
    with open(input) as lines:
        for line in lines:
            line = line.strip()
            if line:
                pairs.append(line.split(" "))
    return pairs

def _solveRPS(pair):
    """
    ABC = Opponent
    XYZ = Player
    ABC = RPS
    Part 1 : XYZ = Rock, Paper, Scissors
    Part 2 : XYZ = Lose, Draw, Win
    """
    points = 0
    match pair[0]:
        case 'A':
            match pair[1]:
                case 'X':
                    points += 3
                case 'Y':
                    points += 4
                case 'Z':
                    points += 8
        case 'B':
            match pair[1]:
                case 'X':
                    points += 1
                case 'Y':
                    points += 5
                case 'Z':
                    points += 9
        case 'C':
            match pair[1]:
                case 'X':
                    points += 2
                case 'Y':
                    points += 6
                case 'Z':
                    points += 7
    return points

def solve():
    pairs = _parseInput('_input.txt')
    score = 0
    for pair in pairs:
       score += _solveRPS(pair)
    print(score)
    
# print(_parseInput("input.txt"))
# print(_solveRPS([['B', 'Z']]))
solve()