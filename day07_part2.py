import re
import queue

input_string = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''

rules = input_string.split('\n')

children = dict()

pattern = re.compile(r'(?:\d+ )?\w+ \w+ bag')

for rule in rules:
    matches = pattern.findall(rule)
    parent = matches[0]
    if parent not in children:
        children[parent] = list()
    for child in matches[1:]:
        if child == 'no other bag':
            break
        separator = child.index(' ')
        children[parent].append((child[separator + 1:], int(child[:separator])))

total_bags = 0

stack = queue.LifoQueue()

stack.put(('shiny gold bag', 1))

while not stack.empty():
    bag, num = stack.get()
    total_bags += num
    for child, child_num in children[bag]:
        stack.put((child, child_num * num))

print(total_bags - 1)
