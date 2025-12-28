import aocd
from functools import cache

connections = {}

def parse_data(data):
    global connections
    lines = data.splitlines()
    for line in lines:
        line = line.split(': ')
        connections[line[0]] = line[1].split(' ')

@cache
def count_paths(current, fft_visited, dac_visited):
    if current == 'out':
        return 1 if fft_visited and dac_visited else 0
    
    total_paths = 0
    for neighbor in connections[current]:
        new_fft_visited = fft_visited or (neighbor == 'fft')
        new_dac_visited = dac_visited or (neighbor == 'dac')
        total_paths += count_paths(neighbor, new_fft_visited, new_dac_visited)
        
    return total_paths

if __name__ == "__main__":
    # parse_data(open("sample_2.txt").read())
    parse_data(aocd.get_data(year=2025, day=11))

    print(count_paths('svr', False, False))