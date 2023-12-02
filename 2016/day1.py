with open ('./day1.txt') as f:
    inp = f.read().split(', ')

inp = "R2, L3".split(', ')
rot = lambda lst, k: lst[-k:] + lst[:-k]    

x, y = 0, 0
f = "U"

RL = {f: rot([(1,0),(-1,0)],i) for i, f in enumerate(list("UD"))}
UD = {f: rot([(0,1),(0,-1)],i) for i, f in enumerate(list("RL"))}

for i in inp:
    d, val = i[0], int(i[1:])
    move = RL[f] if f in "UD" else UD[f]

    dx, dy = move["RL".index(d)]
    x, y = x + dx, y + dy
    if f == "U":
        f = d
    elif f == "R":


print(x, y)
