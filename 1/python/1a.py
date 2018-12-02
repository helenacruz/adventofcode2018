frequency = 0

with open('input.txt') as file:
    for line in file:
        for x in line.split():
            frequency += int(x)

print("frequency: " + str(frequency))