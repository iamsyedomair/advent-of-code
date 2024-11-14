with open('day4.txt') as f:
    inp = [i.split(',') for i in f.read().strip().split()]

p1 = p2 = 0
for i in inp:
    x1,y1 = map(int, i[0].split('-'))
    x2,y2 = map(int, i[1].split('-'))
    s1 = range(x1,y1+1)
    s2 = range(x2,y2+1)

    if all([i in s1 for i in s2]) or all([i in s2 for i in s1]):
        p1 += 1

    if any([i in s1 for i in s2]) or any([i in s2 for i in s1]):
        p2 += 1

print(p1, p2)
