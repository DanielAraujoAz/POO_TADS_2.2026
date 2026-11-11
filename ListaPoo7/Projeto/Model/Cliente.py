class Cliente():
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
    
    def set_id(self, x):
        self.__id = x
    def set_nome(self, x):
        self.__nome = x
    def set_email(self, x):
        self.__email = x
    def set_fone(self, x):
        self.__fone =  x

    def __str__(self):
        return f"{self.__id}|{self.__nome}|{self.__email}|{self.__fone}"