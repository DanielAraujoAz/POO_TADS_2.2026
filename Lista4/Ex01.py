class musica:
    def __init__(self, titulo, artista, album):
        self.__titulo = self.set_titulo(titulo)
        self.__artista = self.set_artista(artista)
        self.__album = self.set_album(album)

    def set_titulo(self, titulo):
        if titulo != None: self.__titulo = titulo
        else: raise ValueError("titulo não devê ser nulo")
    def set_artista(self, artista):
        if artista != None: self.__artista = artista
        else: raise ValueError("artita não devê ser nulo")
    def set_album(self, album):
        if album != None: self.__album = album
        else: raise ValueError("album não devê ser nulo")

    def get_titulo(self):
        return self.__titulo
    def get_artista(self):
            return self.__artista
    def get_album(self):
            return self.__album

    def __str__(self):
         return f"Titulo ={self.__titulo} | Artista = {self.__artista} | Album = {self.__album}"

class playlist:
    def __init__(self, nome, descrição):
        self.__musicas = [""]
        self.__descrição = self.set_descrição(descrição)
        self.__nome = self.set_nome(nome)

    def set_nome(self, nome):
        if nome != None: self.__nome = nome
        else: raise ValueError("nome não devê ser nulo")
    def set_descrição(self, descrição):
        if descrição != None: self.__descrição = descrição

    def get_nome(self):
        return self.__nome
    def get_descrição(self):
        return self.__descrição

    def inserir(self, titulo, artista, album):
        self.__musicas.append(musica(titulo, artista, album))
    def listar(self):
        return self.__musicas

    def __str__(self):
        return len(self.__musicas)