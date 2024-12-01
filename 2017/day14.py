from functools import reduce

def knot_hash(s: str) -> str:
    nums = list(range(256))
    pos = skip = 0
    
    lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]
    
    for _ in range(64):
        for l in lengths:
            idx = [i % 256 for i in range(pos, pos + l)]
            for i, v in zip(idx, reversed([nums[i] for i in idx])):
                nums[i] = v
            pos = (pos + l + skip) % 256
            skip += 1
    
    dense = [reduce(lambda x,y: x^y, nums[i:i+16]) for i in range(0, 256, 16)]
    return ''.join(f'{x:02x}' for x in dense)

key = "jzgqcdpd"

grid=[]
for i in range(128):
    hsh = knot_hash(f"{key}-{i}")
    row = ''.join([f"{int(hsh[i:i+1],16):08b}" for i, c in enumerate(hsh[::1])])
    grid.append(row)

# part 1
print(sum([row.count("1") for row in grid]))


moves = [(1,0),(0,1)(-1,0),(0,-1)] #D R L U
for x, row in enumerate(grid):
    for y, square in enumerate(row):
        if square == "1":
            [tuple(map(sum, zip((x,y), i)) for i in moves]
        

