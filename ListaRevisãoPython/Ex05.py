lista_valores = list(map(int, input("digite 3 valores inteiros: ").split()))
maior_valor = "null"
menor_valor = "null"

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

lista_valores.remove(maior_valor)
lista_valores.remove(menor_valor)

print(menor_valor,", ",lista_valores[0],", ",maior_valor,sep="")