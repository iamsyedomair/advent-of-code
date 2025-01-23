import re
from collections import Counter

inp = open('inp.txt').read().strip().split('\n')
pattern = '(\S+)\[(\w+)\]'
ans = 0

for i in inp:
    name, check = re.match(pattern, i).groups()
    name = name.split('-')
    name, ID = ''.join(name[:-1]), int(name[-1]) 
    lst = sorted(list(Counter(name).items()), key=lambda x:(-x[1], x[0]))[:5] 
    if check == ''.join(i[0] for i in lst):
        ans += ID 

print(ans)

for i in inp:
    name, check = re.match(pattern, i).groups()
    if check == ''.join(i[0] for i in sorted(Counter(''.join(name.split('-')[:-1])).items(), key=lambda x:(-x[1],x[0]))[:5]):
        d = ''.join(' ' if c=='-' else chr((ord(c)-97+int(name.split('-')[-1]))%26+97) for c in '-'.join(name.split('-')[:-1]))
        if 'north' in d: 
            print(int(name.split('-')[-1]))
