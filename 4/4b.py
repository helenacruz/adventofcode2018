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

minutes = {}

for e in guards:
    max_times = max(guards[e])
    if max_times == 0:
        continue
    if guards[e].index(max(guards[e])) in minutes:
        minutes[guards[e].index(max(guards[e]))] += [[e, max_times]]
    else:
        minutes[guards[e].index(max(guards[e]))] = [[e, max_times]]

guard_id = 0
max_times = 0
minute = 0
for m in minutes:
    for e in minutes[m]:
        if e[1] > max_times:
            minute = m
            guard_id = e[0]
            max_times = e[1]

print("guard: " + str(guard_id))
print("minute: " + str(minute))
print("multiplied: " + str(guard_id * minute))