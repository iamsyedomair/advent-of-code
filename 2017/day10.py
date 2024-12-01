from functools import reduce

def knot(lens, rounds=1):
    nums = list(range(256))
    pos = skip = 0
    for _ in range(rounds):
        for l in lens:
            idx = [i % 256 for i in range(pos, pos + l)]
            for i, v in zip(idx, [nums[i] for i in idx][::-1]):
                nums[i] = v
            pos = (pos + l + skip) % 256
            skip += 1
    return nums

# Part 1
lengths = [102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216]
result = knot(lengths)
print(result[0] * result[1])

# Part 2
s = "102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216"
lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]
sparse = knot(lengths, 64)
dense = [reduce(lambda x,y: x^y, sparse[i:i+16]) for i in range(0, 256, 16)]
print(''.join(f'{x:02x}' for x in dense))
