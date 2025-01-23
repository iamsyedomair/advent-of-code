import re
inp = open('inp.txt').read().strip().split()

tls = 0
ssl = 0

for ip in inp:
    sn = re.split(r'\[.*?\]', ip)  # Supernets
    hn = re.findall(r'\[(.*?)\]', ip)  # Hypernets
    
    sn_abba = any(re.search(r'(.)(?!\1)(.)\2\1', s) for s in sn)
    hn_abba = any(re.search(r'(.)(?!\1)(.)\2\1', h) for h in hn)
    if sn_abba and not hn_abba:
        tls += 1

    aba = [m[0] + m[1] + m[0] for s in sn for m in re.findall(r'(?=(.)(?!\1)(.)\1)', s)]
    if any(bab in h for h in hn for bab in aba):
        ssl += 1

print(tls)
print(ssl)
