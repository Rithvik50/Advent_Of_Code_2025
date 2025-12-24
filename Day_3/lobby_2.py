with open("input.txt", 'r') as file:
    lines = file.readlines()
    banks = [line.strip() for line in lines]

total = 0
for bank in banks:
    stack = []
    bank_digits = len(bank)
    for i, digit in enumerate(bank):
        while len(stack) > 0 and stack[-1] < digit and len(stack) + (bank_digits - i) > 12:
            stack.pop()
        if len(stack) < 12:
            stack.append(digit)
    total += int("".join(stack))

print(total)