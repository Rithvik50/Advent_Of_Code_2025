with open("input.txt", 'r') as file:
    lines = file.readlines()
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
            
print(password)