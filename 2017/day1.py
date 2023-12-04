with open('day1.txt') as f:
    inp = f.read().strip()

l1,l2 = [], []
inp2 = inp*2
check = lambda i1, i2: inp2[i1] == inp2[i2]

for i, d in enumerate(inp):
    if check(i, i+1):
        l1.append(d)
    if check(i, i+len(inp)//2):
        l2.append(d)

print(sum(list(map(int, l1))), sum(list(map(int, l2))))
