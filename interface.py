from Dispositivo import MacInvalido
from Switch import Switch
from hash_table import *
from SwitchModel import *


def exibir_swiches(lista):
	for i, sw in enumerate(lista):
		print(i, sw)

lista_de_switches = index()

print("Bem vindo ao Gerenciador de Switches\n")

opcao = None

while opcao != '0':

	print('-------------------------------------')
	print('\nSeus switches:\n')
	exibir_swiches(lista_de_switches)

	print()
	print('Escolha a opção a seguir :\n')
	print('1 - Cadastrar switch')
	print('2 - Exibir switches')
	print('3 - Conectar dispositivo')
	print('4 - Descobrir porta')
	print('0 - Salvar e sair do gerenciador')

	opcao = input('\nOpção --> ')
	print()

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
					print('DIGITE OS DADOS DO NOVO SWITCH')
					nome = input('Nome --> ')
					ip = input('IP --> ')
					mac = input('MAC --> ')
					portas = int(input('Quantidade de portas [4, 8, 16 ou 24] --> '))

					if not nome and not ip and not mac:
						print('Não são permitidos campos vazios!\n')
						continue
					novo_switch = Switch(nome, ip, mac, portas)
					break
			except ValueError:
				print('No campo portas são permitidos apenas valores numéricos!')
			except AssertionError:
				print('O switch pode possuir apenas 4, 8, 16 ou 24 portas!')
			except MacInvalido:
				print('O MAC digitado não é válido!')
			else:
				lista_de_switches.append(novo_switch)
				print('Switch cadastrado com sucesso!')
				break

	elif opcao == '2':
		exibir_swiches(lista_de_switches)
	elif opcao == '3':
		while True:
			try:
				exibir_swiches(lista_de_switches)
				print()
				sw = int(input('Em qual switch deseja conectar o dispositivo? '))
				mac = input('Digite o MAC do dispositivo que deseja conectar: ')
				porta = int(input('Digite a porta do dispositivo que deseja conectar: '))

				lista_de_switches[sw].addMac(mac, porta)
			except ValueError:
				print('Digite apenas valores numéricos no switch e na porta!')
			except IndexError:
				print('Switche não encontrado!')
			except MacInvalido:
				print('O MAC digitado não é válido!')
			except FullTableException:
				print('A tabela MAC do switch já está cheia!')
			else:
				print('Dispositivo conectado!!')
				break
	elif opcao == '4':
		while True:
			try:
				exibir_swiches(lista_de_switches)
				print()
				sw = int(input('Em qual switch deseja conectar o dispositivo? '))
				mac = input('Digite o MAC do dispositivo que deseja pesquisar a porta: ')

				print('A porta é', lista_de_switches[sw].buscar(mac))
			except ValueError:
				print('Digite apenas valores numéricos no switch!')
			except IndexError:
				print('Switch não encontrado!')
			except MacInvalido:
				print('O MAC digitado não é válido!')
			except AbsentKeyException:
				print('O MAC pesquisado não existe na tabela MAC deste switch!')
			else:
				break
	elif opcao == '0':
		salvar(lista_de_switches)
		print('bye')
	else:
		print('Opção indispnível')
