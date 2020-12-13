input_string = '''abc

a
b
c

ab
ac

a
a
a
a

b'''

groups = input_string.split('\n\n')

total = 0

for group in groups:
    people = group.split('\n')
    yes = set(iter(people[0]))
    for person in people[1:]:
        yes.intersection_update(set(iter(person)))
    print(yes)
    total += len(yes)

print(total)
