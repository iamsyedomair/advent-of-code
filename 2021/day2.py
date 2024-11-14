ops_1 = {'forward': lambda x,y,d: (x+d,y), 'up': lambda x,y,d:(x,y+d), 'down': lambda x,y,d:(x,y-d)}
ops_2 = {'forward': lambda x,y,z,d: (x+d,y+(z*d),z), 'up': lambda x,y,z,d:(x,y,z-d), 'down': lambda x,y,z,d:(x,y,z+d)}

x = d = a = 0
for line in open('day2.txt'):
    op, unit = line.split()
    #x, d = ops_1[op](x,d,int(unit)) # uncomment for part 1
    x, d, a = ops_2[op](x,d,a,int(unit))

print(x*d)
