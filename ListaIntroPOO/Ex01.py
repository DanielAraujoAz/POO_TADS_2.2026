class circulo:
    def __init__(self):
        self.r = 0
    def area_circulo(self):
        return self.r * 2*3.14
    def diametro_circ(self):
        return self.r*2

x = circulo()
x.r = int(input())

print(x)
print(x.area_circulo())
print(x.diametro_circ())
