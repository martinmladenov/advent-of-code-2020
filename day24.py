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

print(len(black))
