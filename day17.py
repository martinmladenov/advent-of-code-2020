input_string = '''.#.
..#
###'''

active = set()

lines = input_string.split('\n')

for y in range(len(lines)):
    line = lines[y]
    for x in range(len(line)):
        if line[x] == '#':
            active.add((x, y, 0))

for _ in range(6):
    active_neighbors = dict()
    for x, y, z in active:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    if dx == dy == dz == 0:
                        continue
                    neighbor = (x + dx, y + dy, z + dz)
                    active_neighbors[neighbor] = active_neighbors.get(neighbor, 0) + 1

    to_remove = set()
    for cube in active:
        if active_neighbors.get(cube, 0) not in (2, 3):
            to_remove.add(cube)

    active.difference_update(to_remove)

    for cube in active_neighbors:
        if active_neighbors[cube] == 3:
            active.add(cube)

print(len(active))
