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


def get_row(tile, row):
    return tile[row]


def get_col(tile, col):
    arr = list()
    for row in tile:
        arr.append(row[col])
    return arr


tiles = list()

for tile_str in input_string.split('\n\n'):
    tile_spl = tile_str.split('\n')
    num = int(tile_spl[0].split()[1][:-1])
    tile = list()
    for line in tile_spl[1:]:
        tile.append(list(x == '#' for x in line))
    tiles.append((num, tile))

prod = 1

for corner_id, possible_corner in tiles:
    num_edges = 0
    for c_edge in (get_row(possible_corner, 0), get_row(possible_corner, -1),
                   get_col(possible_corner, 0), get_col(possible_corner, -1)):
        found = False
        for other_id, other in tiles:
            if corner_id == other_id:
                continue
            for o_edge in (get_row(other, 0), get_row(other, -1),
                           get_col(other, 0), get_col(other, -1)):
                for flip_corner in (1, -1):
                    for flip_other in (1, -1):
                        if c_edge[::flip_corner] == o_edge[::flip_other]:
                            found = True
                            break

                    if found:
                        break
                if found:
                    break
            if found:
                break

        if not found:
            num_edges += 1

    if num_edges == 2:
        prod *= corner_id

print(prod)
