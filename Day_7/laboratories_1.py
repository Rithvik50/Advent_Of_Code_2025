import aocd

def solve(data):
    lines = data.splitlines()
    grid = [line.strip() for line in lines]

    height = len(grid)
    width = len(grid[0])
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                start_x = x
                start_y = y
                break

    beams = {start_x}
    splits = 0
    for y in range(start_y + 1, height):
        next_beams = set()
        for x in beams:
            if x < 0 or x >= width:
                continue

            cell = grid[y][x]
            if cell == '^':
                splits += 1
                next_beams.add(x - 1)
                next_beams.add(x + 1)
            else:
                next_beams.add(x)

        beams = next_beams
        if not beams:
            break

    return splits

if __name__ == "__main__":
    # print(solve(open("sample.txt").read()))
    print(solve(aocd.get_data(year=2025, day=7)))