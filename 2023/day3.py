from collections import defaultdict
import re

inp = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
inp = inp.strip().split('\n')

with open('day3.txt') as f:
    lines = f.read().strip().split('\n')
with open('day3.txt') as f:
    inp = f.read().strip().split('\n')

def neighbours(row, col, max_row, max_col):
    neighbors = [(r, c) for r in range(row-1, row+2) for c in range(col-1, col+2) if 0 <= r < max_row and 0 <= c < max_col and (r, c) != (row, col)]
    return neighbors

total = 0
for i, row in enumerate(inp):
    nums = re.findall("(\d+)", row)
    row += '.'
    if nums:
        for num in nums:
            f = False
            #print(num, row.index(num))
            start = row.index(num)

            l = len(num)
            num_idxs = [(i, start+k) for k in range(len(num))]
            for k in range(l):
                ns = neighbours(i, start+k, len(inp[0]), len(inp))
                for n in ns:
                    x,y = n
                    char = inp[x][y]
                    if char != '.' and n not in num_idxs:
                        #total += int(num)
                        f = True
            if f:
                total += int(num)

        #nums = list(map(int, nums))

    #print(nums)

#print(inp)
print(total)

p1 = 0
num_str = ''
for r,line in enumerate(lines):
    line+='.'
    for c,char in enumerate(line):
        if char.isdigit():
            num_str += char
        elif num_str:
            if any(lines[r1][c1] not in '.0123456789' for r1 in (range(max(0,r-1),min(len(lines),r+2)))
                   for c1 in range(max(0,c-1-len(num_str)),min(len(line)-1,c+1))):
                p1 += int(num_str)
            num_str = ''
print("Part 1:",p1)

dct = defaultdict(list)
num_str = ''
for r,line in enumerate(lines):
    line+='.'
    for c,char in enumerate(line):
        if char.isdigit():
            num_str += char
        elif num_str:
            for r1 in (range(max(0,r-1),min(len(lines),r+2))):
                for c1 in range(max(0,c-1-len(num_str)),min(len(line)-1,c+1)):
                    if lines[r1][c1] == '*':
                        dct[r1,c1].append(int(num_str))
            num_str = ''

p2=sum(ab[0]*ab[1] for ab in dct.values() if len(ab)==2)
print("Part 2:",p2)
