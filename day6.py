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
    yes = set()
    for person in group.split('\n'):
        for question in person:
            yes.add(question)
    print(yes)
    total += len(yes)

print(total)
