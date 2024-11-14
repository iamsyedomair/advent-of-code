with open('day1.txt') as f:
    inp = [int(i) for i in f.read().strip().split('\n')]

print(sum([1 for i in range(1, len(inp)) if inp[i-1] < inp[i]]))

p_2 = 0
for i in range(1, len(inp) - 2):
    if inp[i-1]+inp[i]+inp[i+1] < inp[i]+inp[i+1]+inp[i+2]:
        p_2 += 1

print(p_2)
