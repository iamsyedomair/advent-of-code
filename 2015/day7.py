import re
from pprint import pprint as pp

with open('./day7.txt', 'r') as f:
    inp = [tuple(i.split(' ')) for i in f.read().strip().split('\n')]

opcodes = ('AND', 'LSHIFT', 'NOT')

wires = dict()

"""
and = lambda x, y: x & y
or = lambda x, y: x | y
lshift = lambda x, y: x << y
rshift = lambda x, y: x >> y
not = lambda x: ~x

def process(inst):
    if(inst[1] == "AND"):
        return and(inst[0], inst[2])
    elif(inst[1] == "OR"):
        return or(inst[0], inst[2])
    elif(inst[1] == "LSHIFT"):
        return lshifr(inst[0], inst[2])
    elif(inst[1] == "RSHIFT"):
        return rshift(inst[0], inst[2])
"""

for i in inp:
    wires[i[-1]] = i[:-2]

pp(wires)
