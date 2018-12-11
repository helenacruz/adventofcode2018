puzzle_input = 6392

grid_size = 300
grid_serial = puzzle_input

def calculate_power(x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_serial
    power_level *= rack_id
    if power_level >= 100:
        power_level //= 100
        power_level = str(power_level)
        power_level = power_level[-1]
        power_level = int(power_level)
    else:
        power_level = 0
    power_level -= 5
    return power_level

def calculate_power_grid(x, y, square_size):
    if x >= (grid_size - square_size) or y >= (grid_size - square_size):
        return
    total_power = 0
    for yy in range(y, y + square_size):
        for xx in range(x, x + square_size):
            total_power += grid[xx][yy]
    power[x + 1, y + 1, square_size] = total_power

grid = [[0 for x in range(grid_size)] for y in range(grid_size)] 

for yy in range(grid_size):
    for xx in range(grid_size):
        grid[xx][yy] = calculate_power(xx + 1, yy + 1)

power = {}

# i kinda cheated and submitted the value once it stopped changing
# waiting for this to finish would take a looong time
for square_size in range(1, 301, 1):
    print(f'square_size: {square_size}')
    for yy in range(grid_size):
        for xx in range(grid_size):
            calculate_power_grid(xx, yy, square_size)
    pos = max(power, key=lambda key: power[key])
    max_power = power[pos]
    power.clear()
    power[pos] = max_power
    print(f'{pos} power: {max_power}')

# part 1 and part 2
print(max(power, key=lambda key: power[key]))