guards = {}

with open('input.txt') as file:
    lines = file.readlines()

lines.sort()

for line in lines:
    data = line.split()
    year, month, day = data[0].replace('[', '').split('-')
    minutes = data[1].replace(']', '').split(':')[1]
    minutes = int(minutes)
    if '#' in line:
        guard_id = int(data[3].replace('#', ''))
        if guard_id not in guards:
            guards[guard_id] = [0 for i in range(60)]
    if 'asleep' in line:
        start = minutes
    if 'wakes' in line:
        end = minutes
        for t in range(start, end):
            guards[guard_id][t] += 1

best_guard = 0
best = {}
for e in guards:
    best[e] = sum(guards[e])

time = 0
for e in best:
    if best[e] > time:
        best_guard = e
        time = best[e]

best_minute = guards[best_guard].index(max(guards[best_guard]))

print("guard_id: " + str(best_guard))
print("max_time: " + str(best_minute))
print("multiplied: " + str(best_guard * best_minute))