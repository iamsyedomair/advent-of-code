import math

with open('day2.txt') as f:
    inp = f.read().strip().split('\n')

c = [12, 13, 14]
total_1, total_2 = 0, 0
for i in inp:
    mins = [-1,-1,-1]
    game, sets = i.split(': ')
    sets = sets.split('; ') 
    game = int(game.split(' ')[-1])
    f = False
    for s in sets:
        rgb = [0,0,0]
        ss = (s.split(', '))
        for t in ss:
            n, color = t.split(' ')
            i = ["red", "green", "blue"].index(color)
            rgb[i] = int(n)
            mins[i] = max(int(n), mins[i])

        f = any([x > y for x,y in zip(rgb, c)]) if not f else f

    total_1 += game if not f else 0
    x = math.prod(mins)
    total_2 += x


print(total_1)
print(total_2)
