# read input lines
with open('2_input.txt', 'r') as f:
    input: list[str] = f.read().splitlines()

shape_score: dict[str, int] = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

idx: dict[str, int] = {
    'A': 0, # rock
    'B': 1, # paper
    'C': 2, # scissor
    'X': 0, # rock
    'Y': 1, # paper
    'Z': 2 # scissor
}

# RPS (opp) / RPS (me)
scores: list[list[int]] = [
    [3,6,0],
    [0,3,6],
    [6,0,3]
]

# RPS (opp) / LDW (me)
ldw: list[list[str]] = [
    ['Z', 'X', 'Y'],
    ['X', 'Y', 'Z'],
    ['Y', 'Z', 'X']
]

score_1: int = 0
score_2: int = 0
for round in input: 
    # part 1
    opp, me = round.split()
    score_1 += shape_score[me]
    score_1 += scores[idx[opp]][idx[me]]

    # part 2
    me2 = ldw[idx[opp]][idx[me]]
    score_2 += shape_score[me2]
    score_2 += scores[idx[opp]][idx[me2]]

print('following the strategy guide I received the following score: %s' % score_1)
print('following the elf I received the following score: %s' % score_2)
print('break')