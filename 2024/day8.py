from collections import defaultdict
from itertools import combinations

inp = open('inp.txt').read().strip().split()
nodes = defaultdict(list)
antinodes = set()

for r, row in enumerate(inp):
    for c, node in enumerate(row):
        if node != ".":
            nodes[node].append((r,c))

num_rows, num_cols = len(inp), len(inp[0])

def is_collinear(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (y2-y1) * (x3-x1) == (y3-y1) * (x2-x1)

for freq in nodes:
    if len(nodes[freq]) < 2:
        continue
    for i in range(num_rows):
        for j in range(num_cols):
            point = (i,j)
            collinear_count = 0
            for a, b in combinations(nodes[freq], 2):
                if is_collinear(a, b, point):
                    antinodes.add(point)
                    break

print(len(antinodes))
