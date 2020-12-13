input_string = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''


def get_result(instruction_list):
    acc = 0
    visited = set()

    i = 0

    while i < len(instruction_list):
        if i in visited:
            return None

        visited.add(i)

        spl = instruction_list[i]
        opcode = spl[0]
        value = int(spl[1])

        if opcode == 'acc':
            acc += value
        elif opcode == 'jmp':
            i += value
            continue

        i += 1

    return acc


instructions = list(map(lambda instr: instr.split(), input_string.split('\n')))

reverse_dict = {'jmp': 'nop', 'nop': 'jmp'}

for x in range(len(instructions)):
    instruction = instructions[x]
    if instruction[0] not in reverse_dict:
        continue

    instruction[0] = reverse_dict[instruction[0]]

    result = get_result(instructions)

    if result is not None:
        print(f'changed instruction {x} to {instruction[0]}, result: {result}')
        break

    instruction[0] = reverse_dict[instruction[0]]
