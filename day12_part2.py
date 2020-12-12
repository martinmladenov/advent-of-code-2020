input_string = '''F10
N3
F7
R90
F11'''

instructions = list(map(lambda line: (line[0], int(line[1:])), input_string.split('\n')))

x = 10
y = -1
shipX = shipY = 0

for i, value in instructions:
    if i in ('L', 'R'):
        for _ in range(value // 90):
            x, y = y, x
            if i == 'R':
                x *= -1
            elif i == 'L':
                y *= -1
    elif i == 'F':
        shipX += value * x
        shipY += value * y
    elif i == 'E':
        x += value
    elif i == 'W':
        x -= value
    elif i == 'S':
        y += value
    elif i == 'N':
        y -= value

print(abs(shipX) + abs(shipY))
