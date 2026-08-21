n = int(input())

def Primo(n):
    divs = []
    x=0
    for i in range(0,n):
        x=x+1
        if n % x == 0:
            divs.append(x)

    if divs == [1, n]:
        return "Primo"
    else:
        return("Não primo")

print(Primo(n))