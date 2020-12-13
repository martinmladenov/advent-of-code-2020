input_string = '''939
7,13,x,x,59,x,31,19'''

timestamp_str, busses = input_string.split('\n')

timestamp = int(timestamp_str)

min_wait = float('inf')
min_bus = 0

for bus_str in busses.split(','):
    if bus_str == 'x':
        continue

    bus = int(bus_str)
    wait = bus - (timestamp % bus)
    if wait < min_wait:
        min_wait = wait
        min_bus = bus

print(min_bus * min_wait)
