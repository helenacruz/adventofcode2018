import copy

acres = []

with open("input.txt") as file:
    for line in file:
        line = list(line.strip())
        acres += [line]

def how_many(xx, yy, acre):
    global acres
    sum_acre = 0
    for x in range(xx - 1, xx + 2):
        if x not in range(len(acres[0])):
            continue
        for y in range(yy - 1, yy + 2):
            if y not in range(len(acres)):
                continue
            elif x == xx and y == yy:
                continue
            if acres[y][x] == acre:
                sum_acre += 1
    return sum_acre

def evolve_trees(x, y):
    if how_many(x, y, '|') >= 3:
        return True
    return False

def evolve_lumberyard(x, y):
    if how_many(x, y, '#') >= 3:
        return True
    return False

def remain_lumberyard(x, y):
    if how_many(x, y, '#') >= 1 and how_many(x, y, '|') >= 1:
        return True
    return False  

generations = {}
stable = 0
period = 0
found = False

def save(acres, m):
    global generations
    global stable
    global period
    global found
    tuple_acres = ()
    for e in acres:
        tuple_acres += (tuple(e),)
    if tuple_acres in generations and not found:
        t = generations[tuple_acres] 
        generations[tuple_acres] = (t[0] + 1, t[1] + [m])
        stable = m
        period = m - t[1][0]
        found = True
    else:
        generations[tuple_acres] = (1, [m])

def result():
    global acres
    sum_trees = sum(1 for line in acres for acre in line if acre == '|')
    sum_lumberyards = sum(1 for line in acres for acre in line if acre == '#')
    return sum_lumberyards * sum_trees

def evolve(minutes):
    global acres
    global found
    puzzle = 1000000000
    for m in range(1, minutes + 1):
        new_acres = copy.deepcopy(acres)
        for x in range(len(acres[0])):
            for y in range(len(acres)):
                if acres[y][x] == '.':
                    if evolve_trees(x, y):
                        new_acres[y][x] = '|'
                elif acres[y][x] == '|':
                    if evolve_lumberyard(x, y):
                        new_acres[y][x] = '#'
                elif acres[y][x] == '#':
                    if not remain_lumberyard(x, y):
                        new_acres[y][x] = '.'
        acres = new_acres 
        if m == 10:
            print(f'part 1: {result()}')
        elif found and m == (stable + ((puzzle - stable) % period)):
            print(f'part 2: {result()}')
            return
        save(acres, m)

evolve(1000) 
