import aocd

def count_paths(connections, current, visited, paths):
    if current in paths:
        return paths[current]
    
    if 'out' in connections[current]:
        return 1
    
    total_paths = 0
    for neighbor in connections[current]:
        if neighbor in visited:
            continue
        new_visited = visited | {current}
        total_paths += count_paths(connections, neighbor, new_visited, paths)
    
    paths[current] = total_paths
    return total_paths

def solve(data):
    connections = {}
    lines = data.splitlines()
    for line in lines:
        line = line.split(': ')
        connections[line[0]] = line[1].split(' ')
    
    return count_paths(connections, 'you', set(), {})

if __name__ == "__main__":
    print(solve(open("sample_1.txt").read()))
    print(solve(aocd.get_data(year=2025, day=11)))