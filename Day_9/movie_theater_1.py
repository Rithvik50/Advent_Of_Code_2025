corners = []
with open("input.txt", 'r') as file:
    for line in file:
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

print(max_area)