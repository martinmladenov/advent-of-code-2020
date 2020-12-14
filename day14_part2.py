input_string = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''

instructions = input_string.split('\n')


def write_memory(memory, addr, val, mask, i):
    if i >= len(mask):
        memory[addr] = val
        return

    if mask[i] == 'X':
        addr &= ~(1 << (len(mask) - i - 1))
        write_memory(memory, addr, val, mask, i + 1)
        addr |= 1 << (len(mask) - i - 1)
        write_memory(memory, addr, val, mask, i + 1)
    else:
        if mask[i] == '1':
            addr |= 1 << (len(mask) - i - 1)
        write_memory(memory, addr, val, mask, i + 1)


mask_str = ''
mem = dict()

for instruction in instructions:
    spl = instruction.replace('[', ' ').replace(']', ' ').split()

    if spl[0] == 'mask':
        mask_str = spl[2]
    elif spl[0] == 'mem':
        index = int(spl[1])
        value = int(spl[3])
        write_memory(mem, index, value, mask_str, 0)

print(sum(mem.values()))
