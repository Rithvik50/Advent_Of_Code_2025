with open("input.txt", 'r') as file:
    lines = file.readlines()
    banks = [line.strip() for line in lines]

total = 0
for bank in banks:
    max_joltage = 0
    for i in range(len(bank)-1):
        for j in range(i+1, len(bank)):
            joltage = int(bank[i]+bank[j])
            if joltage > max_joltage:
                max_joltage = joltage
    total += max_joltage
    
print(total)