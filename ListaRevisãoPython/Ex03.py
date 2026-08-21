#3. Ler 4 valores inteiros diferentes e realizar as seguintes operações: verificar se os valores são realmente diferentes
#e mostrar uma mensagem de erro, caso contrário; mostrar o maior valor lido; mostrar o menor valor lido e mostrar o
#resultado da soma entre o segundo maior valor e o segundo menor.

lista_valores = list(map(int, input("digite 4 valores inteiros: ").split()))
maior_valor = "null"
menor_valor = "null"
invalido = False


for ii in range(0,len(lista_valores)):
    x = lista_valores[ii]
    if maior_valor == "null":
        maior_valor = x
    elif x > maior_valor:
        maior_valor = x
    if menor_valor == "null":
        menor_valor = x
    elif x < menor_valor:
        menor_valor = x

for i in range(0,len(lista_valores)):
    for ir in range(i+1,4):
        if lista_valores[i] == lista_valores[ir]:
            invalido = True
            break
    if invalido == True:
        break

lista_valores.remove(maior_valor)
lista_valores.remove(menor_valor)

if invalido != True:
    print("Maior valor =",maior_valor)
    print("Menor valor =",menor_valor)
    print("Soma do segundo maior valor com o segundo menor =",sum(lista_valores))
else:
    print("Dois ou mais numeros iguais!")
