def twice():
    frequency = 0
    frequencies = {0}

    while True:
        with open('input.txt') as file:
            for line in file:
                for x in line.split():
                    frequency += int(x)
                    if frequency in frequencies:
                        return frequency
                    frequencies.add(frequency)

print("twice: " + str(twice()))