from collections import deque

input_string = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''

player1 = deque()
player2 = deque()

player_cards = list(map(lambda p: p.split('\n')[1:], input_string.split('\n\n')))

for c in player_cards[0]:
    player1.append(int(c))
for c in player_cards[1]:
    player2.append(int(c))

while len(player1) > 0 and len(player2) > 0:
    p1 = player1.popleft()
    p2 = player2.popleft()

    if p1 > p2:
        player1.append(p1)
        player1.append(p2)
    else:
        player2.append(p2)
        player2.append(p1)

score = 0
i = 1
winner = player2 if len(player1) == 0 else player1
while len(winner) > 0:
    score += winner.pop() * i
    i += 1

print(score)
