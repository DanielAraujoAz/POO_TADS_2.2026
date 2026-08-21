def Diagonal(b, h):
    import math
    d2 = (b*b) + (h*h)
    d = math.sqrt(d2)
    return d

b, h = map(int, input().split())
print(Diagonal(b, h))