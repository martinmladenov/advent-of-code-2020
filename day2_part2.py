import re

input_string = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''

pws = list(map(lambda x: re.split('-|:? ', x), input_string.split('\n')))

count = 0

for pw in pws:
    i1 = int(pw[0])
    i2 = int(pw[1])
    ch = pw[2]
    pw_str = pw[3]

    if pw_str[i1-1] == ch and pw_str[i2-1] != ch \
            or pw_str[i1-1] != ch and pw_str[i2-1] == ch:
        count += 1

print(count)
