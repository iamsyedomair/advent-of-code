import re

inp = open('inp.txt').read().strip()

pattern = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

nums = re.findall(pattern, inp)
p1 = p2 = 0

flag = True
for n in nums:
    if "don't" in n:
        flag = False
        continue

    if "do" in n:
        flag = True
        continue

    if flag: 
        a,b = map(int, n[4:-1].split(','))
        p2 += a * b
    p1 += a * b

print(p1, p2)
