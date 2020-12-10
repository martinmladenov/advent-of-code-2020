input_string = '''16
10
15
5
1
11
7
19
6
12
4'''

adapters = [0] + list(sorted(map(int, input_string.split('\n'))))
adapters.append(adapters[-1] + 3)

diff1 = 0
diff3 = 0

for i in range(1, len(adapters)):
    diff = adapters[i] - adapters[i - 1]
    if diff == 1:
        diff1 += 1
    elif diff == 3:
        diff3 += 1

print(diff1, diff3, diff1 * diff3)
