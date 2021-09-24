from abc import ABC, abstractmethod

class Dispositivo(ABC):
    def __init__(self, nome: str, ip: str, mac: str):
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
    def portas(self, ip: str):
        self.__ip = portas
    
    @mac.setter
    def mac(self, mac: str):
        self.__mac = mac
    
    def __str__(self):
        return ("Nome: %s, IP: %s, MAC: %s"%(self.__nome,self.__ip,self.__mac))