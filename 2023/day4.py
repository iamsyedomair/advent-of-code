with open('day4.txt') as f:
    inp = f.read().strip().split('\n')

l = []
wins = []

d = dict() 
    
check = lambda win, mine: sum([1 for w in win if w in mine])
for i in inp:
    card, numbers = i.split(': ')
    card = int(card.split()[-1])
    winners, mine = numbers.split(' | ')
    winners = tuple(map(int, winners.split()))
    mine = tuple(map(int, mine.split()))
    d[card] = [winners, mine]
    value = check(winners, mine)
    if value == 0:
        pass
    else:
        l.append(2 ** (value - 1)) 

copies = {c:0 for c in d}

for card in d:
    winners, mine = d[card][0], d[card][1]
    value = check(winners, mine)
    copies[card] += 1

    cs = ([card + i for i in range(1, value + 1) if card + i in d] )

    for _ in range(copies[card]):
        for c in cs:
            if c in copies:
                copies[c] += 1

print(sum(l))
print(sum(copies.values()))
