class Viagem:
    def __init__(self):
        self.__distancia = 0
        self.__tempo = 0
    def set_distancia(self, z):
        if z > 0:
            self.__distancia = z
        else:
            raise ValueError("Numero não positivo")
    def set_tempo(self, z):
        if z > 0:
            self.__tempo = z
        else:
            raise ValueError("Numero não positivo")
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    def velocidade_media(self):
        return self.__distancia / self.__tempo

x = Viagem()
y = 999

while y != 0:
    y = int(input("insira um valor, 0 = sair, 1 = get_dist, 2 = get_temp, 3 = set_dist, 4 = set_temp, 5 = Vel_media: "))
    if y == 1:
        print("valor atual da distancia",x.get_distancia())
    elif y == 2:
        print("valor atual do tempo",x.get_tempo())
    elif y == 3:
        x.set_distancia(int(input()))
    elif y == 4:
        x.set_tempo(int(input()))
    elif y == 5:
        print("Velocidade media =",x.velocidade_media())