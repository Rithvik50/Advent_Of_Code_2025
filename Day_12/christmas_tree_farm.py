import aocd

def solve(data):
    parts = data.split('\n\n')
    presents = parts[:-1]
    sizes = {}
    for present in presents:
        lines = present.splitlines()
        name = int(lines[0][:-1])
        G = [list(row) for row in lines[1:]]
        size = 0
        for row in G:
            for c in row:
                if c == '#':
                    size += 1
        sizes[name] = size

    ans = 0
    regions = parts[-1]
    for region in regions.splitlines():
        sz, ns = region.split(': ')
        R, C = [int(x) for x in sz.split('x')]
        ns = [int(x) for x in ns.split()]
        total_present_size = sum(n*sizes[i] for i,n in enumerate(ns))
        total_grid_size = R * C
        if total_present_size * 1.3 < total_grid_size:
            ans += 1
        elif total_present_size > total_grid_size:
            pass

    return ans

if __name__ == "__main__":
    # print(solve(open("sample.txt").read()))
    print(solve(aocd.get_data(year=2025, day=12)))