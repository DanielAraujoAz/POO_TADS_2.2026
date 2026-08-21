n, h = map(int, input().split())

divsx = []
divsy = []
x=0
for i in range(0,n):
    x=x+1
    if n % x == 0:
        divsx.append(x)

y=0
for ir in range(0,h):
    y=y+1
    if h % y == 0:
        divsy.append(y)

MDc = "null"

for i in range(len(divsx)):
    for ir in range(len(divsy)):
        if divsx[i] == divsy[ir]:
            if (MDc == "null") or (MDc < divsx[i]):
                MDc = divsx[i]
    
print(MDc)
print(divsx, divsy)