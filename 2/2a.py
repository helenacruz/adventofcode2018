letters = { }
two_letters = 0
three_letters = 0

with open('input.txt') as file:
    for line in file:
        for c in line:
            letters[c] = letters.setdefault(c, 0) + 1
        for e in letters:
            if letters[e] == 2:
                two_letters += 1
                break
        for e in letters:
            if letters[e] == 3:
                three_letters += 1
                break
        letters = {}

print("two letters: " + str(two_letters))
print("three letters: " + str(three_letters))
print("checksum: " + str(two_letters * three_letters))
