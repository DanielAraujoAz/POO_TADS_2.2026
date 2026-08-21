def MMC(x, y):
    if x <= y:
        for i in range(0,10001):
            if ((x+i) % x == 0) and ((x+i) % y == 0):
                return x+i
    if x > y:
        for i in range(0,10001):
            if ((y+i) % y == 0) and ((y+i) % x == 0):
                return y+i
            
x, y = map(int, input().split())
print(MMC(x, y))