input_string = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''

instructions = input_string.split('\n')

and_mask = or_mask = 0
mem = dict()

for instruction in instructions:
    spl = instruction.replace('[', ' ').replace(']', ' ').split()

    if spl[0] == 'mask':
        and_mask = or_mask = 0
        for c in spl[2]:
            and_mask <<= 1
            or_mask <<= 1
            if c == '1':
                or_mask |= 1
            if c != '0':
                and_mask |= 1
    elif spl[0] == 'mem':
        index = int(spl[1])
        value = int(spl[3]) & and_mask | or_mask
        mem[index] = value

print(sum(mem.values()))
