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

matrix = list(map(lambda line: list(i == '#' for i in line), input_string.split('\n')))

x = 0
y = 0
trees = 0

while y < len(matrix):
    if matrix[y][x % len(matrix[y])]:
        trees += 1
    x += 3
    y += 1

print(trees)
