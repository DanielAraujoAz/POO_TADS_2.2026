def MenorInteiro(x):
    y = int(x)
    if y < x:
        y = y+1
    return y

y = float(input())
print(MenorInteiro(y))