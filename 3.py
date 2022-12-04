# read input lines
with open('3_input.txt', 'r') as f:
    input: list[str] = f.read().splitlines()

def get_priority(letter: str) -> int:
    if letter.isupper():
        return ord(letter) - 38
    elif letter.islower():
        return ord(letter) - 96

def common_char(strlist: list[str]) -> str:
    return ''.join(set.intersection(*map(set, strlist)))

total_priority: int = 0
badge_priority: int = 0
for i, rs in enumerate(input):
    # part 1
    c0, c1 = rs[:len(rs)//2], rs[len(rs)//2:]
    total_priority += get_priority(common_char([c0, c1]))

    # part 2
    if i%3 == 2:
        badge_priority += get_priority(common_char(input[i-2:i+1]))

print('break')