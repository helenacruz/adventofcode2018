letters = { }
two_letters = 0
three_letters = 0

with open('input.txt') as file:
    for line in file:
        for word in line.split():
            for c in word:
                if c in letters:
                    letters[c] += 1
                else:
                    letters[c] = 1
            # print(letters)
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
