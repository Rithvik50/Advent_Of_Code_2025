with open("input.txt", 'r') as file:
    ranges = []
    ids = []
    for line in file:
        line = line.strip()
        if not line:
            continue
        if '-' in line:
            ranges.append(line)
        else:
            ids.append(int(line))

fresh = set()
for rng in ranges:
    start, end = map(int, rng.split('-'))
    for id in ids:
        if start <= id <= end:
            fresh.add(id)

print(len(fresh))