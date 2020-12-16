input_string = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''

rules_str, your_ticket_str, nearby_tickets_str = input_string.split('\n\n')

rules = list()

for rule in rules_str.split('\n'):
    range_strs = rule.split(': ')[1].split(' ')[::2]
    for range_str in range_strs:
        range_spl = list(map(int, range_str.split('-')))
        rules.append((range_spl[0], range_spl[1]))

error_rate = 0

for ticket in map(lambda t: map(int, t.split(',')), nearby_tickets_str.split('\n')[1:]):
    for value in ticket:
        found_rule = False
        for low, high in rules:
            if low <= value <= high:
                found_rule = True
                break

        if not found_rule:
            error_rate += value

print(error_rate)
