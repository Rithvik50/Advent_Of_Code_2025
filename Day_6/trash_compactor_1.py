with open("input.txt", 'r') as file:
    nums = []
    ops = []
    for line in file:
        line = line.strip()
        if '+' not in line and '*' not in line:
            nums.append(line.split())
        else:
            ops = list(line.replace(' ', ''))

total = 0
for col in range(len(nums[0])):
    col_total = 0
    for row in range(len(nums)):
        if ops[col] == '+':
            total += int(nums[row][col])
        elif ops[col] == '*':
            if col_total == 0:
                col_total = 1
            col_total *= int(nums[row][col])
    total += col_total

print(total)