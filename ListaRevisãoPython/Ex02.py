#2. Ler o número do mês (1 – janeiro; 2 – fevereiro; ...; 12 – dezembro) e identificar o nome do mês e em que trimestre
#o mês está incluído.



mes = int(input())
meses = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
if (mes > 0) and (mes < 4):
    trimestre = "primeiro"
elif (mes > 3) and (mes < 7):
    trimestre = "segundo"
elif (mes > 6) and (mes < 10):
    trimestre = "terceiro"
elif (mes > 9) and (mes < 13):
    trimestre = "quarto"
print("O mes de",meses[mes-1],"é do",trimestre,"trimestre do ano")