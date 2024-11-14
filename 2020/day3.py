with open('day3.txt') as f:
    inp = f.read().strip().split()

a = len(inp[0])
b = len(inp)
s = min(a,b)

coords = [(3*i,1*i) for i in range(s)]
print(sum([inp[x][y] == "#" for x,y in coords]))
