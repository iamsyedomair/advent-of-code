with open('day1.txt') as f:
    inp = [sum(map(int, i.split('\n'))) for i in f.read().strip().split('\n\n')]

print(max(inp))
print(sum(sorted(inp, reverse=True)[:3]))
