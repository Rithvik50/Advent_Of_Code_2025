import aocd

def solve(data):
    ranges = data.strip().split(',')
    
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
                    
    return total

if __name__ == "__main__":
    # print(solve(open("sample.txt").read()))
    print(solve(aocd.get_data(year=2025, day=2)))