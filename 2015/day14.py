import re

inp = open('day14.txt').read().splitlines()
reindeers = [tuple(map(int, re.findall("\d+", i))) for i in inp]

def f(speed, duration, rest, time):
    dist=0
    while(time>0):
        if duration <= time:
            dist += duration*speed
        else:
            dist += min(duration,time)*speed
        time -= duration + rest
    return dist

t = 2503

print(max([f(a,b,c,t) for a,b,c in reindeers]))

scores = [0]*len(inp)

for t in range(1,t):
    distances = [f(a,b,c,t) for a,b,c in reindeers]
    indexes = [i for i,x in enumerate(distances) if x == max(distances)]
    for i in indexes:
        scores[i] += 1

print(max(scores))
