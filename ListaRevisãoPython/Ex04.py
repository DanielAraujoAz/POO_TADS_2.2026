x = input("insira uma data no formato dd/mm/aaaa: ")

def validação_data(x):
    data_invalida=0
    if len(x) > 10:
        data_invalida = 1
        return data_invalida
    elif (x[2] != "/") or (x[5] != "/"):
        data_invalida = 1
        return data_invalida

    dia = int((x[0]+x[1]))
    mes = int((x[3]+x[4]))
    ano = int(x[6]+x[7]+x[8]+x[9])

    if (ano < 0) or (ano > 10000):
        data_invalida=1
        return data_invalida
    elif (mes > 12) or (mes < 1):
        data_invalida=1
        return data_invalida
    elif (dia < 1) or (dia > 31):
        data_invalida=1
        return data_invalida
    elif (mes == 2) and (dia > 29):
        data_invalida=1
        return data_invalida
    elif mes == 2 and (ano % 400 != 0):
        data_invalida = 1
        return data_invalida
    elif ((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)) and (dia > 30):
        data_invalida=1
        return data_invalida

if validação_data(x) == 1:
    print("A data informada não é valida")
else:
    print("A data informada é valida")