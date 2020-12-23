input_string = '''389125467'''


class Cup:
    value = 0
    next = None

    def __init__(self, i):
        self.value = i


init_cup = curr_cup = Cup(int(input_string[0]))

cup_dict = dict()
cup_dict[init_cup.value] = init_cup

for c in input_string[1:]:
    curr_cup.next = Cup(int(c))
    curr_cup = curr_cup.next
    cup_dict[curr_cup.value] = curr_cup

for i in range(10, 1000001):
    curr_cup.next = Cup(int(i))
    curr_cup = curr_cup.next
    cup_dict[i] = curr_cup

curr_cup.next = init_cup
curr_cup = init_cup

print('finished building circular linked list')

for r in range(10000000):
    next_cup = curr_cup.next
    next_in_circle = next_cup.next.next.next
    curr_cup.next = next_in_circle

    unavailable_numbers = {next_cup.value, next_cup.next.value, next_cup.next.next.value}

    min_value = 1
    while min_value in unavailable_numbers:
        min_value += 1

    max_value = 1000000
    while max_value in unavailable_numbers:
        max_value -= 1

    i = curr_cup.value - 1
    while True:
        if i < min_value:
            i = max_value
            break
        if i in unavailable_numbers:
            i -= 1
            continue
        break

    dest_cup = cup_dict[i]

    next_cup.next.next.next = dest_cup.next
    dest_cup.next = next_cup

    curr_cup = curr_cup.next

    if (r + 1) % 500000 == 0:
        print('finished round', r + 1)

print(cup_dict[1].next.value * cup_dict[1].next.next.value)
