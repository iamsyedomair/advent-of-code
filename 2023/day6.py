import re
import math

inp = """
Time:        35696887
Distance:   213116810861248
""".split('\n')[1:-1]

_, lst = inp[0].split(':') 
time = list(map(int, re.findall('\d+', lst)))

_, lst = inp[1].split(':') 
distance = list(map(int, re.findall('\d+', lst)))

wins = [0] * len(time)

race = 0
for d, t in zip(distance, time):
    for i in range(t):
        distance = i * (t - i)
        if distance > d:
            wins[race] += 1
    race += 1


print(math.prod(wins))
