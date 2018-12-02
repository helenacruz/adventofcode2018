# read large string, remove last \n
# result is a list where each character in the string is an element of the list

with open('input.txt') as file:
    data = list(file.read())
    del data[-1]

# read numbers by line
# result is a list of lists of integers: [ [], [], [], ... ]

with open('input2.txt') as file:
    data = [[int(x) for x in line.split()] for line in file]
    print(data)

# read words by line
# result is a list of lists of strings: [ [], [], [], ... ]

with open('input2.txt') as file:
    data = [[x for x in line.split()] for line in file]
    print(data)

