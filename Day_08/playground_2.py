import aocd

def solve(data):
    lines = data.splitlines()
    points = []
    for line in lines:
        line = line.strip()
        if line:
            points.append(tuple(map(int, line.split(","))))

    n = len(points)

    parent = list(range(n))
    size = [1] * n
    components = n

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

    for _, a, b in edges:
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
            components -= 1

            if components == 1:
                x1 = points[a][0]
                x2 = points[b][0]
                return x1 * x2
            
if __name__ == "__main__":
    # print(solve(open("sample.txt").read()))
    print(solve(aocd.get_data(year=2025, day=8)))