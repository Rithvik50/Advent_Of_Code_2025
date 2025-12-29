import aocd

def solve(data):
    ranges = []
    lines = data.splitlines()
    for line in lines:
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

    return fresh

if __name__ == "__main__":
    # print(solve(open("sample.txt").read()))
    print(solve(aocd.get_data(year=2025, day=5)))