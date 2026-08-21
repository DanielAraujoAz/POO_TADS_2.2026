x = str(input("Digite uma frase: "))
y = list(map(str, x.split()))

def remontar_string(lista):
    string_remontada = ""
    for i in range(len(lista)):
        string_remontada = string_remontada + " " + lista[i]
    return string_remontada

print(x)
for i in range(1,len(y)):
    y.remove(y[0])
    print(remontar_string(y))