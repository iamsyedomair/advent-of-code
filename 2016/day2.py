with open('day2.txt') as f:
    inp = f.read().strip().split('\n')

keypad1 = """
1 2 3
4 5 6
7 8 9
"""

keypad2 = """
    1    
  2 3 4  
5 6 7 8 9
  A B C  
    D    
"""

move = [(0,2), (0,-2),(1,0),(-1,0)]

def get_code(keypad, start):
    x, y = start
    keypad = [k for k in keypad.split('\n')][1:-1]
    code = []
    rows, cols = len(keypad), len(keypad[0])
    for inst in inp:
        for d in inst:
            dx, dy = tuple(sum(x) for x in zip((x,y),  move['RLDU'.index(d)]))
            if 0 <= dx < rows and 0 <= dy < cols and keypad[dx][dy] != ' ':
                x = dx
                y = dy
        code.append(keypad[x][y])
    return ''.join(code)


print(get_code(keypad1, (1,2)), get_code(keypad2, (2,0)))
