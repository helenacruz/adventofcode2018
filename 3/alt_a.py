file = open('input.txt')

fabric = {}

for line in file:
    line = line.split()
    line[0] = line[0].replace('#', '')
    claim_id = int(line[0])

    line[2] = line[2].replace(':', '')
    line[2] = line[2].split(',')
    width = int(line[2][0])
    height = int(line[2][1])

    line[3] = line[3].split('x')
    claim_width = int(line[3][0])
    claim_height = int(line[3][1])

    for w in range(width, width + claim_width):
        for h in range(height, height + claim_height):
            if (w, h) in fabric:
                fabric[(w, h)] = 'X'
            else:
                fabric[(w, h)] = claim_id

file.close()
    
counter = 0
for e in fabric:
    if fabric[e] == 'X':
        counter += 1

print("counter: " + str(counter))