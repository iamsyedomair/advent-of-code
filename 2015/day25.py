def get_next(r,c):
    if r == 1:
        return c+1,1

    return r-1,c+1

code = 20151125
r,c = 1,1
while (r,c) != (2947, 3029):
    code = (code * 252533) % 33554393 
    r,c = get_next(r,c)

print(get_next(1,1))
print(code)
