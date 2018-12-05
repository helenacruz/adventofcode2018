# read large string, remove last \n
# result is a list where each character in the string is an element of the list

with open('input.txt') as file:
    line = file.read().strip()

def react(line):
    i = 0
    while i < len(line) - 1:
        if line[i] == line[i + 1].swapcase():
            line = line[:i] + line[i + 2:]
            i = max(0, i - 1)   
        else:
            i += 1
    return len(line)

# part 1
print(react(line))

chars = set(line)
min_length = len(line)
for c in chars:
    new_line = line.replace(c, '')
    new_line = new_line.replace(c.upper(), '')
    min_length = min(min_length, react(new_line))

# part 2
print(min_length)