from Computador import Computador
from grafo import *


dispositivos = []
rede = Grafo()


def carregar_topologia(pcs, switches):
	global dispositivos

	dispositivos = [
		rede.adicionarVertice(switches[0]),  # SW1
		rede.adicionarVertice(pcs[0]),  # C1
		rede.adicionarVertice(pcs[1]),  # C2
		rede.adicionarVertice(pcs[2]),  # C3
		rede.adicionarVertice(switches[1]),  # SW2
		rede.adicionarVertice(pcs[3]),  # C4
		rede.adicionarVertice(pcs[4]),  # C5
		rede.adicionarVertice(pcs[5]),  # C6
		rede.adicionarVertice(switches[2]),  # SW3
		rede.adicionarVertice(pcs[6]),  # C7
		rede.adicionarVertice(pcs[7]),  # C8
		rede.adicionarVertice(pcs[8]),  # C9
	]

	try:
		rede.adicionarAresta(dispositivos[1], dispositivos[0])
		rede.adicionarAresta(dispositivos[2], dispositivos[0])
		rede.adicionarAresta(dispositivos[3], dispositivos[0])
		rede.adicionarAresta(dispositivos[0], dispositivos[4])
		rede.adicionarAresta(dispositivos[5], dispositivos[4])
		rede.adicionarAresta(dispositivos[6], dispositivos[4])
		rede.adicionarAresta(dispositivos[7], dispositivos[4])
		rede.adicionarAresta(dispositivos[4], dispositivos[8])
		rede.adicionarAresta(dispositivos[9], dispositivos[8])
		rede.adicionarAresta(dispositivos[10], dispositivos[8])
		rede.adicionarAresta(dispositivos[11], dispositivos[8])

	except ConnectionNotPermitedException as cnpe:
		raise ConnectionNotPermitedException('A conexão entre computadores não é permitida!')

	return rede


def ARP(ip: str, origem: 'Vertice'):
	if ip == origem.dado.ip:
		return origem.dado.mac

	for v in rede.percorrer(origem):
		if v.dado.ip == ip:
			return v.dado.mac


def mostrar_topologia():
	for i, disp in enumerate(dispositivos):
		print(i, disp.dado)

