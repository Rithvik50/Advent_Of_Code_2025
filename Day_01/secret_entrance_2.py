import aocd

def solve(data):
    lines = data.splitlines()
    rotations = [line.strip() for line in lines]
    
    dial = 50
    password = 0
    for rotation in rotations:
        dir, val = rotation[0], int(rotation[1:])
        step = 1 if dir == "R" else -1
        for _ in range(val):
            dial = (dial + step) % 100
            if dial == 0:
                password += 1
                
    return password

if __name__ == "__main__":
    # print(solve(open("sample.txt").read()))
    print(solve(aocd.get_data(year=2025, day=1)))