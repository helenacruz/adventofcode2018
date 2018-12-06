coords = set()
infinite = {}
areas = {}

max_x = -1
min_x = 500
max_y = -1
min_y = 500

with open('input.txt') as file:
    for line in file:
        data = line.split(',')
        x = int(data[0])
        y = int(data[1])
        coord = (x, y)
        coords.add(coord)
        infinite[coord] = False
        areas[coord] = 0
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)

grid = max(max_x, max_y) + 1
update = False

for x in range(grid):
    for y in range(grid):
        min_coord = (0, 0)
        min_distance = grid
        for coord in coords:
            distance = abs(coord[0] - x) + abs(coord[1] - y)
            if distance < min_distance:
                min_distance = distance
                min_coord = coord
                update = True
            elif distance == min_distance:
                update = False
        if x == (grid - 1) or x == 0 or y == (grid - 1) or y == 0:
            infinite[min_coord] = True
        if update == True:
            areas[min_coord] = areas.setdefault(min_coord, 0) + 1

max_area = 0
for coord, area in areas.items():
    if not infinite[coord]:
        max_area = max(max_area, area)

print("max_area: " + str(max_area))

max_distance = 10000
region_size = 0
for x in range(grid):
    for y in range(grid):
        total_distance = 0
        for coord in coords:
            total_distance += abs(coord[0] - x) + abs(coord[1] - y)
        if total_distance < max_distance:
            region_size += 1

print("region_size: " + str(region_size))
