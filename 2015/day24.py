from itertools import combinations
from functools import reduce
import operator


with open('day24.txt', 'r') as f:
    weights = tuple(map(int, f.read().strip().split('\n')))

package_weight = sum(weights) // 4 

def has_sum(lst, sub):
    for y in range(1, len(lst)):
        for x in (z for z in combinations(lst, y) if sum(z) == package_weight):
            if sub == 2:
                return True
            elif sub < 3:
                return has_sum(list(set(lst) - set(x)), sub - 1)
            elif has_sum(list(set(lst) - set(x)), sub -1):
                return reduce(operator.mul, x, 1)

print(has_sum(weights, 4))
