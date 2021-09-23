from Dispositivo import Dispositivo

class Switch(Dispositivo):
    def __init__(self, nome: str, ip: str, mac: str, portas: int):
        super().__init__(nome, ip, mac)
        self.__portas = portas
        self.__enderecos  = []

    @property
    def portas(self):
        return self.__portas
    
    @portas.setter
    def portas(self, portas: int):
       self.__portas = portas

    def addEndereco(self, endereco):
        self.__enderecos.append(endereco)

    def buscar(self):
        pass