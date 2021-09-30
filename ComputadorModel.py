import csv
from Computador import Computador

def index():
    listaDeComputadores = []

    with open('computadores.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')

        for row in csv_reader:
            if len(row) > 0:
                computador = Computador(row[0], row[1], row[2])

                listaDeComputadores.append(computador)
            else:
                break

    return listaDeComputadores


def salvar(lista: list):
    with open('computadores.csv', 'w', newline='') as csv_file:
        arquivo = csv.writer(csv_file, delimiter=';')

        for computador in lista:
            arquivo.writerow([computador.nome, computador.ip, computador.mac])


if __name__ == '__main__':
    a = index()
    for b in a:
        print(b)

    c = Computador("Lenovo", "192.168.0.5", "bb:bb:bb:bb:bb:bb")
    a.append(c)
    salvar(a)