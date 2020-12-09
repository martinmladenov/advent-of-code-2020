input_string = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''

nums = list(map(int, input_string.split('\n')))

preamble_length = 5  # change to 25 when running with actual input

for i in range(preamble_length, len(nums)):
    found = False
    for i1 in range(i - preamble_length, i):
        for i2 in range(i - preamble_length, i):
            if nums[i1] + nums[i2] == nums[i]:
                found = True
                break
        if found:
            break

    if not found:
        print(nums[i])
        break
