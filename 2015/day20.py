inp = 34000000
limit = inp // 10

h1 = [0] * (limit + 1)

for elf in range(1, limit):
    for house in range(elf, limit, elf):
        h1[house] += elf * 10

p1 = next(i for i, presents in enumerate(h1) if presents >= inp)
print(p1)

h2 = [0] * (limit + 1)

for elf in range(1, limit):
    for house in range(elf, min(elf * 50, limit), elf):
        h2[house] += elf * 11

p2 = next(i for i, presents in enumerate(h2) if presents >= inp)
print(p2)
