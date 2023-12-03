with open('day3.txt') as f:
    inp = f.read().strip()

total_1,total_2 = 0,0
ts = list()
ctr = 0
for i in inp.split('\n'):
    t = tuple(map(int, i.split()))
    a,b,c = t
    if (a + b > c) and (a + c > b) and (b + c > a):
        total_1 += 1

    ts.append(t)
    if ctr == 2:
        for t in zip(ts[-1], ts[-2], ts[-3]):
            x, y, z = t
            if (x + y > z) and (x + z > y) and (y + z > x):
                total_2 += 1
        ctr = -1
    ctr += 1

print(total_1, total_2)
