inp = open("day8.txt").read().strip().splitlines()

decode = lambda s: s.encode('ascii').decode('unicode_escape')
encode = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

p1 = sum(len(i) - len(decode(i)[1:-1]) for i in inp)
p2 = sum(len(encode(i)) - len(i) for i in inp)

print(p1,p2)

