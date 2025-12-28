import aocd

def solve(data):
    corners = []
    lines = data.splitlines()
    for line in lines:
        line = line.strip()
        x, y = map(int, line.split(","))
        corners.append((x, y))

    max_area = 0
    for a in range(len(corners)-1):
        for b in range(1, len(corners)):
            x1, y1 = corners[a]
            x2, y2 = corners[b]
            area = (abs(x1-x2) + 1) * (abs(y1-y2) + 1)
            if area > max_area:
                max_area = area

    return max_area

if __name__ == "__main__":
    # print(solve(open("sample.txt").read()))
    print(solve(aocd.get_data(year=2025, day=9)))