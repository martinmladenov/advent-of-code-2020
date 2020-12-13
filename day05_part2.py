from math import floor, ceil

input_string = '''FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL'''


def get_seat_id(seat):
    low = 0
    high = 127
    for i in range(7):
        if seat[i] == 'F':
            high = floor(high - (high - low) / 2)
        else:
            low = ceil(low + (high - low) / 2)

    row = low

    left = 0
    right = 7
    for i in range(7, 10):
        if seat[i] == 'L':
            right = floor(right - (right - left) / 2)
        else:
            left = ceil(left + (right - left) / 2)

    col = left

    seat_id = row * 8 + col

    # print(seat, 'row:', row, 'col:', col, 'id:', seat_id)

    return seat_id


all_seats = set(get_seat_id(x) for x in input_string.split('\n'))

i = min(all_seats)
while True:
    if i not in all_seats:
        break

    i += 1

print(i)
