def rasilB(Frase):
    sTRL = list(Frase)
    x = sTRL[0]
    sTRL.remove(sTRL[0])
    sTRL.append(x)
    Frase = "".join(sTRL)
    return Frase

x = str(input("Digite uma frase: "))
y = list(map(str, x.split()))

for i in range(len(y)):
    print(rasilB(y[i]))