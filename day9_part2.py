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

invalid_number = 0

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
        invalid_number = nums[i]
        print(invalid_number)
        break

# Part 2 starts here
start = 0
end = 0

while True:
    set_sum = sum(nums[start:end + 1])
    if set_sum == invalid_number:
        break

    if set_sum < invalid_number or start == end:
        end += 1
    else:
        start += 1

print(min(nums[start:end + 1]) + max(nums[start:end + 1]))
