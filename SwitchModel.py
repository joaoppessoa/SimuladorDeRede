import csv
from Switch import Switch


def index():
    listaDeSwitch = []

    with open('banco.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')

        for row in csv_reader:
            if len(row) > 0:
                switch = Switch(row[0], row[1], row[2], int(row[3]))

                if len(row) == 5:
                    tabelaMac = row[4].split(',')

                    for enderecos in tabelaMac:
                        enderecoArray = enderecos.split('-')

                        switch.addMac(enderecoArray[1], enderecoArray[0])

                listaDeSwitch.append(switch)
            else:
                break

    return listaDeSwitch


def salvar(lista: list):
    with open('banco.csv', 'w', newline='') as csv_file:
        arquivo = csv.writer(csv_file, delimiter=';')

        for switch in lista:
            if switch.haPortasEmUso():
                tabelaMac = switch.returnEnderecos()
                entradas_string = []

                for entry in tabelaMac:
                    entradas_string.append(f'{str(entry[1])}-{entry[0]}')
                    # print(entry[0], entry[1])

                tabela_mac_string = ','.join(entradas_string)
                arquivo.writerow([switch.nome, switch.ip, switch.mac, switch.portas, tabela_mac_string])
            else:
                arquivo.writerow([switch.nome, switch.ip, switch.mac, switch.portas])


a = index()

salvar(a)
