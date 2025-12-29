import aocd
    
def solve(data):
    lines = data.splitlines()
    rotations = [line.strip() for line in lines]
    
    dial = 50
    password = 0
    for rotation in rotations:
        dir, val = rotation[0], int(rotation[1:])
        dial = dial + val if dir == "R" else dial - val
        if dial % 100 == 0:
            password += 1
            
    return password

if __name__ == "__main__":
    # print(solve(open("sample.txt").read()))
    print(solve(aocd.get_data(year=2025, day=1)))