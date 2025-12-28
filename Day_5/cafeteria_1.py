import aocd

def solve(data):
    ranges = []
    ids = []
    lines = data.splitlines()
    for line in lines:
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

    return len(fresh)

if __name__ == "__main__":
    # print(solve(open("sample.txt").read()))
    print(solve(aocd.get_data(year=2025, day=5)))