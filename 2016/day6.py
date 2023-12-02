from collections import Counter

with open ('./day6.txt') as f:
    inp = f.read().split()

inp = [''.join([row[i] for row in inp]) for i in range(len(inp[0]))]
print(''.join([max(Counter(s), key=lambda x: Counter(s)[x]) for s in inp]))
print(''.join([min(Counter(s), key=lambda x: Counter(s)[x]) for s in inp]))
