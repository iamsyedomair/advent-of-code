from itertools import product

inp = open('inp.txt').read().strip().split('\n')
inp = [i.split(": ") for i in inp]
inp = {int(a): tuple(map(int, b.split(' '))) for a,b in inp}

total = 0
for target in inp:
    values = inp[target]
    found = False
    ops = ['+', '*', '||']
    for combo in product(ops, repeat=len(values)-1):
        curr_value = values[0]
        for i, (op, next_val) in enumerate(zip(combo, values[1:])):
            if op == '+':
                curr_value += next_val
            elif op == '*':
                curr_value *= next_val
            else:  # ||
                curr_value = int(str(curr_value) + str(next_val))
        
        if curr_value == target:
            found = True
            break
    
    if found:
        total += target

print(total)
