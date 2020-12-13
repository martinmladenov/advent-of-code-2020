input_string = '''939
7,13,x,x,59,x,31,19'''

busses_arr = input_string.split('\n')[1].split(',')

busses = list()
for i in range(len(busses_arr)):
    if busses_arr[i] == 'x':
        continue

    busses.append((int(busses_arr[i]), i))

timestamp = 0
lcm = 1
for x, i in busses:
    while (timestamp + i) % x != 0:
        timestamp += lcm

    lcm *= x

print(timestamp)
