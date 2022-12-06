with open('6_input.txt', 'r') as f:
    input = f.read()

def all_unique(uq) -> bool:
    for i, j in enumerate(uq[:-1]):
        if j in uq[i+1:]:
            return False
    return True

def loop_str(input, chars):
    for i in range(0, len(input)):
        if all_unique(input[i:i+chars]):
            return i+chars

print(loop_str(input, 4))
print(loop_str(input, 14))

print('break')