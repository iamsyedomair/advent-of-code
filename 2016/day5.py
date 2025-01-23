import hashlib
p1,p2,i="",["_"]*8,0
d="reyedfim"
while "_" in p2 or len(p1)<8:
    h=hashlib.md5((d+str(i)).encode()).hexdigest()
    if h.startswith("00000"):
        if len(p1)<8:p1+=h[5]
        pos=int(h[5],16)
        if pos<8 and p2[pos]=="_":p2[pos]=h[6]
    i+=1
print(p1, ''.join(p2))
