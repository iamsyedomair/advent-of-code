
with open('./day1.txt', 'r') as f:
    inp = f.read()

"""
for i in inp:
    if i == '(':
        floor = floor + 1
    elif i == ')':
        floor = floor - 1
"""

floor = 0
num_instruction = 0
for i in inp:
    if i == '(':
        floor = floor + 1
    elif i == ')':
        floor = floor - 1

    num_instruction = num_instruction + 1


    if floor < 0:
        break
    


print(floor)
print(num_instruction)
