with open("input.txt", 'r') as file:
    ranges = []
    ids = []
    for line in file:
        line = line.strip()
        if '-' in line:
            ranges.append(line)
        if not line:
            break

ranges_parsed = []
for rng in ranges:
    start, end = map(int, rng.split('-'))
    ranges_parsed.append((start, end))
ranges_parsed.sort()

merged = []
for start, end in ranges_parsed:
    if not merged or start > merged[-1][1] + 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)
fresh = sum(end - start + 1 for start, end in merged)

print(fresh)