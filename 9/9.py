from collections import deque

with open('input.txt') as file:
    data = file.readline().split()
    players = int(data[0])
    last_marble = int(data[6])

print(f'players: {players}')
print(f'last_marble: {last_marble}')

def play_marbles(n):
    score = [0] * players
    marbles = deque([0])
    for marble in range(1, (last_marble + 1) * n):
        if marble % 23 == 0:
            marbles.rotate(-7)
            score[(marble - 1) % players] += marble + marbles.pop()
        else:
            marbles.rotate(2)
            marbles.append(marble)
    return max(score)

# part 1
print(f'Part 1 highest score: {play_marbles(1)}')
# part 2
print(f'Part 2 highest score: {play_marbles(100)}')
