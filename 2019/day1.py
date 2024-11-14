with open('day1.txt') as f:
    inp = [int(i) for i in f.read().strip().split('\n')]

p1 = sum([i//3 - 2 for i in inp])
p2 = 0
for i in inp:
    while(True):
        i //= 3
        i -= 2
        if i <= 0:
            break
        else:
            p2 += i

print(p1,p2)
