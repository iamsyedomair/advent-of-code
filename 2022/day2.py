with open('day2.txt') as f:
    inp = f.read().strip().split('\n')

wins = ["AY", "BZ", "CX"]
x = "ABC"
y = "XYZ"
score_1 = score_2 = 0

for i in inp:
    move = ''.join(i.split())
    s = move[-1]
    m = x.index(move[0])

    score_1 += y.index(s) + 1

    if move in wins:
        score_1 += 6
    elif m == y.index(s):
        score_1 += 3

    score_2 += 3 * y.index(s) 

    if s == "X": # win 
        score_2 += (m - 1) % 3 + 1
    elif s == "Y": # draw
        score_2 += m + 1 
    elif s == "Z": # lose
        score_2 += (m + 1) % 3 + 1

print(score_1, score_2)
