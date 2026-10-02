class Viagem:
    def __init__(self,destino, distancia,litros):
        self.__destino = destino
        self.__distancia = distancia
        self.__litros = litros
    def set_distancia(self, z):
        if z > 0:
            self.__distancia = z
        else:
            raise ValueError("Numero não positivo")
    def set_litros(self, z):
        if z > 0:
            self.__litros = z
        else:
            raise ValueError("Numero não positivo")
    def set_destino(self, z):
        self. __destino = z
    def get_distancia(self):
        return self.__distancia
    def get_litros(self):
        return self.__litros
    def get_destino(self):
        return self.__destino
    def Consumo(self):
        return f"{self.__distancia / self.__litros}L/km"
    def __str__(self):
        return f"Destino = {self.__destino} | Distancia = {self.__distancia}km/h | Litros = {self.__litros}L"

class ViagemUI:
    def main():
        x = 0
        while x != 2:
            x = ViagemUI.menu()
            if x == 1:
                ViagemUI.Calculo()
    def menu():
        return int(input("1 = Calcular, 2 = Fim: "))
    def Calculo():
        destino = input("insira o destino: ")
        distancia = int(input("insira a distancia ao destino: "))
        litros = int(input("insira o combustivel consumido na viagem: "))
        x = Viagem(destino, distancia, litros)
        print(x)
        print(x.Consumo())

ViagemUI.main()