with open('4_input.txt', 'r') as f:
    input: list[str] = f.read().splitlines()


def in_range(r0, r1, fully_contain=True) -> int:
    '''sorts such that range with lowest start is always r0
    in case of same start point check end point such that r0 is always
    largest range'''
    if r0[0] > r1[0]:  # check start -> always lowest
        r0, r1 = r1, r0
    elif r0[0] == r1[0]:  # if equal check end -> r0 always largest
        if r0[1] < r1[1]:
            r0, r1 = r1, r0

    if fully_contain:
        if r0[0] <= r1[0] and r0[1] >= r1[1]:
            return 1
    else:
        if r1[0] <= r0[1]:
            return 1

    return 0


def line_parse(line) -> list[int]:
    a, b = line.split(',')
    a0, a1 = a.split('-')
    b0, b1 = b.split('-')
    return [int(a0), int(a1)], [int(b0), int(b1)]


fully_contain: int = 0
partly_contain: int = 0
for rp in input:
    # part 1, fully contain
    r0, r1 = line_parse(rp)
    fully_contain += in_range(r0, r1)

    # part 2, partly contain
    partly_contain += in_range(r0, r1, fully_contain=False)


print('break')