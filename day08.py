input_string = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''

instructions = input_string.split('\n')

acc = 0
visited = set()

i = 0

while i < len(instructions):
    if i in visited:
        break

    visited.add(i)

    spl = instructions[i].split()
    opcode = spl[0]
    value = int(spl[1])

    if opcode == 'acc':
        acc += value
    elif opcode == 'jmp':
        i += value
        continue

    i += 1

print(acc)
