class viagem:
    def __init__(self):
        self.km = 0
        self.h = 0
    def velocidade_media(self):
        return self.km / self.h

x = viagem()
x.km = int(input())
x.h = int(input())

print(x)
print(x.velocidade_media())