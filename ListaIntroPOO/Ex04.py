# 1 = domingo, 2 = segundo, 3 = terça, 4 = quarta, 5 = quinta, 6 = sexta, 7 = sabado

class entrada_cinema:
    def __init__(self):
        self.dia = 0
        self.h = 0
        self.valor = 0
    def calcValor(self):
        if self.dia == 4:
            self.valor = 8
        elif (self.dia == 2) or (self.dia == 3) or (self.dia == 5):
            self.valor = 16
            if (self.h >= 17) and (self.h <= 24):
                self.valor = 24
        elif (self.dia == 6) or (self.dia == 7) or (self.dia == 1):
            self.valor = 20
            if (self.h >= 17) and (self.h <= 24):
                self.valor = 30
        return self.valor

x = entrada_cinema()
x.dia = int(input("insira o dia do filme (1 = domingo, 2 = segundo, 3 = terça, 4 = quarta, 5 = quinta, 6 = sexta, 7 = sabado): "))
x.hora = int(input("insira a hora do filme no formato de 24horas e sem o h: "))

print(x.calcValor())
