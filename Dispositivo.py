from abc import ABC, abstractmethod
from re import match


class MacInvalidoException(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class Dispositivo(ABC):

    def __init__(self, nome: str, ip: str, mac: str):

        if not Dispositivo.MAC_valido(mac):
            raise MacInvalidoException('MAC inválido')

        self.__nome = nome
        self.__ip   = ip
        self.__mac  = mac
    
    @property
    def nome(self):
        return self.__nome

    @property
    def ip(self):
        return self.__ip
    
    @property
    def mac(self):
        return self.__mac

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @ip.setter
    def ip(self, ip: str):
        self.__ip = ip
    
    @mac.setter
    def mac(self, mac: str):
        self.__mac = mac

    @staticmethod
    def MAC_valido(mac: str) -> bool:
        return match('^(([0-9a-f]{2}):){5}([0-9a-f]{2})$', mac.lower())
    
    def __str__(self):
        return ("Nome: %s, IP: %s, MAC: %s"%(self.__nome,self.__ip,self.__mac))
