import datetime

class Treino:
    def __init__(self):
        self.__id = None
        self.__data = None
        self.__distancia =  None
        self.__tempo = None
    def set_id(self, x):
        if x == None:
            raise ValueError("id não possue valor")
        self.__id = x
    def set_data(self,x):
        self.__data = x
    def set_distancia(self,x):
        if x <= 0:
            raise ValueError("distancia não positiva")
        self.__distancia = x
    def set_tempo(self, x):
        self.__tempo = x

    def get_id(self):
        return self.__id
    def get_data(self):
        return self.__data
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo

    def pace(self):
        minutos = (self.__tempo.seconds/60)
        return minutos/self.__distancia

    def __str__(self):
        return f"id = {self.__id} | data = {self.__data} | distancia = {self.__distancia} | tempo = {self.__tempo}"

class TreinoUI:
    __treinos = []
    def main(self):
        __rep = 1
        while __rep != 0:
            try:
                __rep = self.menu()
                if __rep == 1:
                    self.inserir()
                elif __rep == 2:
                    self.listar()
                elif __rep == 3:
                    self.listar_id()
                elif __rep == 4:
                    self.atualizar()
                elif __rep == 5:
                    self.excluir()
                elif __rep == 6:
                    self.MaisRapido()
                elif __rep > 6:
                    raise ValueError("Operação Invalida")
            except ValueError as erro:
                print(f"Erro: {erro}")   
    def menu(self):
        return int(input("0 = fim | 1 = inserir | 2 = listar | 3 = procurar id | 4 = Atualizar | 5 = Excluir | 6 = Menor pace: "))
    def inserir(self):
        print('Inserir')
        t = Treino()        
        id = input("insira o id do treino: ")
        i = 0
        if len(self.__treinos) > 0:
            for i in range(0,len(self.__treinos)):
                if id == self.__treinos[i].get_id():
                    raise ValueError("id ja aplicado a outro treino")
        t.set_id(id)
        t.set_data(datetime.datetime.today())
        t.set_distancia(int(input("insira a distancia percorida no treino em KM: ")))
        t.set_tempo(datetime.timedelta(minutes=int(input("insira quantos minutos durou o treino: "))))
        self.__treinos.append(t)
    def listar(self):
        i = 0
        if len(self.__treinos) > 0:
            print(len(self.__treinos))
            for i in range(0,len(self.__treinos)):
                print(self.__treinos[i])
    def listar_id(self):
        i = 0
        id_procurado = input("insira o id do treino: ")
        for i in range(0,len(self.__treinos)):
            if self.__treinos[i].get_id() == id_procurado:
                print(self.__treinos[i])
                break
            if len(self.__treinos) == i:
                print(f"treino com id={id_procurado} não encontrado")
    def atualizar(self):
        i = 0
        x = None
        id_procurado = input("insira o id do treino: ")
        for i in range(0,len(self.__treinos)):
            if self.__treinos[i].get_id() == id_procurado:
                print(self.__treinos[i])
                x = i
                break
            if len(self.__treinos) == i:
                print(f"treino com id={id_procurado} não encontrado")
        if x != None:
            self.__treinos[x].set_distancia(int(input("insira a distancia percorida no treino em KM: ")))
            self.__treinos[x].set_tempo(datetime.timedelta(minutes=int(input("insira quantos minutos durou o treino: "))))
    def excluir(self):
        i = 0
        x = None
        id_procurado = input("insira o id do treino: ")
        for i in range(0,len(self.__treinos)):
            if self.__treinos[i].get_id() == id_procurado:
                x = i
                break
            if len(self.__treinos) == i:
                print(f"treino com id={id_procurado} não encontrado")
        if x != None:
            del self.__treinos[x]
            
    def MaisRapido(self):
        i = 0
        MaisRapido = None
        x = None
        for i in range(0,len(self.__treinos)):
            if MaisRapido == None:
                MaisRapido = self.__treinos[i].pace()
                x = i
            elif self.__treinos[i].pace() < MaisRapido:
                MaisRapido = self.__treinos[i].pace()
                x = i
        print(self.__treinos[x])

        
x = TreinoUI()
x.main()    
