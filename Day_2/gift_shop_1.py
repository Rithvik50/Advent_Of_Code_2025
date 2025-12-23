with open("input.txt", 'r') as f:
    ranges = f.read().strip().split(',')

total = 0
for rng in ranges:
    start, end = map(int, rng.split('-'))
    for i in range(start, end + 1):
        id = str(i)
        if id[:len(id)//2] == id[len(id)//2:]:
            total += i
print(total)