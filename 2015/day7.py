with open('./day7.txt', 'r') as f:
    inp = [tuple(i.split(' ')) for i in f.read().strip().split('\n')]

wires = {i[-1]: i[:-2] for i in inp}

def solve(wires, wire):
    ins = wires[wire]

    if isinstance(ins, int): return ins

    if len(ins) == 1: 
        try:
            c = int(ins[-1])
        except:
            c = solve(wires, ins[-1])

    if len(ins) == 2: c = ~solve(wires, ins[1])
    if len(ins) == 3: 
        a,b = ins[0], ins[2]
        a = int(a) if a.isdigit() else solve(wires, a) 
        b = int(b) if b.isdigit() else solve(wires, b) 

        if ins[1] == "RSHIFT": c = a >> b 
        if ins[1] == "LSHIFT": c = a << b
        if ins[1] == "AND": c = a & b
        if ins[1] == "OR": c = a | b

    wires[wire] = c
    return wires[wire]

p1 = solve(wires, "a")

wires = {i[-1]: i[:-2] for i in inp}
wires["b"] = p1
p2 = solve(wires, "a")

print(p1, p2)
