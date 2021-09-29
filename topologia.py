from Computador import Computador
from grafo import *
from Switch import Switch

# Equipamentos da rede
# ---> Computadores
c1 = Computador('C1', '192.168.0.12', '77:87:01:0C:1E:A6')
c2 = Computador('C2', '192.168.0.11', '01:7F:6C:29:3A:31')
c3 = Computador('C3', '192.168.0.10', '41:12:96:A0:E2:7E')
c4 = Computador('C4', '10.0.0.10', 'E8:51:28:27:93:92')
c5 = Computador('C5', '10.0.0.11', 'A3:38:6A:69:21:E9')
c6 = Computador('C6', '10.0.0.12', '68:FC:A5:88:DD:9F')
c7 = Computador('C7', '192.168.1.12', '5B:6E:F0:09:33:19')
c8 = Computador('C8', '192.168.1.11', 'E7:30:81:9E:99:A3')
c9 = Computador('C9', '192.168.1.10', '13:84:69:E4:01:59')
# ---> Switches
s1 = Switch('S1', '192.168.10.10', '38:A4:65:A6:61:5C', 4)
s2 = Switch('S2', '192.168.10.11', '38:A4:65:A6:61:A7', 16)
s3 = Switch('S3', '192.168.10.12', '38:A4:65:A6:61:10', 8)


# Topologia da rede
rede = Grafo()

c1 = rede.adicionarVertice(c1)
c2 = rede.adicionarVertice(c2)
c3 = rede.adicionarVertice(c3)
c4 = rede.adicionarVertice(c4)
c5 = rede.adicionarVertice(c5)
c6 = rede.adicionarVertice(c6)
c7 = rede.adicionarVertice(c7)
c8 = rede.adicionarVertice(c8)
c9 = rede.adicionarVertice(c9)
s1 = rede.adicionarVertice(s1)
s2 = rede.adicionarVertice(s2)
s3 = rede.adicionarVertice(s3)

rede.adicionarAresta(c1, s1)
rede.adicionarAresta(c2, s1)
rede.adicionarAresta(c3, s1)
rede.adicionarAresta(s1, s2)
rede.adicionarAresta(c4, s2)
rede.adicionarAresta(c5, s2)
rede.adicionarAresta(c6, s2)
rede.adicionarAresta(s2, s3)
rede.adicionarAresta(c7, s3)
rede.adicionarAresta(c8, s3)
rede.adicionarAresta(c9, s3)


def ARP(origem: 'Vertice', ip: str):
	if ip == origem.dado.ip:
		return origem.dado.mac

	for v in rede.percorrer(origem):
		if v.dado.ip == ip:
			return v.dado.mac
