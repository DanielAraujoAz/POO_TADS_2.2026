import datetime

class musica:
    def __init__(self, x, y, z, h, u):
        self.__id = x
        self.__titulo = y
        self.__artista = z
        self.__album = h
        self.__duracao = u    
    def set_id(self, x):
        self.__id = x
    def set_titulo(self, x):
        self.__titulo = x
    def set_artista(self, x):
        self.__artista = x
    def set_album(self, x):
        self.__album = x
    def set_duracao(self, x):
        self.__duracao = x

    def get_id(self):
        return self.__id
    def get_titulo(self):
        return self.__titulo
    def get_artista(self):
        return self.__artista 
    def get_album(self):
        return self.__album
    def get_duracao(self):
        return self.__duracao

    def __str__(self):
        return f"id = {self.__id} | titulo = {self.__titulo} | artista = {self.__artista} | album = {self.__album} | duracao = {self.__duracao}"

class playlist:
    def __init__(self, x, y, z):
        self.__id = x
        self.__nome = y
        self.__descricao = z

    def set_id(self, x):
        self.__id = x
    def set_nome(self, x):
        self.__nome = x
    def set_descicao(self, x):
        self.__descricao = x

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_descicao(self):
        return self.__descricao

    def tempo_total(self):
        tempo_total = 0
        if len(x.playlistitens) > 0:    
            for i in range(0,len(x.playlistitens)):
                if x.playlistitens[i].get_id_playlist() == self.__id:
                    for j in range(0,len(x.musicas)):
                        if x.playlistitens[i].get_id_musica() == x.musicas[j].get_id():
                            tempo_total = tempo_total + x.musicas[j].get_duracao().seconds            
        else:
            return "nenhuma musica na playlist"
        return tempo_total

    def __str__(self):
        return f"id = {self.__id} | nome = {self.__nome} | descricao = {self.__descricao}"

class PlayListItem:
    def __init__(self, a, b, c, d, e):
        self.__id = a
        self.__id_playlist = b
        self.__id_musica = c
        self.__datainclusao = d
        self.__sequencia = e

    def set_id(self, x):
        self.__id = x
    def set_id_playlist(self, x):
        self.__id_playlist = x
    def set_id_musica(self, x):
        self.__id_musica = x
    def set_datainclusao(self, x):
        self.__datainclusao = x
    def set_sequencia(self, x):
        self.__sequencia = x

    def get_id(self):
        return self.__id
    def get_id_playlist(self):
        return self.__id_playlist
    def get_id_musica(self):
        return self.__id_musica
    def get_datainclusao(self):
        return self.__datainclusao
    def get_sequencia(self):
        return self.__sequencia

    def __str__(self):
        return f"{self.__id} | {self.__id_playlist} | {self.__id_musica} | {self.__datainclusao} | {self.__sequencia}"

class UI:
    musicas = []
    playlists = []
    playlistitens = []
    def main(self):
        __rep = 1
        while __rep != 0:
            __rep = self.menu()
            if __rep == 1:
                self.criar_musica()
            elif __rep == 2:
                self.criar_playlist()
            elif __rep == 3:
                self.criar_playlistitem()
            elif __rep == 4:
                self.tempo_total_playlist()
    def menu(self):
        return int(input("0 = fim | 1 = criar musica | 2 = criar playlist | 3 = inserir musica | 4 = verificar tempo total de playlist: "))

    def criar_musica(self):
        __id = int(input("insira o id da musica: "))
        __titulo = input("insira o titulo da musica: ")
        __artista = input("insira o criador da musica: ")
        __album = input("insira o album da musica: ")
        __duracao = datetime.timedelta(minutes = int(input("insira a quantidade de minutos na musica: ")), seconds = int(input("insira a quantidade de segundos na musica: ")))
        x = musica(__id,__titulo,__artista,__album,__duracao)
        print(x)
        self.musicas.append(x)

    def criar_playlist(self):
        __id = int(input("insira o id da playlist: "))
        __nome = input("insira o nome da playlist: ")
        __descricao = input("insira a descricao da playlist:")
        x = playlist(__id,__nome,__descricao)
        print(x)
        self.playlists.append(x)
        print(self.playlists[0].get_id())

    def criar_playlistitem(self):
        __id = int(input("insira o id do playlistitem: "))
        __id_playlist = int(input("insira o id da playlist em que quer inserir a musica: "))
        __id_musica = int(input("insira o id da musica a ser inserida: "))
        __datainclusao = datetime.datetime.today()
        __sequencia = input("insira a sequencia da musica na playlist: ")
        x = PlayListItem(__id,__id_playlist,__id_musica,__datainclusao,__sequencia)
        print(x)
        self.playlistitens.append(x)
        

    def tempo_total_playlist(self):
        tt = 0
        horas = 0
        minutos = 0
        __id_playlist = int(input("insira o id da playlist: "))
        index_playlist = None
        for j in range(0,len(self.playlists)):
            if self.playlists[j].get_id() == __id_playlist:
                index_playlist = j
        for i in range(0,len(self.playlistitens)):
            if self.playlistitens[i].get_id_playlist() == __id_playlist:
                tt = self.playlists[index_playlist].tempo_total()
                print(tt)
        if tt > 3600:
            horas = tt // 3600
            tt = tt % 3600
        if tt > 60:
            minutos = tt // 60
            tt = tt % 60
        print(f" duração total = {datetime.timedelta(hours = horas, minutes = minutos, seconds= tt)}")
            
    def __str__(self):
        return f"{self.musicas} | {self.playlists} | {self.playlistitens}"

x = UI() 
x.main()
