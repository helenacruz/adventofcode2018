max_height = 0
min_height = 1000

max_width = 0
min_width = 1000

file = open('input.txt')

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

    if (height + claim_height + height) > max_height:
        max_height = (height + claim_height + height)
    if (height + claim_height + height) < min_height:
        min_height = (height + claim_height + height)
    if (width + claim_width + width) > max_width:
        max_width = (width + claim_width + width)
    if (width + claim_width + width) < min_width:
        min_width = (width + claim_width + width)

m = [[[] for x in range(max_width)] for y in range(max_height)] 

file.close()
file = open('input.txt')

claims = {}

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
                m[h][w] += [claim_id]

    claims[claim_id] = claim_height * claim_width

file.close()

final_claims = {}

for e in m:
    for f in e:
        if len(f) > 1:
            continue
        for l in f:
            if l in final_claims:
                final_claims[l] += 1
            else:
                final_claims[l] = 1
        
for e in final_claims:
    if final_claims[e] == claims[e]:
        print("clean claim: " + str(e))
