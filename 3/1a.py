import re

max_height = 0
min_height = 1000

max_width = 0
min_width = 1000

with open('input.txt') as file:
    for line in file:
        line = line.split()
        line[0] = line[0].replace('#', '')
        claim_id = int(line[0])
        # print(claim_id)
        line[2] = line[2].replace(':', '')
        line[2] = line[2].split(',')
        width = int(line[2][0])
        height = int(line[2][1])
        #print(width)
        #print(height)
        line[3] = line[3].split('x')
        claim_width = int(line[3][0])
        claim_height = int(line[3][1])
        #print(claim_width)
        #print(claim_height)
        if (height + claim_height + height) > max_height:
            max_height = (height + claim_height + height)
        if (height + claim_height + height) < min_height:
            min_height = (height + claim_height + height)
        if (width + claim_width + width) > max_width:
            max_width = (width + claim_width + width)
        if (width + claim_width + width) < min_width:
            min_width = (width + claim_width + width)
    print("max_width: " + str(max_width))
    print("min_width: " + str(min_width))
    print("max_height: " + str(max_height))
    print("min_height: " + str(min_height))

    m = [[0 for x in range(max_width)] for y in range(max_height)] 
    # print(m)

    with open('input.txt') as file:
        c = 1
        for line in file:
            print(line)
            line = line.split()
            line[0] = line[0].replace('#', '')
            claim_id = int(line[0])
            # print(claim_id)
            line[2] = line[2].replace(':', '')
            line[2] = line[2].split(',')
            width = int(line[2][0])
            height = int(line[2][1])
            #print("w: " + str(width))
            #print("h:" + str(height))
            line[3] = line[3].split('x')
            claim_width = int(line[3][0])
            claim_height = int(line[3][1])
            print("cw: " + str(claim_width))
            print("ch: " + str(claim_height))

            for w in range(width, width + claim_width):
                #print("w: from " + str(width) + "to " + str(width + claim_width))
                for h in range(height, height + claim_height):
                    #print("h: from " + str(height) + "to " + str(height + claim_height))
                    if m[h][w] != 0:
                        m[h][w] = True
                    else:
                        m[h][w] = c
            c += 1
            
            #for e in m:
            #    print(e)
            #print()

    counter = 0
    for e in m:
        for f in e:
            if isinstance(f, bool):
                counter += 1

    print("counter: " + str(counter))