def removerEspaços(texto):
    texto = "".join(map(str, texto.split()))
    return texto

x = input()
print(removerEspaços(x))