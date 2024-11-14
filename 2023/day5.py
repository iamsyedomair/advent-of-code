from pprint import pprint as pp

inp = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

d = {}
seeds = list()
x = ""

for i in inp.split("\n"):
    if "seeds: " in i:
        _, seeds = i.split(': ')

    if i == '':
        continue
    if i.endswith(':'):
        x, _ = i.split(' ')
        d[x] = list()
    else:
        if x != "":
            d[x].append(list(map(int, i.split(' '))))

print(d)
1/0
d2 = dict()

for key in d:
    for entry in d[key]:
        dest = tuple(range(entry[0], entry[0] + entry[-1]))
        src = tuple(range(entry[1], entry[1] + entry[-1]))
        t = {i:j for i, j in zip(src, dest)}

        if key not in d2:
            d2[key] = {i:j for i, j in zip(src, dest)}
        else:
            d2[key].update({i:j for i, j in zip(src, dest)})
            
order = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]


seeds = list(map(int, seeds.split(' ')))

lst = []
for s in seeds:
    f = s
    for key in order:
        #print(key, d2[k])
        if f not in d2[key]:
            k = f
        else:
            k = d2[key][f]
        f = k
    lst.append(f)
    
print(min(lst))
