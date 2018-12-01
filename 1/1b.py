def twice():
    frequency = 0
    frequencies = {}
    frequencies[0] = 1

    while True:
        with open('input.txt') as file:
            for line in file:
                for x in line.split():
                    frequency += int(x)
                    if frequency in frequencies:
                        return frequency
                    frequencies[frequency] = 1

print("twice: " + str(twice()))