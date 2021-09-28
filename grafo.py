class Vertice:

	def __init__(self, dado: object):
		self.__dado = dado
		self.__adjs: list['Aresta'] = []

	@property
	def dado(self):
		return self.__dado

	@dado.setter
	def dado(self, valor: object):
		self.__dado = valor

	@property
	def adjs(self):
		return self.__adjs

	def adicionarAdj(self, adj: 'Aresta'):
		self.adjs.append(adj)

	def __str__(self):
		return str(self.__dado)


class Aresta:

	def __init__(self, origem: 'Vertice', destino: 'Vertice'):
		self.__origem = origem
		self.__destino = destino

	@property
	def origem(self):
		return self.__origem

	@property
	def destino(self):
		return self.__destino

	@origem.setter
	def origem(self, origem):
		self.__origem = origem

	@destino.setter
	def destino(self, destino):
		self.__destino = destino

	def __str__(self):
		return f'{self.__origem} -------- {self.__destino}'


from hash_table import *


class Grafo:

	def __init__(self):
		self.__vertices: list['Vertice'] = []
		self.__arestas: list['Aresta'] = []

	def adicionarVertice(self, dado: object) -> 'Vertice':
		vertice = Vertice(dado)
		self.__vertices.append(vertice)
		return vertice

	def adicionarAresta(self, origem: 'Vertice', destino: 'Vertice') -> 'Aresta':
		aresta = Aresta(origem, destino)
		origem.adjs.append(aresta)
		self.__arestas.append(aresta)
		return aresta

	def buscar(self, chave: object, origem: 'Vertice') -> 'Vertice':
		# Busca BFS (Breadth-First Search)
		# Marcar todos os vértices como não visitado (verts.value = False)
		verts = HashTable(self.qtdVertices())
		for v in self.__vertices:
			verts.insert(v, False)

		# Marcar vertice de origem como visitado
		verts.insert(origem, True)

		# Busca
		fila = [origem]
		while fila:
			v = fila.pop(0)
			for w in v.adjs:
				w = w.destino
				if not verts.get(w):
					# processe w
					print('-->', w)
					# -- #
					verts.insert(w, True)
					fila.append(w)

	def qtdVertices(self):
		return len(self.__vertices)

	def qtdArestas(self):
		return len(self.__arestas)

	def __str__(self):
		grafo_str = ''
		for v in self.__vertices:
			grafo_str += f'{v.dado} --> '
			for a in v.adjs:
				grafo_str += str(a.destino.dado)
			grafo_str += '\n'

		return grafo_str


if __name__ == '__main__':

	rede = Grafo()

	pc1 = rede.adicionarVertice(['PC1', '192.168.1.10', 'ab:cd:ef:12:34:00'])
	pc2 = rede.adicionarVertice(['PC2', '192.168.1.11', 'ab:cd:ef:12:34:01'])
	pc3 = rede.adicionarVertice(['PC3', '192.168.1.12', 'ab:cd:ef:12:34:02'])
	pc4 = rede.adicionarVertice(['PC4', '192.168.1.13', 'ab:cd:ef:12:34:03'])
	sw1 = rede.adicionarVertice(['SW1', '192.168.1.14', '00:ff:aa:bb:cc:dd'])

	rede.adicionarAresta(pc1, sw1)
	rede.adicionarAresta(pc2, sw1)
	rede.adicionarAresta(pc3, sw1)
	rede.adicionarAresta(pc4, sw1)

	rede.buscar('', pc1)
