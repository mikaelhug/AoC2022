from copy import deepcopy

with open('5_input.txt', 'r') as f:
    input = f.read()

cr, inst = input.split('\n\n')

cr = cr.split('\n')
inst = inst.split('\n')[:-1]

crates1 = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
}


def move_crate(crates, cramnt, crfrom, crto, end=True):
    start = []
    for i in range(0, cramnt):
        crate = crates[crfrom].pop(-1)
        if end:
            crates[crto].append(crate)
        else:
            start.insert(0, crate)

    if not end:
        crates[crto].extend(start)


# populate crates
for crline in cr[:-1]:
    for i in range(0, 9):
        crate = crline[1+4*i:2+4*i]
        if crate != ' ':
            crates1[i+1].insert(0, crate)


# make copy for part 2
crates2 = deepcopy(crates1)
for ist in inst:
    ist = ist.split(' ')
    cramnt, crfrom, crto = int(ist[1]), int(ist[3]), int(ist[5])
    move_crate(crates1, cramnt, crfrom, crto)
    move_crate(crates2, cramnt, crfrom, crto, end=False)

# result
result1 = ''
result2 = ''
for i in range(0, 9):
    result1 += crates1[i+1][-1]
    result2 += crates2[i+1][-1]

print(result1)
print(result2)

print("break")