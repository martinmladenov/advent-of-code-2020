input_string = '''0,3,6'''

spl = list(map(int, input_string.split(',')))

for part, limit in [(1, 2020), (2, 30000000)]:

    last_spoken = dict()

    for i in range(len(spl) - 1):
        last_spoken[spl[i]] = i + 1

    last_num = spl[-1]

    for i in range(limit - len(spl)):
        last_index = last_spoken.get(last_num, i + len(spl))
        last_spoken[last_num] = i + len(spl)
        last_num = i + len(spl) - last_index

    print(f'Answer to part {part}: {last_num}')
