with open("input.txt", 'r') as file:
    lines = file.readlines()
    rotations = [line.strip() for line in lines]

dial = 50
password = 0
for rotation in rotations:
    dir, val = rotation[0], int(rotation[1:])
    dial = dial + val if dir == "R" else dial - val
    if dial % 100 == 0:
        password += 1
print(password)