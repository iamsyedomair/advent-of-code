inp = open('day12.txt').read().strip().split('\n')
d = {j: set(k.split(', ')) for j, k in (line.split(' <-> ') for line in inp)}

def visit(start):
    stack = [start]
    visited = set()
    while stack:
        s = stack.pop()
        if s not in visited:
            visited.add(s)
            stack.extend(d[s] - visited)
    return visited

visited = visit("0")
print(len(visited))

groups = 1
for program in d:
    if program not in visited:
        visited |= visit(program)
        groups += 1

print(groups)
