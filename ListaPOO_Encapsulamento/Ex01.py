class circulo:
    def __init__(self):
        self.__r = 0
    def set_raio(self, z):
        if z <= 0:
            raise ValueError("Numero não positivo")
        else:
            self.__r = z
    def get_raio(self):
        return self.__r
    def area_circulo(self):
        return self.__r * 2*3.14
    def diametro_circ(self):
        return self.__r*2

x = circulo()
y = 999

while y != 0:
    y = int(input("insira um valor, 0 = sair, 1 = get_r, 2 = set_r, 3 = area_circ, 4 = dia_circ: "))
    if y == 1:
        print("valor atual do raio",x.get_raio())
    elif y == 2:
        x.set_raio(int(input()))
    elif y == 3:
        print("Area do circulo",x.area_circulo())
    elif y == 4:
        print("Diametro do circulo",x.diametro_circ())