input_string = '''Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...'''


def rotate(tile):
    return list(map(list, zip(*tile[::-1])))


def get_row(tile, row):
    return tile[row]


def get_col(tile, col):
    arr = list()
    for row in tile:
        arr.append(row[col])
    return arr


def find_match_down(curr_id, curr_tile, tiles):
    border = get_row(curr_tile, -1)
    for other_id in tiles:
        if other_id == curr_id:
            continue
        other = tiles[other_id]

        for _ in range(4):
            if get_row(other, 0) == border:
                return other_id, other
            if get_row(other, 0) == border[::-1]:
                return other_id, list(map(lambda x: x[::-1], other))
            other = rotate(other)

    return -1, None


def find_match_right(curr_id, curr_tile, tiles):
    border = get_col(curr_tile, -1)
    for other_id in tiles:
        if other_id == curr_id:
            continue
        other = tiles[other_id]

        for _ in range(4):
            if get_col(other, 0) == border:
                return other_id, other
            if get_col(other, 0) == border[::-1]:
                return other_id, other[::-1]
            other = rotate(other)

    return -1, None


# Parse tiles
tiles = dict()
for tile_str in input_string.split('\n\n'):
    tile_spl = tile_str.split('\n')
    num = int(tile_spl[0].split()[1][:-1])
    tile = list()
    for line in tile_spl[1:]:
        tile.append(list(x == '#' for x in line))
    tiles[num] = tile

grid = list()

# Find upper left corner
for corner_id in tiles:
    possible_corner = tiles[corner_id]
    for _ in range(4):
        did, dtile = find_match_down(corner_id, possible_corner, tiles)
        rid, rtile = find_match_right(corner_id, possible_corner, tiles)

        if rid == did == -1:
            tiles.pop(corner_id)
            grid.append([(corner_id, rotate(rotate(possible_corner)))])
            break

        possible_corner = rotate(possible_corner)

    if len(grid) > 0:
        break

# Find first row
while True:
    curr_id, curr_tile = grid[0][-1]
    rid, rtile = find_match_right(curr_id, curr_tile, tiles)
    if rid == -1:
        break
    grid[0].append((rid, rtile))
    tiles.pop(rid)

# Find all other rows
for i in range(len(grid[0])):
    j = 1
    while True:
        curr_id, curr_tile = grid[j - 1][i]
        did, dtile = find_match_down(curr_id, curr_tile, tiles)
        if did == -1:
            break
        if i == 0:
            grid.append(list())
        grid[j].append((did, dtile))
        tiles.pop(did)
        j += 1

# Remove borders and assemble full image
full_image = list()
for x in range(len(grid)):
    for c in range(len(grid[x][0][1]) - 2):
        line = list()
        for _, z in grid[x]:
            line += z[c + 1][1:-1]
        full_image.append(line)

# Parse monster
monster_str = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''

monster = list()
for line in monster_str.split('\n'):
    monster.append(list(x == '#' for x in line))

monsters_found = 0
while monsters_found == 0:
    for i in range(4):

        for y in range(len(full_image) - len(monster)):
            for x in range(len(full_image[0]) - len(monster[0])):

                is_monster = True
                for dy in range(len(monster)):
                    for dx in range(len(monster[0])):
                        if monster[dy][dx] and not full_image[y + dy][x + dx]:
                            is_monster = False
                            break
                    if not is_monster:
                        break
                if is_monster:
                    monsters_found += 1

        if monsters_found > 0:
            break

        full_image = rotate(full_image)
    full_image = full_image[::-1]

blocks_per_monster = 0
for y in range(len(monster)):
    for x in range(len(monster[0])):
        if monster[y][x]:
            blocks_per_monster += 1

total_blocks = 0
for y in range(len(full_image)):
    for x in range(len(full_image[0])):
        if full_image[y][x]:
            total_blocks += 1

print(total_blocks - blocks_per_monster * monsters_found)
