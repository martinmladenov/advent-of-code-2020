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


def calc_score(player):
    score = 0
    for i in range(len(player)):
        c = player.pop()
        player.appendleft(c)
        score += c * (i + 1)
        i += 1
    return score


def play(player1, player2):
    previous_rounds = set()

    while len(player1) > 0 and len(player2) > 0:
        curr_round = (calc_score(player1), calc_score(player2))

        if curr_round in previous_rounds:
            return 1

        previous_rounds.add(curr_round)

        p1 = player1.popleft()
        p2 = player2.popleft()

        if len(player1) >= p1 and len(player2) >= p2:
            p1sub = deque()
            p2sub = deque()
            for i in range(p1):
                p1sub.append(player1[i])
            for i in range(p2):
                p2sub.append(player2[i])
            w = play(p1sub, p2sub)
            winner = player1 if w == 1 else player2
        else:
            winner = player1 if p1 > p2 else player2

        if winner == player1:
            winner.append(p1)
            winner.append(p2)
        else:
            winner.append(p2)
            winner.append(p1)

    return 1 if len(player1) > 0 else 2


play(player1, player2)
winner = player2 if len(player1) == 0 else player1

print(calc_score(winner))
