from collections import defaultdict

inp = [tuple(i.split(')')) for i in open('day6.txt').read().strip().split('\n')]
d = defaultdict(list)
for a,b in inp:
    d[a].append(b)

def f(n, depth=0):
    return depth + sum(f(i,depth+1) for i in d[n])

print(f('COM'))

orbits = {}
for a,b in inp:
    orbits[b] = a

# Get path to COM from any object
def path_to_com(obj):
    path = []
    while obj in orbits:
        obj = orbits[obj]
        path.append(obj)
    return path

# Get paths for YOU and SAN
you_path = path_to_com('YOU')
san_path = path_to_com('SAN')

# Find first common ancestor
for i, obj in enumerate(you_path):
    if obj in san_path:
        print(i + san_path.index(obj))
        break

