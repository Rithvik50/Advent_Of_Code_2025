with open("input.txt", 'r') as f:
    ranges = f.read().strip().split(',')

total = 0
for rng in ranges:
    start, end = map(int, rng.split('-'))
    for i in range(start, end + 1):
        id = str(i)
        length = len(id)
        for sub_len in range(1, length // 2 + 1):
            if length % sub_len == 0:
                pattern = id[:sub_len]
                repeats = length // sub_len
                if pattern * repeats == id and repeats >= 2:
                    total += i
                    break
print(total)