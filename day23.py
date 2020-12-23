input_string = '''389125467'''


class Cup:
    value = 0
    next = None

    def __init__(self, i):
        self.value = i


init_cup = curr_cup = Cup(int(input_string[0]))
for c in input_string[1:]:
    curr_cup.next = Cup(int(c))
    curr_cup = curr_cup.next

curr_cup.next = init_cup
curr_cup = init_cup

for r in range(100):
    next_cup = curr_cup.next
    next_in_circle = next_cup.next.next.next

    min_value = next_in_circle.value
    max_cup = next_in_circle
    curr_iter_cup = next_in_circle
    while curr_iter_cup != next_cup:
        if curr_iter_cup.value < min_value:
            min_value = curr_iter_cup.value
        if curr_iter_cup.value > max_cup.value:
            max_cup = curr_iter_cup
        curr_iter_cup = curr_iter_cup.next

    curr_cup.next = next_in_circle

    i = curr_cup.value
    dest_cup = next_in_circle
    while True:
        if dest_cup == next_in_circle:
            dest_cup = next_in_circle
            i -= 1
            if i < min_value:
                dest_cup = max_cup
                break
        if dest_cup.value == i:
            break
        dest_cup = dest_cup.next

    next_cup.next.next.next = dest_cup.next
    dest_cup.next = next_cup

    curr_cup = curr_cup.next

curr_iter_cup = curr_cup
while curr_iter_cup.value != 1:
    curr_iter_cup = curr_iter_cup.next
values = list()
one_cup = curr_iter_cup
curr_iter_cup = curr_iter_cup.next
while curr_iter_cup != one_cup:
    values.append(str(curr_iter_cup.value))
    curr_iter_cup = curr_iter_cup.next
print(''.join(values))
