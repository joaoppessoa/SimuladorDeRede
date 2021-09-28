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


class Grafo:

	def __init__(self):
		self.__vertices: list['Vertice'] = []
		self.__arestas: list['Aresta'] = []

	def AdicionarVertice(self, dado: object) -> 'Vertice':
		pass

	def AdicionarAresta(self, origem: 'Vertice', destino: 'Vertice') -> 'Aresta':
		pass
