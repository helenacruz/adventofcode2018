rules = {}

with open('input.txt') as file:
    initial_state = file.readline().replace(' ', '').strip().split(':')[1]
    for line in file:
        if line != '\n':
            line = line.strip().replace(' ', '').split('=>')
            rules[line[0]] = line[1]

def change_char(l, i, c):
    l = list(l)
    l[i] = c
    l = ''.join(l)
    return l

previous_generation = initial_state 
zero_index = 0

def sum_plants():
    sum_plants = 0
    for i in range(len(previous_generation)):
        if previous_generation[i] == '#':
            if i < zero_index:
                sum_plants -= zero_index - i
            elif i == zero_index:
                continue # sum_plants += 0
            else:
                sum_plants += i - zero_index
    return sum_plants

def evolve(n):
    global zero_index
    global previous_generation
    for _ in range(n):
        if previous_generation[:3] != '...':
            previous_generation = "..." + previous_generation
            zero_index += 3
        if previous_generation[-3:] != '...':
            previous_generation = previous_generation + "..."
        next_generation = previous_generation
        for n in range(len(previous_generation) - 4):
            pots = previous_generation[n : n + 5]
            if pots in rules:
                next_generation = change_char(next_generation, n + 2, rules[pots])
            else:
                next_generation = change_char(next_generation, n + 2, '.')
        previous_generation = next_generation
    return sum_plants()
    
# part 1
print(f'sum_plants: {evolve(20)}')
# part 2
# print(f'sum_plants: {evolve(50000000000)}')