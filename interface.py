import topologia

from Dispositivo import MacInvalidoException
from hash_table import *
from Switch import Switch
from SwitchModel import *


def exibir_swiches(lista):
	for i, sw in enumerate(lista):
		print(i, sw)


lista_de_switches = index()

print('\n-------------------------------------')
print("Bem vindo ao Gerenciador de dispositivos".upper())

opcao = None

while opcao != '0':

	print('-------------------------------------')
	print('\033[1;36mSeus switches:')
	print('-------------------------------------')
	exibir_swiches(lista_de_switches)
	print('-------------------------------------\033[0;0m')

	print()
	print('Escolha uma das opções a seguir :\n')
	print('1 - Cadastrar switch')
	print('2 - Cadastrar computador')
	print('3 - Exibir switches')
	print('4 - Exibir computadores')
	print('5 - Conectar dispositivo em switch')
	print('6 - Descobrir porta por MAC')
	print('7 - Descobrir MAC por IP (ARP)')
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
			except AssertionError:
				print('\033[1;31mO switch pode possuir apenas 4, 8, 16 ou 24 portas!\033[0;0m')
			except MacInvalidoException:
				print('\033[1;31mO MAC digitado não é válido!\033[0;0m')
			else:
				lista_de_switches.append(novo_switch)
				print('\033[1;32mSwitch cadastrado com sucesso!\033[0;0m')
				break

	# cadastrar computador
	elif opcao == '2':
		pass

	# exibir switches
	elif opcao == '3':
		exibir_swiches(lista_de_switches)

	# exibir computadores
	elif opcao == '4':
		pass

	# Conectar dispositivo em switch
	elif opcao == '5':
		while True:
			try:
				exibir_swiches(lista_de_switches)
				print()
				sw = int(input('\033[1;33mEm qual switch deseja conectar o dispositivo? '))
				mac = input('Digite o MAC do dispositivo que será conectado: ')
				porta = int(input('Digite a porta na qual o dispositivo será conectado: \033[0;0m'))

				lista_de_switches[sw].addMac(mac, porta)
			except ValueError:
				print('\033[1;31mDigite apenas valores numéricos para os campos switch e porta!\033[0;0m')
			except IndexError:
				print('\033[1;31mSwitch não encontrado!\033[0;0m')
			except MacInvalidoException:
				print('\033[1;31mO MAC digitado não é válido!\033[0;0m')
			except FullTableException:
				print('\033[1;31mA tabela MAC do switch já está cheia!\033[0;0m')
			else:
				print('\033[1;32mDispositivo conectado!!\033[0;0m')
				break

	# Descobrir porta por MAC
	elif opcao == '6':
		while True:
			try:
				exibir_swiches(lista_de_switches)
				print()
				sw = int(input('\033[1;33mEm qual switch deseja fazer a pesquisa de porta? '))
				mac = input('Digite o MAC do dispositivo que deseja pesquisar a porta: \033[0;0m')

				print(f'\033[1;32mA porta é {lista_de_switches[sw].buscar(mac)}\033[0;0m')
			except ValueError:
				print('\033[1;31mDigite apenas valores numéricos no switch!\033[0;0m')
			except IndexError:
				print('\033[1;31mSwitch não encontrado!\033[0;0m')
			except MacInvalidoException:
				print('\033[1;31mO MAC digitado não é válido!\033[0;0m')
			except AbsentKeyException:
				print('\033[1;31mO MAC pesquisado não existe na tabela MAC deste switch!\033[0;0m')
			else:
				break

	# Descobrir MAC por IP (ARP)
	elif opcao == '7':
		pass

	# Salvar e sair
	elif opcao == '0':
		salvar(lista_de_switches)
		print('\033[1;34mbye')

	# Opção indisponível
	else:
		print('\033[1;31mOpção indisponível\033[0;0m')
