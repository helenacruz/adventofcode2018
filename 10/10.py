import re

class Point:
    def __init__(self, position_x, position_y, velocity_x, velocity_y):
        self.position_x = position_x
        self.position_y = position_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y      

    def move(self):
        self.position_x += self.velocity_x
        self.position_y += self.velocity_y

points = []
with open('input.txt') as file:
    for line in file:
        line = re.findall(r"[-\d']+", line)
        point = Point(int(line[0]), int(line[1]), int(line[2]), int(line[3]))
        points += [point]

def limits():
    max_x = max([p.position_x for p in points])
    min_x = min([p.position_x for p in points])
    max_y = max([p.position_y for p in points])
    min_y = min([p.position_y for p in points])
    return max_x, min_x, max_y, min_y

def is_point(x, y):
    for point in points:
        if point.position_x == x and point.position_y == y:
            return True
    return False

for time in range(15000):
    word_size = 65
    max_x, min_x, max_y, min_y = limits()
    if min_x + word_size >= max_x and min_y + word_size >= max_y:
        print(f'\ntime: {time}')
        for y in range(min_y, max_y + 1, 1):
            for x in range(min_x, max_x + 1, 1):
                if is_point(x, y):
                    print("#", end='', flush=True)
                else:
                    print(".", end='', flush=True)
            print()
    for p in points:
        p.move()
