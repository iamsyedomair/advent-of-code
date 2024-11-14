with open('day2.txt') as f:
    inp = [tuple(i.split()) for i in f.read().strip().split('\n')]

p1 = p2 = 0
#inp = [("1-3","a:","abcde")]

for i in inp:
    limits, c, p = i
    c = c[0]
    x,y = map(int, limits.split('-'))

    if (x <= p.count(c) <= y):
        p1 += 1

    if (bool(p[x-1] == c) ^ bool(p[y-1] == c)):
        p2 += 1

print(p1, p2)
