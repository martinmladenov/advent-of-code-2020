input_string = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''

rules_str, your_ticket_str, nearby_tickets_str = input_string.split('\n\n')

rules = list()

for rule in rules_str.split('\n'):
    rule_name, rule_range_strs = rule.split(': ')
    range_strs = rule_range_strs.split(' ')[::2]
    rule_ranges = list()
    for range_str in range_strs:
        range_spl = list(map(int, range_str.split('-')))
        rule_ranges.append((range_spl[0], range_spl[1]))
    rules.append((rule_name, rule_ranges))

# print(rules)

tickets = list(map(lambda t: list(map(int, t.split(','))), nearby_tickets_str.split('\n')[1:]))

valid = list()

for ticket in tickets:
    invalid = False
    for value in ticket:
        found_rule = False
        for rule, ranges in rules:
            for low, high in ranges:
                if low <= value <= high:
                    found_rule = True
                    break
            if found_rule:
                break

        if not found_rule:
            invalid = True
            break
    if not invalid:
        valid.append(ticket)

# print(list(tickets))
# print(list(valid))

departure_rules = list(filter(lambda r: r[0].startswith('departure '), rules))

# print(departure_rules)

possibilities = list()

for rule, ranges in rules:
    rule_possibilities = list()
    for i in range(len(valid[0])):
        found = True
        for t in valid:
            value = t[i]
            found_range = False
            for low, high in ranges:
                if low <= value <= high:
                    found_range = True
                    break
            if not found_range:
                found = False
                break

        if found:
            rule_possibilities.append(i)
    possibilities.append((rule, rule_possibilities))

possibilities.sort(key=lambda x: len(x[1]))

# print(possibilities)

unavailable_indices = set()
fields = list()

for rule, rule_possibilities in possibilities:
    for index in rule_possibilities:
        if index not in unavailable_indices:
            unavailable_indices.add(index)
            fields.append((rule, index))
            break

# print(fields)

your_ticket = list(map(int, your_ticket_str.split('\n')[1].split(',')))

prod = 1

for field, index in fields:
    print(field, your_ticket[index])
    if field.startswith('departure '):
        prod *= your_ticket[index]

print(prod)
