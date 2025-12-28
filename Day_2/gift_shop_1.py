import aocd

def solve(data):
    ranges = data.strip().split(',')
    
    total = 0
    for rng in ranges:
        start, end = map(int, rng.split('-'))
        for i in range(start, end + 1):
            id = str(i)
            if id[:len(id)//2] == id[len(id)//2:]:
                total += i
                
    return total

if __name__ == "__main__":
    # print(solve(open("sample.txt").read()))
    print(solve(aocd.get_data(year=2025, day=2)))