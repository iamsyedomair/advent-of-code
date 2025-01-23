droplets = [tuple(map(int, i.split(','))) for i in open('inp.txt').read().strip().split('\n')]
s = set(droplets)

diff = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

total = 0
for drop in droplets:
    ns = [tuple(map(sum,zip(drop, d))) for d in diff]
    total += 6 - sum([1 for n in ns if n in s])
    
for drop in droplets:
    for d1 in diff:
        tmp_drop = tuple(map(sum, zip(drop, d1)))

            
    print(drop)

print(s)
print(total)

