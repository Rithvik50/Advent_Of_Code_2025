with open("input.txt", 'r') as file:
    grid = [line.strip() for line in file.readlines()]

rows = len(grid)
cols = len(grid[0])
dir = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
      ]
total = 0
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == '@':
            rolls = 0
            for dr, dc in dir:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == '@':
                    rolls += 1
            if rolls < 4:
                total += 1

print(total)