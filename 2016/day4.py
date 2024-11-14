import re

with open('day4.txt') as f:
    inp = f.read().strip().split('\n')

inp = ["aaaaa-bbb-z-y-x-123[abxyz]"]
pattern = '(\S+)\[(\w+)\]'
real = []
for i in inp:
    name, checksum = re.match(pattern, i).groups()
    name = name.split('-')
    name, ID = ''.join(name[:-1]), name[-1]
    print(name, ID, checksum)
    max_len = float('inf') 
    idx = -1
    for char in checksum:
        pat = re.findall(f"({char}+)", name)
        if pat:
            pat = sorted(pat, key=lambda x:len(x))
            idx = name.find(pat[0])
            
            print(idx)
        break

    print(name, ID, checksum)
    break
