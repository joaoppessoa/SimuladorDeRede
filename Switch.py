from Dispositivo import *
from hash_table import HashTable


class Switch(Dispositivo):
    def __init__(self, nome: str, ip: str, mac: str, portas: int):
        assert portas == 4 or portas == 8 or portas == 16 or portas == 24

        super().__init__(nome, ip, mac)
        self.__portas = portas
        self.__enderecos = HashTable(portas)

    @property
    def portas(self):
        return self.__portas
    
    @portas.setter
    def portas(self, portas: int):
        self.__portas = portas

## OK
    def addMac(self, mac, porta):
        if not Dispositivo.MAC_valido(mac):
            raise MacInvalidoException('MAC inválido!')
        self.__enderecos.insert(mac, porta)

    ##OK

    def buscar(self, mac: object):
        return self.__enderecos.get(mac)

   # def adicionarDispositivo(self, porta: int, mac:str):
       # dispositivo = HashTable(self.__portas)
       # dispositivo.insert(mac, porta)
       # self.__enderecos.append(dispositivo)
##OK
    def exibirTabelaMac(self):
        self.__enderecos.print_entries()

    def haPortasEmUso(self):
        return self.__enderecos.haEntradasOcupadas()
    
    def returnEnderecos(self):
        return self.__enderecos

    def __str__(self):
        return f''' {super().__str__()}, Nº Portas: {self.portas} '''
