input_string = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''

rule_strs, messages = map(lambda s: s.split('\n'), input_string.split('\n\n'))

rules_arr = dict()

for n_str, rule_str in map(lambda x: x.split(': '), rule_strs):
    rule = rule_str.strip('"') if '"' in rule_str \
        else list(map(lambda x: list(map(int, x.split())), rule_str.split(' | ')))
    rules_arr[int(n_str)] = rule


def is_match(rules, n, message):
    rule = rules[n]
    if isinstance(rule, str):
        return [1] if len(message) > 0 and message[0] == rule else []

    match_lengths = list()
    for path in rule:
        q = list()
        q.append((0, 0))
        while len(q) > 0:
            path_index, length = q.pop()
            if path_index == len(path):
                match_lengths.append(length)
                continue

            i = path[path_index]
            curr_lengths = is_match(rules, i, message[length:])
            if not curr_lengths:
                continue
            for l in curr_lengths:
                q.append((path_index + 1, length + l))

    return match_lengths


valid_messages = 0
for message in messages:
    match_lengths = is_match(rules_arr, 0, message)
    if any(l == len(message) for l in match_lengths):
        valid_messages += 1

print(valid_messages)
