import csv
from Switch import Switch

def index():
    listaDeSwitch = []

    with open('banco.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        
        for row in csv_reader:
            switch = Switch(row[0], row[1], row[2], int(row[3]))

            if row[4]:
                tabelaMac = row[4].split(',')

                for enderecos in tabelaMac:
                    enderecoArray = enderecos.split('-')

                    switch.adicionarDispositivo(enderecoArray[0], enderecoArray[1])

            listaDeSwitch.append(switch)
    
    return listaDeSwitch

def salvar(lista: list):
    with open('banco.csv', 'w', newline='') as csv_file:
        arquivo = csv.writer(csv_file, delimiter=';')

        for switch in lista:
            if switch.haPortasEmUso():
                tabelaArp = switch.returnEnderecos()

                enderecos = str(tabelaArp[0]['porta'])+'-'+tabelaArp[0]['mac']
                for i in range(1,len(tabelaArp)):
                    enderecoString = ','+str(tabelaArp[i]['porta'])+'-'+tabelaArp[i]['mac']
                    enderecos += enderecoString
                
                arquivo.writerow([switch.nome, switch.ip, switch.mac, switch.portas, enderecos])
                endereco=''

            else:
                arquivo.writerow([switch.nome, switch.ip, switch.mac, switch.portas])

a = index()
a.append(Switch("teste3", '192.168.1.2', "shdjshdjhsjd", 12))
a[1].adicionarDispositivo(4, "shajhsajshua")
salvar(a)