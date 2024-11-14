import re

inp = open('day19.txt').read().splitlines()
target_molecule = inp[-1]
replacements = [line.split(" => ") for line in inp[:-3]]

unique_molecules = set()
for a, b in replacements:
    for match in re.finditer(a, target_molecule):
        start = match.start()
        unique_molecules.add(target_molecule[:start] + b + target_molecule[start + len(a):])

print(len(unique_molecules))

reversed_replacements = sorted([(b, a) for a, b in replacements], key=lambda x: -len(x[0]))
steps = 0
while target_molecule != 'e':
    for product, replacement in reversed_replacements:
        if product in target_molecule:
            target_molecule = target_molecule.replace(product, replacement, 1)
            steps += 1
            break

print(steps)
