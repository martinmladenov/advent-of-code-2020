import re

input_string = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''

pws = list(map(lambda x: re.split('-|:? ', x), input_string.split('\n')))

count = 0

for pw in pws:
    minc = int(pw[0])
    maxc = int(pw[1])
    ch = pw[2]

    actual = pw[3].count(ch)

    if minc <= actual <= maxc:
        count += 1

print(count)
