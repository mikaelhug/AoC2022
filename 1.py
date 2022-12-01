# read input (remove last new line)
with open('1_input.txt', 'r') as f:
    elves = f.read()[:-1].split('\n\n')

# number, calories
top_elf = [0, 0]
all_totals = []
for i, elf in enumerate(elves):
    elf_cal = [int(x) for x in elf.split('\n')]
    total_cal = sum(elf_cal)
    all_totals.append(total_cal)

    if total_cal > top_elf[1]:
        top_elf = [i, total_cal]

result = 'Maximum calories is: %s, and its carried by elf: %s' % (top_elf[1], top_elf[0])
print(result)

all_totals.sort(reverse=True)
print(sum(all_totals[0:3]))

print("break")