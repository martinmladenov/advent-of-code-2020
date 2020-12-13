input_string = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''

deltas = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

matrix = list(map(lambda line: list(i == '#' for i in line), input_string.split('\n')))

prod = 1

for dx, dy in deltas:
    x = 0
    y = 0
    trees = 0
    while y < len(matrix):
        if matrix[y][x % len(matrix[y])]:
            trees += 1
        x += dx
        y += dy

    prod *= trees
    print(trees)

print(prod)
