"""
written by:         omair syed @ 11:13 pm nov 30 2024
live streamed by:   kashish tandon via discord
"""
inp = [tuple(map(int, i.split('   '))) for i in open("inp.txt").read().strip().split('\n')]
l1, l2 = sorted(x[0] for x in inp), sorted(x[1] for x in inp)
print(sum(abs(a - b) for a, b in zip(l1, l2)), sum(a * l2.count(a) for a in l1))
