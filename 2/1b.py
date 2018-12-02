words = []

max_match = 0
match_words = []

def match(word1, word2):
    #print(word1)
    #print(word2)
    global max_match
    global match_words
    match = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            match += 1
    if match > max_match:
        max_match = match
        match_words = [word1, word2]
    return match

with open('input.txt') as file:
    for line in file:
        for word in line.split():
            words += [word]

# print(words)

for word in words:
    new_words = words.copy()
    if word in new_words:
        new_words.remove(word)
    for w in new_words:
        match(word, w)
        #print(match(word, w))

print("max_match: " + str(max_match))
print(match_words)

matching_chars = ""

for i in range(len(match_words[0])):
    if match_words[0][i] == match_words[1][i]:
        matching_chars += match_words[0][i]

print("matching: " + str(matching_chars))