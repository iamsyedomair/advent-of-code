import math

inp = open('day8.txt').read().strip().split('\n')
directions = inp[0]

d = dict()
for i in inp[2:]:
    a, b = i.split(" = ")
    l, r = b.split(', ') 
    d[a] = l[1:], r[:-1]

def traverse(node,i):
    l,r = d[node]
    return l if directions[i%len(directions)] == "L" else r

def f(node,part=2):
    i = 0
    ret = traverse(node,i)
    if part == 1:
        while ret != "ZZZ":
            i += 1
            ret = traverse(ret,i)
    else:
        while not ret.endswith("Z"):
            i += 1
            ret = traverse(ret,i)

    return i+1

#part 1
print(f("AAA",1))

#part 2
starts = [f(n) for n in d.keys() if n.endswith("A")]
print(math.lcm(*starts))
