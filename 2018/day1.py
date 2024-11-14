with open('day1.txt') as f:
    inp = f.read().strip().split('\n')

print(sum([int(i) for i in inp]))

freq = 0
freqs = {freq}
found = False
while not found:
    for i in inp:
        freq += int(i)
     
        if freq in freqs:
            found = True
            break
        freqs.add(freq)

print(freq)
