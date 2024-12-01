droplets = [tuple(map(int, i.split(','))) for i in open('day18.txt').read().strip().split('\n')]

start = droplets[0]

"""
breadth first search version
    start anywhere
    look around
    if you find a droplet, return its faces + faces of the adj found recursively  
    else faces += 1

    return faces 
"""

print(droplets)
