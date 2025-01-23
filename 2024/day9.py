from collections import OrderedDict

#inp = open('inp.txt').read().strip()
inp = "12345"

block_num = 0
l = []

d = dict()
for i in range(0, len(inp) - 1, 2):
    block_size, free_space = int(inp[i]), int(inp[i+1])
    d[block_num] = (block_size, free_space)
    block_num += 1

d[block_num] = (int(inp[-1]), 0)


print(len(inp))
print(d)
