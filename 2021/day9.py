def f(img):
    if len(img) == 0: return -1
    if not all([len(img[i]) == len(img[i+1]) for i in range(len(img)-1)]): return -1
    if not all([all([0<=c<=255 for c in row]) for row in img]): return -1
    
    return sum([sum(row) for row in img]) / len(img)**2

print(f([[100,200], [50,150]]))
