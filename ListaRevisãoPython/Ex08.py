def rasilB(Frase):
    sTRL = list(Frase)
    x = sTRL[0]
    sTRL.remove(sTRL[0])
    sTRL.append(x)
    Frase = "".join(sTRL)
    return Frase

string = str(input())

for i in range(len(string)):
    string = rasilB(string)
    print(string)