input_string = '''1721
979
366
299
675
1456'''


def find_pair():
    for i1 in ints:
        for i2 in ints:
            if i1 + i2 == 2020:
                return i1, i2


ints = list(map(int, input_string.split('\n')))

f1, f2 = find_pair()

print(f1, f2, f1 * f2)
