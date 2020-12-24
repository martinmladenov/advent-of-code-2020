input_string = '''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew'''

black = set()

for line in input_string.split('\n'):
    x = y = z = 0
    i = 0
    while i < len(line):
        c = line[i]
        if c == 'e':
            x += 1
            y -= 1
        elif c == 'w':
            x -= 1
            y += 1
        elif c == 's':
            i += 1
            n = line[i]
            if n == 'e':
                y -= 1
            elif n == 'w':
                x -= 1
            z += 1
        elif c == 'n':
            i += 1
            n = line[i]
            if n == 'e':
                x += 1
            elif n == 'w':
                y += 1
            z -= 1
        i += 1
    tile = (x, y, z)
    if tile in black:
        black.remove(tile)
    else:
        black.add(tile)

for _ in range(100):
    n_neighbors = dict()
    for x, y, z in black:
        for p in (-1, 1):
            for dx, dy, dz in ((-1, 1, 0), (-1, 0, 1), (0, -1, 1)):
                t = (x + dx * p, y + dy * p, z + dz * p)
                if t in n_neighbors:
                    n_neighbors[t] += 1
                else:
                    n_neighbors[t] = 1

    for t in black:
        if t not in n_neighbors:
            n_neighbors[t] = 0

    for t in n_neighbors:
        n = n_neighbors[t]
        if t in black:
            if n == 0 or n > 2:
                black.remove(t)
        else:
            if n == 2:
                black.add(t)

print(len(black))
