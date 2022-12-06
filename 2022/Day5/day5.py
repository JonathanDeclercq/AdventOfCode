"""
AoC Day 5 : Crates

[G]                 [D] [R]        
[W]         [V]     [C] [T] [M]    
[L]         [P] [Z] [Q] [F] [V]    
[J]         [S] [D] [J] [M] [T] [V]
[B]     [M] [H] [L] [Z] [J] [B] [S]
[R] [C] [T] [C] [T] [R] [D] [R] [D]
[T] [W] [Z] [T] [P] [B] [B] [H] [P]
[D] [S] [R] [D] [G] [F] [S] [L] [Q]
 1   2   3   4   5   6   7   8   9 
"""
col1 = ['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G']
col2 = ['S', 'W', 'C']
col3 = ['R', 'Z', 'T', 'M']
col4 = ['D', 'T', 'C', 'H', 'S', 'P', 'V']
col5 = ['G', 'P', 'T', 'L', 'D', 'Z']
col6 = ['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'B']
col7 = ['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R']
col8 = ['L', 'H', 'R', 'B', 'T', 'V ', 'M']
col9 = ['Q', 'P', 'D', 'S', 'V']

def _parseInput(input):
    moves = []
    with open(input) as lines:
        for line in lines:
            line = line.strip()
            if line:
                moves.append(line)
    return moves

def _crane(move):
    move = move.split(' ')
    amount = int(move[1])
    source = 'col' + move[3]
    destination = 'col' + move[5]
    for i in range(0, amount):
        globals()[destination].append(globals()[source][-1])
        globals()[source].pop()

def _crane9001(move):
    move = move.split(' ')
    amount = int(move[1])
    source = 'col' + move[3]
    destination = 'col' + move[5]
    for i in range(0, amount):
        globals()[destination].append(globals()[source][len(globals()[source])-amount+i])
        globals()[source].pop(len(globals()[source])-amount+i)

def part1():
    for move in _parseInput('input.txt'):
        _crane(move)
    print(col1[-1]+col2[-1]+col3[-1]+col4[-1]+col5[-1]+col6[-1]+col7[-1]+col8[-1]+col9[-1])

def part2():
    for move in _parseInput('input.txt'):
        _crane9001(move)
    print(col1[-1]+col2[-1]+col3[-1]+col4[-1]+col5[-1]+col6[-1]+col7[-1]+col8[-1]+col9[-1])
part2()