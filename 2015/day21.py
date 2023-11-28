import re
from itertools import product

# Item Name | cost | damage | armor

weapons = """
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
"""

armor = """
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
"""

rings = """
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""

en_stats = {'hp': 103, 'damage': 9, 'armor' : 2}
p_stats = {'hp': 100}

pat = re.compile("\s(\d+)\s+(\d+)\s+(\d+)")

find = lambda data: [tuple(map(int, i)) for i in re.findall(pat, data)] 
w, a, r = tuple(map(find, [weapons, armor, rings]))

a.append((0,0,0))

r.append((0,0,0))
r = [(i,j) for i,j in product(r, r) if (i != j)]
r.append(((0,0,0),(0,0,0)))

def fight(e_stats, p_stats) -> bool:
    """simulate the fight that takes the enemy and player stats"""
    p_damage, e_damage = p_stats['damage'] - e_stats['armor'], e_stats['damage'] - p_stats['armor']
    p_health, e_health = p_stats['hp'], e_stats['hp'] 

    while p_health > 0:
        e_health -= p_damage
        if(e_health < 0):
            return True
        p_health -= e_damage
    return False
    

cost = lambda p : p[0][0] + p[1][0] + p[2][0][0] + p[2][1][0]
damage = lambda p : p[0][1] + p[2][0][1] + p[2][1][1]
armor = lambda p : p[1][2] + p[2][0][2] + p[2][1][2]

possibilities = sorted(product(w, a, r), key = cost)

for p in possibilities:
    p_stats['damage'] = damage(p)
    p_stats['armor'] = armor(p)

    if fight(en_stats, p_stats) == True:
        print(cost(p))
        break

for p in possibilities[::-1]:
    p_stats['damage'] = damage(p)
    p_stats['armor'] = armor(p)

    if not fight(en_stats, p_stats) == True:
        print(cost(p))
        break
