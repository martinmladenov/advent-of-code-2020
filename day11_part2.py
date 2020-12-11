input_string = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''

seats = list(map(lambda line: list(iter(line)), input_string.split('\n')))


def is_outside_grid(grid, seat_x, seat_y):
    return seat_x < 0 or seat_y < 0 or seat_y >= len(grid) or seat_x >= len(grid[seat_y])


def is_occupied(grid, seat_x, seat_y):
    if is_outside_grid(grid, seat_x, seat_y):
        return False

    return grid[seat_y][seat_x] == '#'


def is_empty(grid, seat_x, seat_y):
    if is_outside_grid(grid, seat_x, seat_y):
        return False

    return grid[seat_y][seat_x] == '.'


def get_adj_occupied(grid, seat_x, seat_y):
    adj_occ = 0

    # left
    d = 1
    while is_empty(grid, seat_x - d, seat_y):
        d += 1
    if is_occupied(grid, seat_x - d, seat_y):
        adj_occ += 1

    # down-left
    d = 1
    while is_empty(grid, seat_x - d, seat_y + d):
        d += 1
    if is_occupied(grid, seat_x - d, seat_y + d):
        adj_occ += 1

    # down
    d = 1
    while is_empty(grid, seat_x, seat_y + d):
        d += 1
    if is_occupied(grid, seat_x, seat_y + d):
        adj_occ += 1

    # down-right
    d = 1
    while is_empty(grid, seat_x + d, seat_y + d):
        d += 1
    if is_occupied(grid, seat_x + d, seat_y + d):
        adj_occ += 1

    # right
    d = 1
    while is_empty(grid, seat_x + d, seat_y):
        d += 1
    if is_occupied(grid, seat_x + d, seat_y):
        adj_occ += 1

    # up-right
    d = 1
    while is_empty(grid, seat_x + d, seat_y - d):
        d += 1
    if is_occupied(grid, seat_x + d, seat_y - d):
        adj_occ += 1

    # up
    d = 1
    while is_empty(grid, seat_x, seat_y - d):
        d += 1
    if is_occupied(grid, seat_x, seat_y - d):
        adj_occ += 1

    # up-left
    d = 1
    while is_empty(grid, seat_x - d, seat_y - d):
        d += 1
    if is_occupied(grid, seat_x - d, seat_y - d):
        adj_occ += 1

    return adj_occ


flipped = list([False] * len(r) for r in seats)

while True:
    changed = False
    for y in range(len(seats)):
        for x in range(len(seats[y])):
            adj_occupied = get_adj_occupied(seats, x, y)
            seat_occupied = is_occupied(seats, x, y)

            if adj_occupied == 0 and seats[y][x] == 'L' or \
                    adj_occupied >= 5 and is_occupied(seats, x, y):
                flipped[y][x] = True
                changed = True

    if not changed:
        break

    for y in range(len(seats)):
        for x in range(len(seats[y])):
            if flipped[y][x]:
                flipped[y][x] = False
                if seats[y][x] == 'L':
                    seats[y][x] = '#'
                else:
                    seats[y][x] = 'L'

    # for row in seats:
    #     print(row)
    #
    # print()

print(sum(sum(seat == '#' for seat in row) for row in seats))
