from pprint import pprint as pp
from itertools import permutations 

with open('day2.txt') as f:
    inp = [tuple(map(int, i.split('\t'))) for i in f.read().strip().split('\n')]
            
print(sum([max(row) - min(row) for row in inp]))
print(sum([[max(p) // min(p) for p in permutations(row,2) if max(p) % min(p) == 0][0] for row in inp]))
