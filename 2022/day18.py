droplets = [tuple(map(int, i.split(','))) for i in open('inp.txt').read().strip().split('\n')]
s = set(droplets)

diff = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

total = 0
for drop in droplets:
    ns = [tuple(map(sum,zip(drop, i))) for i in diff]
    total += 6 - sum([1 for n in ns if n in s])
    
print(total)


"""
breadth first search version
    start anywhere
    look around
    if you find a droplet, return its faces + faces of the adj found recursively  
    else faces += 1

    return faces 
"""



