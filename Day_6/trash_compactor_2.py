input_data = open("input.txt", 'r').read().split('\n')    

matrix = []
for line in input_data[:-1]:
    matrix.append([val for val in line])
ops = list(input_data[-1].replace(' ', ''))[::-1]

total = 0
equations = [[] for _ in range(len(ops))]
eq_counter = 0
for col in range(len(matrix[0])-1, -1, -1):
    if eq_counter == len(equations):
        break
    
    col_vals = [matrix[row][col] for row in range(len(matrix))]
    if all(x == ' ' for x in col_vals):
        eq_counter += 1
        continue
    
    operand = int(''.join(val for val in col_vals if val != ' '))
    equations[eq_counter].append(operand)

for index, eq in enumerate(equations):
    eq_result = 0 if ops[index] == '+' else 1
    for i in range(len(eq)):
        if ops[index] == '+':
            eq_result += eq[i]
        elif ops[index] == '*':
            eq_result *= eq[i]
    total += eq_result

print(total)