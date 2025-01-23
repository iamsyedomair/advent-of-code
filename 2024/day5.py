from collections import defaultdict

s1, s2 = open('inp.txt').read().strip().split("\n\n")
s1 = [tuple(map(int, i.split('|'))) for i in s1.split()]
s2 = [tuple(map(int, j.split(','))) for j in s2.split()]

deps = defaultdict(set)
for before, after in s1:
    deps[after].add(before)

def is_valid(page1, page2):
    return page2 not in deps[page1]

part1 = sum(
    pages[len(pages)//2] 
    for pages in s2 
    if all(is_valid(pages[i], p) for i, p in enumerate(pages) for p in pages[i+1:])
)

part2 = sum(
    sorted(pages, key=lambda x: len(deps[x]))[len(pages)//2]
    for pages in s2 
    if not all(is_valid(pages[i], p) for i, p in enumerate(pages) for p in pages[i+1:])
)

print(part1, part2)
