with open("input.txt") as f:
    grid = [line.rstrip("\n") for line in f]

height = len(grid)
width = len(grid[0])
for y in range(height):
    for x in range(width):
        if grid[y][x] == 'S':
            start_x = x
            start_y = y
            break

timelines = {start_x: 1}

for y in range(start_y + 1, height):
    next_timelines = {}

    for x, count in timelines.items():
        if x < 0 or x >= width:
            continue

        cell = grid[y][x]
        if cell == '^':
            lx = x - 1
            if lx in next_timelines:
                next_timelines[lx] += count
            else:
                next_timelines[lx] = count

            rx = x + 1
            if rx in next_timelines:
                next_timelines[rx] += count
            else:
                next_timelines[rx] = count
        else:
            if x in next_timelines:
                next_timelines[x] += count
            else:
                next_timelines[x] = count

    timelines = next_timelines
    if not timelines:
        break

print(sum(timelines.values()))