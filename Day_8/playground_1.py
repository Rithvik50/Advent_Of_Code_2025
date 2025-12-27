points = []
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            points.append(tuple(map(int, line.split(","))))

n = len(points)
if n <= 20:
    limit = 10
else:
    limit = 1000

parent = list(range(n))
size = [1] * n

edges = []
for i in range(n):
    x1, y1, z1 = points[i]
    for j in range(i + 1, n):
        x2, y2, z2 = points[j]
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        edges.append((dx*dx + dy*dy + dz*dz, i, j))

edges.sort()

connections = 0
for _, a, b in edges:
    if connections == limit:
        break

    ra = a
    while parent[ra] != ra:
        parent[ra] = parent[parent[ra]]
        ra = parent[ra]

    rb = b
    while parent[rb] != rb:
        parent[rb] = parent[parent[rb]]
        rb = parent[rb]

    if ra != rb:
        parent[rb] = ra
        size[ra] += size[rb]

    connections += 1

circuits = {}
for i in range(n):
    r = i
    while parent[r] != r:
        parent[r] = parent[parent[r]]
        r = parent[r]
    circuits[r] = circuits.get(r, 0) + 1

sizes = sorted(circuits.values(), reverse=True)

result = 1
for i in range(min(3, len(sizes))):
    result *= sizes[i]

print(result)