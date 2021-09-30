import topologia

from Dispositivo import MacInvalidoException
from hash_table import *
from Switch import InvalidPortNumberException
from SwitchModel import *
from grafo import ConnectionNotPermitedException
import ComputadorModel


# Função para exibir a lista de switches ou computadores
def exibir_dispositivos(lista):
	try:
		print('\033[1;36m-------------------------------------')
		print(f'{"Seus " + lista[0].__class__.__name__ + "es":^35}')
		print('-------------------------------------')
	except IndexError:
		print('A lista de dispositivos está vazia!')
	else:
		for i, disp in enumerate(lista):
			print(i, disp)

		print('-------------------------------------\033[0;0m')


def exibir_topologia():
	print('\033[1;33m-------------------------------------')
	print(f'{"Dispositivos de sua topologia atual:":^35}')
	print('-------------------------------------')
	topologia.mostrar_topologia()
	print('\033[0;0m')


lista_de_switches = index()
lista_de_computadores = ComputadorModel.index()

try:
	topologia.carregar_topologia(lista_de_computadores, lista_de_switches)
except ConnectionNotPermitedException as cnpe:
	print(cnpe)


print('\n-------------------------------------')
print("Bem vindo ao Gerenciador de dispositivos".upper())

opcao = None

while opcao != '0':

	exibir_dispositivos(lista_de_switches)

	print()
	print('Escolha uma das opções a seguir :\n')
	print('1 - Cadastrar switch')
	print('2 - Cadastrar computador')
	print('3 - Exibir switches')
	print('4 - Exibir computadores')
	print('5 - Adicionar MAC em switch')
	print('6 - Descobrir porta por MAC')
	print('7 - Descobrir MAC por IP (ARP)')
	print('8 - Exibir dispositivos na topologia de rede')
	print('0 - Salvar e sair do gerenciador')

	opcao = input('\nOpção --> ')
	print()

	# cadastrar switch
	if opcao == '1':
		# possíveis excessões
		# Mac inválido ex
		# campos vazios if OK
		# porta não numérica ex OK
		# porta fora do intervalo ex OK
		while True:
			try:
				novo_switch = None
				while True:
					print('\033[1;33mDIGITE OS DADOS DO NOVO SWITCH')
					nome = input('Nome --> ')
					ip = input('IP --> ')
					mac = input('MAC --> ')
					portas = int(input('Quantidade de portas [4, 8, 16 ou 24] --> \033[0;0m'))

					if not nome and not ip and not mac:
						print('\033[1;31mNão são permitidos campos vazios!\n\033[0;0m')
						continue
					novo_switch = Switch(nome, ip, mac, portas)
					break
			except ValueError:
				print('\033[1;31mNo campo portas são permitidos apenas valores numéricos!\033[0;0m')
			except InvalidPortNumberException as ipne:
				print(f'\033[1;31m{ipne}\033[0;0m')
			except MacInvalidoException as mie:
				print(f'\033[1;31m{mie}\033[0;0m')
			else:
				lista_de_switches.append(novo_switch)
				print('\033[1;32mSwitch cadastrado com sucesso!\033[0;0m')
				break

	# cadastrar computador
	elif opcao == '2':
		while True:
			try:
				novo_pc = None
				while True:
					print('\033[1;33mDIGITE OS DADOS DO NOVO COMPUTADOR')
					nome = input('Nome --> ')
					ip = input('IP --> ')
					mac = input('MAC --> ')

					if not nome and not ip and not mac:
						print('\033[1;31mNão são permitidos campos vazios!\n\033[0;0m')
						continue
					novo_pc = ComputadorModel.Computador(nome, ip, mac)
					break
			except MacInvalidoException as mie:
				print(f'\033[1;31m{mie}\033[0;0m')
			else:
				lista_de_computadores.append(novo_pc)
				print('\033[1;32mComputador cadastrado com sucesso!\033[0;0m')
				break

	# exibir switches
	elif opcao == '3':
		exibir_dispositivos(lista_de_switches)

	# exibir computadores
	elif opcao == '4':
		exibir_dispositivos(lista_de_computadores)

	# Conectar dispositivo em switch
	elif opcao == '5':
		while True:
			try:
				exibir_dispositivos(lista_de_switches)
				print()
				sw = int(input('\033[1;33mEm qual switch deseja adicionar um MAC na tabela? '))
				mac = input('Digite o MAC do dispositivo que será conectado: ')
				porta = int(input('Digite a porta na qual o dispositivo será conectado: \033[0;0m'))

				lista_de_switches[sw].addMac(mac, porta)
			except ValueError:
				print('\033[1;31mDigite apenas valores numéricos para os campos switch e porta!\033[0;0m')
			except IndexError:
				print('\033[1;31mSwitch não encontrado!\033[0;0m')
			except InvalidPortNumberException as ipne:
				print(f'\033[1;31m{ipne}\033[0;0m')
			except AssertionError as ae:
				print(f'\033[1;31m{ae}\033[0;0m')
			except MacInvalidoException as mie:
				print(f'\033[1;31m{mie}\033[0;0m')
			except FullTableException:
				print('\033[1;31mA tabela MAC do switch já está cheia!\033[0;0m')
			else:
				print('\033[1;32mDispositivo conectado!!\033[0;0m')
				break

	# Descobrir porta por MAC
	elif opcao == '6':
		while True:
			try:
				exibir_dispositivos(lista_de_switches)
				print()
				sw = int(input('\033[1;33mEm qual switch deseja fazer a pesquisa de porta? '))
				mac = input('Digite o MAC do dispositivo que deseja pesquisar a porta: \033[0;0m')

				print(f'\033[1;32mA porta é {lista_de_switches[sw].buscar(mac)}\033[0;0m')
			except ValueError:
				print('\033[1;31mDigite apenas valores numéricos no switch!\033[0;0m')
			except IndexError:
				print('\033[1;31mSwitch não encontrado!\033[0;0m')
			except MacInvalidoException as mie:
				print(f'\033[1;31m{mie}\033[0;0m')
			except AbsentKeyException:
				print('\033[1;31mO MAC pesquisado não existe na tabela MAC deste switch!\033[0;0m')
			else:
				break

	# Descobrir MAC por IP (ARP)
	elif opcao == '7':
		try:
			exibir_topologia()
			pc = int(input('De qual dispositivo deseja fazer a solicitação ARP? '))
			ip = input('IP do dispositivo que deseja descobrir o MAC? ')

			mac = topologia.ARP(ip, topologia.dispositivos[pc])
		except ValueError:
			print('O código do dispositivo deve ser numérico!')
		except IndexError:
			print('O computador não existe na topologia!')
		else:
			if mac is None:
				print('MAC não encontrado!')
			else:
				print(f'O MAC de {ip} é {mac}')

	# exibir dispositivos da topologia
	elif opcao == '8':
		exibir_topologia()

	# Salvar e sair
	elif opcao == '0':
		salvar(lista_de_switches)
		ComputadorModel.salvar(lista_de_computadores)
		print('\033[1;34mbye')
		continue

	# Opção indisponível
	else:
		print('\033[1;31mOpção indisponível\033[0;0m')

	input('\n\033[1;36mENTER para retornar ao menu... \n\033[0;0m')
