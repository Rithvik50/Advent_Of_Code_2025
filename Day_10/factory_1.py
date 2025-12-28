from collections import deque

machines = []
with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip().split(' ')
        line[0] = list(line[0].replace('[', '').replace(']', ''))
        for i, elem in enumerate(line[1:]):
            if elem.startswith('(') and elem.endswith(')'):
                line[i + 1] = [int(num.strip()) for num in elem.replace('(', '').replace(')', '').split(',')]
        line.pop()
        machines.append(line)

total_presses = 0
for machine in machines:
    light = machine[0]
    schematics = machine[1:]
    n = len(light)
    target_state = 0
    for i in range(n):
        if light[i] == '#':
            target_state |= (1 << i)

    INF = 2 ** n
    queue = deque([0])
    visited = [False] * (1 << n)
    visited[0] = True
    presses = 0
    while queue:
        for _ in range(len(queue)):
            state = queue.popleft()
            if state == target_state:
                total_presses += presses
                break

            for button in schematics:
                toggled_state = 0
                for i in button:
                    toggled_state |= (1 << i)

                new_state = state ^ toggled_state
                if not visited[new_state]:
                    visited[new_state] = True
                    queue.append(new_state)
        presses += 1

    if visited[target_state] == False:
        total_presses += float('inf')

print(total_presses)
