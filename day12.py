input_string = '''F10
N3
F7
R90
F11'''

instructions = list(map(lambda line: (line[0], int(line[1:])), input_string.split('\n')))

x = y = 0
facing = 'E'

nextRight = {'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E'}
nextLeft = {'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E'}

for i, value in instructions:
    if i in ('L', 'R'):
        nextDirection = nextLeft if i == 'L' else nextRight

        for _ in range(value // 90):
            facing = nextDirection[facing]

        continue

    if i == 'F':
        i = facing

    if i == 'E':
        x += value
    elif i == 'W':
        x -= value
    elif i == 'S':
        y += value
    elif i == 'N':
        y -= value

print(abs(x) + abs(y))
