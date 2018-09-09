'''
Crie um software de gerenciamento banário
Esse software poderá ser capaz de criar clientes e contas
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar_saldo
'''

from cliente import Cliente
from conta import Conta
from pycpfcnpj import cpfcnpj
import os

sair = False

c = 0
c += 1

lista_clientes = list()
lista_contas = list()


def pause():
    input('Pressione ENTER para continuar...')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_principal():
    clear_screen()

    print('\n BANCOS DOS AFOGADOS')

    print('''\n....MENU....\n
    [1] Novo cliente
    [2] Nova conta        
    [3] Buscar cliente       
    [0] Sair''')

    opcao = int(input('Opções:'))

    return opcao


def menu_conta(conta):
    clear_screen()

    while True:

        print(f'Operações disponíveis para a conta do cliente: {conta.cliente.nome}')

        print('''
        [1] Depositar
        [2] Sacar
        [3] Consultar Saldo
        [4] Sair''')

        opcao = int(input('Opção desejada:'))

        if opcao == 1:
            valor_deposito = float(input('Quanto deseja depositar? R$: '))
            conta.depositar(valor_deposito)

        elif opcao == 2:
            valor_saque = float(input('Quanto deseja sacar? R$: '))
            conta.sacar(valor_saque)

        elif opcao == 3:
            saldo = conta.con_saldo()
            print(f'O saldo é de R$ {saldo}')

        elif opcao == 4:
            break


def criar_cliente():
    clear_screen()

    print('\nAdicionar novo cliente')

    nome = str(input('Nome:')).upper()

    while True:
        cpf_number = str(input('CPF:'))
        validado = cpfcnpj.validate(cpf_number)

        if validado:
            break
        else:
            print('Erro. Favor inserir um CPF válido')

    ano_nasc = int(input('Ano de Nascimento:'))

    cliente = Cliente(nome, cpf_number, ano_nasc)

    print(f'Idade: {cliente.idade}')

    return cliente


def criar_conta(cliente):
    clear_screen()

    print('\nAdicionar nova conta')
    print(f'Nome do cliente: {cliente.nome}')

    saldo = int(input('Saldo:'))
    limite = int(input('Limite:'))

    return Conta(cliente, saldo, limite)


def buscar_cliente(cpf_number):
    for cliente in lista_clientes:
        if cliente.cpf_number == cpf_number:
            return cliente
    return False


def buscar_conta(conta):
    for conta in lista_contas:
        return conta
    return False


##################################
# Loop principal
##################################

while not sair:

    opcao = menu_principal()

    # Criar cliente
    if opcao == 1:
        cliente = criar_cliente()
        lista_clientes.append(cliente)

        r = str(input(f'Deseja adicionar uma conta ao Cliente {cliente.nome}? [S/N]')).upper().strip()[0]

        if r in 'S':
            conta = criar_conta(cliente)
            lista_contas.append(conta)

            menu_conta(conta)
            pause()

        if r in 'N':
            pause()
            continue

    # Criar conta
    elif opcao == 2:
        conta = criar_conta(cliente)
        lista_contas.append(conta)

        menu_conta(conta)

    # Buscar cliente
    elif opcao == 3:

        while True:

            busca = str(input('Favor digitar o CPF do cliente:')).strip()
            cliente = buscar_cliente(busca)

            if not cliente:
                print('Cliente não encontrado.')
                pause()
                break
            else:
                print(f'Cliente {cliente.nome} encontrado.')

                conta = buscar_conta(cliente.cpf_number)
                if conta:
                    while True:
                        op = str(input('Deseja fazer alguma operação? [S/N]')).upper().strip()[0]

                        if op in 'S':
                            menu_conta(conta)

                        if op in 'N':
                            break

                else:
                    print('Cliente sem conta.')
                    while True:
                        op = str(input('Deseja criar uma conta para o cliente? [S/N]')).upper().strip()[0]

                        if op in 'S':
                            criar_conta(cliente)

                        if op in 'N':
                            pause()
                            break

                op = str(input('Deseja voltar para o menu principal?[S/N]')).upper().strip()[0]
                if op in 'S':
                    break

    elif opcao == 0:
        sair = True
        print('--' * 10, ' Programa encerrado', '--' * 10)

    else:
        print('Opção inválida, por favor tente novamente. ')
