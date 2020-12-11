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


def get_ways(arr, i, dp):
    if i == len(arr) - 1:
        return 1

    if dp[i] != 0:
        return dp[i]

    w = 0
    j = i + 1
    while j < len(arr) and arr[i] + 3 >= arr[j]:
        w += get_ways(arr, j, dp)
        j += 1

    dp[i] = w
    return w


adapters = [0] + list(sorted(map(int, input_string.split('\n'))))
adapters.append(adapters[-1] + 3)

ways = get_ways(adapters, 0, [0] * len(adapters))

print(ways)
