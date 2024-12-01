inp = [tuple(map(int, i.split('   '))) for i in open("inp.txt").read().strip().split('\n')]
f=lambda x:sorted(i[x] for i in inp)
l1,l2 = f(0), f(1)
print(sum(abs(a - b) for a, b in zip(l1, l2)), sum(a * l2.count(a) for a in l1))
