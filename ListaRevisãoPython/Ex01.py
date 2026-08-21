#1. Ler quatro números inteiros, calcular a soma dos números pares e a soma dos números ímpares.


pares = []
impares = []
for i in range(0,4):
    x = int(input())
    if x%2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print(sum(pares))
print(sum(impares))