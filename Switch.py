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

    def adicionarDispositivo(self, porta: int, mac:str):
        dispositivo = {'porta': porta, 'mac': mac}
        self.__enderecos.append(dispositivo)

    def exibirTabela(self):
        for i in range(len(self.__enderecos)):
            print(self.__enderecos[i])

    def haPortasEmUso(self):
        if len(self.__enderecos) > 0:
            return True
        
        return False
    
    def returnEnderecos(self):
        return self.__enderecos

    def __str__(self):
        return f''' {super().__str__()}, Nº Portas: {self.portas} '''