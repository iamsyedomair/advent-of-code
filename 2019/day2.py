from itertools import product

def run(program, noun=None, verb=None):
    p = program[:]
    if noun is not None: p[1] = noun
    if verb is not None: p[2] = verb
    i = 0
    while p[i] != 99:
        a, b, c = p[i+1:i+4]
        p[c] = p[a] + p[b] if p[i] == 1 else p[a] * p[b]
        i += 4
    return p[0]

prog = list(map(int, "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,10,31,35,2,6,35,39,1,39,13,43,1,43,9,47,2,47,10,51,1,5,51,55,1,55,10,59,2,59,6,63,2,6,63,67,1,5,67,71,2,9,71,75,1,75,6,79,1,6,79,83,2,83,9,87,2,87,13,91,1,10,91,95,1,95,13,99,2,13,99,103,1,103,10,107,2,107,10,111,1,111,9,115,1,115,2,119,1,9,119,0,99,2,0,14,0".split(',')))

print(run(prog, 12, 2))
for n, v in product(range(100), repeat=2):
    if run(prog, n, v) == 19690720:
        print(100 * n + v)
        break
