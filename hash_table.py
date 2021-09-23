def is_prime(num: int) -> bool:
    num = abs(num)
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    if num < 2:
        return False
    return True

def max_prime(num: int) -> int:
    for i in range(num, 1, -1):
        if is_prime(i):
            return i
    return 2


class Entry:
    
    def __init__(self, key: object, value: object):
        self.key = key
        self.value = value


class HashTable:
    
    def __init__(self, length: int):
        self.__length = length
        self.__table: list['Entry'] = [None] * length
        
    def hashing(self, key: object) -> int:
        return hash(key) % self.__length
        
    def hashing2(self, key: object) -> int:
        prime = max_prime(self.length)
        return prime - (hash(key) % prime)
        
    def re_hashing(self, key: object, i: int = 1):
        return (self.hashing(key) + i * self.hashing2(key)) % self.__length
    
    def insert(self, key: object, value: object):
        index = self.hashing(key)
        
        # TODO modularizar o while abaixo em um método de tratamento de colisão
        i = 1
        while self.__table[index] is not None:
            assert i < self.__length, 'Tabela cheia!'
            index = self.re_hashing(key, i)
            i += 1
            
        self.__table[index] = Entry(key, value)
            
        
    def get(self, key: object) -> object:
        index = self.hashing(key)
        assert self.__table[index] is not None, 'Nenhuma entrada correspondente!'
        
        # TODO modularizar o while abaixo em um método de tratamento de colisão
        i = 1
        while self.__table[index].key != key:
            assert i < self.__length, 'Nenhuma entrada correspondente!'
            index = re_hashing(key, i)
            i += 1
            
        return self.__table[index].value
        
    def print_entries(self):
        for k, v in enumerate(self.__table):
            if v:
                print(k, v.key, v.value)
        
        
if __name__ == '__main__':
    
    # Teste
    ports = HashTable(24)
    
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
            print('-->',mac)
            port = ports.get(mac)
            print(f'O MAC {mac} está na porta {port}')
        elif opcao == '3':
            ports.print_entries()
        else:
            break
        
