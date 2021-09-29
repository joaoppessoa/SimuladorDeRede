from Dispositivo import *


class Computador(Dispositivo):

	def __init__(self, nome: str, ip: str, mac: str):
		super().__init__(nome, ip, mac)
