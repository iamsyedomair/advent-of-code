with open('day1.txt') as f:
    inp = [int(i) for i in f.read().strip().split()]

def find():
    p1 = p2 = 0
    for i in range(len(inp)):
        for j in range(i+1, len(inp)):
            x,y=inp[i],inp[j]
            if x + y == 2020:
                p1 = x*y
            for k in range(j+1, len(inp)):
                z=inp[k]
                if x + y + z == 2020:
                    p2 = x*y*z
                    return (p1, p2)

print(find())
