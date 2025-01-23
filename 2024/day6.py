inp = open('inp.txt').read().strip().split()
    
x,y = 0,0
found = False
for r in inp:
    x += 1 
    y = 0
    for c in r:
        if c == "^": found = True 
        if found: break 
        y += 1
    if found: break
        
d = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
        
direction = "^"
s = {(x, y)}
row, col = x, y

while True:
    delta = d[direction]
    next_row = row + delta[0]
    next_col = col + delta[1]
    
    if not (0 <= next_row < len(inp) and 0 <= next_col < len(inp[0])):
        break
        
    if inp[next_row][next_col] == "#":
        if direction == "^": direction = ">"
        elif direction == ">": direction = "v"
        elif direction == "v": direction = "<"
        elif direction == "<": direction = "^"
    else:
        row, col = next_row, next_col
        s.add((row, col))

print(len(s))
