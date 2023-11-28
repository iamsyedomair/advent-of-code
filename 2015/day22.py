import re
from itertools import product

boss = {'hp': 58, 'damage': 9}
player = {'hp': 50, 'mana': 500}

# cost, damage, armor, mana, turns
spells = ((53,4,0,0,0),
          (73,2,2,0,0), 
          (113,0,7,0,6), 
          (173,3,0,0,6),
          (229,0,0,101,5))


