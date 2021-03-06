class FullTableException(Exception):

    def __init__(self, msg: str):
        super().__init__(msg)


class AbsentKeyException(Exception):

    def __init__(self, msg: str):
        super().__init__(msg)


class Entry:

    __slots__ = ('key', 'value')

    def __init__(self, key: object, value: object):
        self.key = key
        self.value = value

    def __str__(self):
        return f'({self.key} --> {self.value})'


class HashTable:
    
    def __init__(self, length: int):
        self.__length = length
        self.__table: list['Entry'] = [None] * length

    @property
    def length(self):
        return self.__length
        
    def __hashing(self, key: object) -> int:
        return hash(key) % self.__length
        
    def __re_hashing(self, key: object, i: int = 1):
        return (hash(key) + i) % self.length

    def insert(self, key: object, value: object):
        index = self.__hashing(key)
        # tratamento de colisão:
        #   se a posição encontrada estiver preenchida:
        #       recalcula a posição, exceto se a chave da entrada encontrada
        #       for igual a passada pelo parâmetro key, nesse caso, o valor é apenas atualizado
        i = 1
        while (self.__table[index] is not None) and (self.__table[index].key != key):
            if i > self.__length:
                raise FullTableException(f'A "{self.__class__.__name__}" já está cheia!')
            index = self.__re_hashing(key, i)
            i += 1
        
        self.__table[index] = Entry(key, value)

    def get(self, key: object) -> object:
        index = self.__hashing(key)
        if self.__table[index] is None:
            raise AbsentKeyException(
                f'Nenhuma entrada para a chave "{key}" foi encontrada em "{self.__class__.__name__}"!')

        i = 1
        while self.__table[index].key != key:
            if i > self.__length:
                raise AbsentKeyException(
                    f'Nenhuma entrada para a chave "{key}" foi encontrada em "{self.__class__.__name__}"!')
            index = self.__re_hashing(key, i)
            i += 1
            
        return self.__table[index].value
        
    def print_entries(self):
        for v in self.__table:
            if v:
                print(f'PORTA: {v.value}, MAC: {v.key}')

    def haEntradasOcupadas(self):
        return any(self.__table)

    def __iter__(self):
        for row in self.__table:
            if row:
                yield row.key, row.value


# ---------------------------------------- #
# Teste (Apenas para debugar a hash table):
# ---------------------------------------- #

if __name__ == '__main__':

    from random import randint

    ports = HashTable(24)
    for j in range(ports.length):
        mac = ':'.join([f'{hex(randint(0, 255))[2:]:0>2}' for k in range(6)])
        ports.insert(mac, randint(1, 24))
    
    while True:
        
        print('''1 --> Inserir MAC/Port
2 --> Pesquisar MAC/Port
3 --> print ports
''')
        
        opcao = input('opção --> ')
        
        if opcao == '1':
            mac, port = input('\nDigite o MAC e a porta. Ex.: [ff:ff:ff:ff:ff:ff 24] -->').split()
            ports.insert(mac, port)
        elif opcao == '2':
            mac = input('\nDigite um MAC --> ')
            print('-->', mac)
            port = ports.get(mac)
            print(f'O MAC {mac} está na porta {port}')
        elif opcao == '3':
            ports.print_entries()
        else:
            break
        
