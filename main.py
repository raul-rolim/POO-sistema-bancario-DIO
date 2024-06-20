from abc import ABC, abstractmethod

class Historico:
    def __init__(self):
        self._historico = ""

    def adicionar_transacao(self, transacao):
        self._historico += str(transacao)
class Deposito:

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        self._valor = float(input("Insira o valor que deseja depositar: "))
        return self._valor

class Saque:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        self._valor = float(input("Insira o valor que deseja sacar: "))
        return self._valor


class Conta(ABC):
    def __init__(self, cliente):
        self._cliente = cliente

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(Conta):

    def __init__(self, cliente, numero):
        Conta.__init__(self, cliente)
        self._saldo = 0
        self._agencia = "0001"
        self._numero = numero
        self._historico = Historico()
        self._limite = 500
        self._limite_saques = 3

    def depositar(self, valor):
        deposito_valido = valor > 0
        if deposito_valido:
            self._saldo += valor
            self._historico.adicionar_transacao(f"\nDepósito: R${self._saldo:.2f}")
            print("Depósito realizado com sucesso")
            return True
        else:
            print("O processo falhou, pois o valor inserido é inválido")
            return False
    @classmethod
    def nova_conta(cls, cliente, numero):
        print("Conta criada com sucesso")
        return cls(cliente, numero)

    def sacar(self, valor):
        limite_disponivel = self._limite_saques != 0
        saque_valido = (valor <= self._limite) and (valor > 0)

        if saque_valido and limite_disponivel:
            self._saldo -= valor
            self._historico.adicionar_transacao(f"\nSaque: R${self._saldo:.2f}")
            print("Saque realizado com sucesso")
            return True
        elif not limite_disponivel:
            print("Você atingiu o limite de saques diários")
            return False
        else:
            print("O valor inserido é inválido")

class PessoaFisica(ABC):
    def __init__(self, nome, cpf, data_nascimento):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

class Cliente(PessoaFisica):
    def __init__(self, nome, cpf, data_nascimento, endereco, senha):
        super().__init__(nome, cpf, data_nascimento)
        self._endereco = endereco
        self._senha = senha
        self._contas = []

    @property
    def cpf(self):
        return self._cpf

    @property
    def senha(self):
        return self._senha
    def realizar_transacao(self, conta, transacao):
        if transacao == Deposito:
            conta.depositar(transacao.valor)
        elif transacao == Saque:
            conta.sacar(transacao.valor)
        else:
            print("Transação inválida. Tente Novamente!")

    def adicionar_conta(self, conta):
        self._contas.append(conta)
        print("Conta adicionada com sucesso")
        return True

    @classmethod
    def nova_conta(cls):
        nome = input("Insira seu nome: ")
        cpf = input("Insira seu CPF: ")
        data_nascimento = input("Insira sua data de nascimento: ")
        endereco = input("Insira seu endereco: ")
        senha = input("Insira uma senha para a conta: ")
        return nome, cpf, data_nascimento, endereco, senha

    def __repr__(self):
        return (f"Nome: {self._nome}, CPF: {self._cpf}, Nascimento: {self._data_nascimento}, "
                f"Endereço: {self._endereco}, Senha: {self._senha}\n")

class Usuarios:
    def __init__(self):
        self._lista_usuarios = []

    def adicionar_usuario(self, usuario):
        self._lista_usuarios.append(usuario)
        print("Usuário criado com sucesso")
        return True

    def listar(self):
        return self._lista_usuarios

    @property
    def lista_usuarios(self):
        return self._lista_usuarios
class Menu:
    def menu_inicial(self):
        lista_de_usuarios = Usuarios()
        print("Menu principal")
        while True:
            opcoes = "1 - Criar Usuário\n2 - Criar Conta Corrente\n3 - Fazer Login\n4 - Sair\nEscolha: "
            escolha = int(input(opcoes))
            match escolha:
                case 1:
                    # nome, cpf, data_nascimento, endereco, senha = Cliente.nova_conta()
                    nome = "teste"
                    cpf = "12345"
                    data_nascimento = "01/01/2021"
                    endereco = "adqwqwdqw"
                    senha = "12345"
                    novo_cliente = Cliente(nome, cpf, data_nascimento, endereco, senha)
                    lista_de_usuarios.adicionar_usuario(novo_cliente)

                case 2:
                    nova_conta_corrente = ContaCorrente.nova_conta(lista_de_usuarios.lista_usuarios[0], len(lista_de_usuarios.lista_usuarios))
                    cliente = lista_de_usuarios.lista_usuarios[0]
                    cliente.adicionar_conta(nova_conta_corrente)

                case 3:
                    cpf = input("Insira o CPF da sua conta: ")
                    senha = input("Insira sua senha: ")
                    for conta in lista_de_usuarios.lista_usuarios:
                        if conta.cpf == cpf and conta.senha == senha:
                            print("Bem Vindo")

                    print("Tente novamente")

                case 4:
                    print("Obrigado por utilizar o nosso serviço!\nAté a próxima!")
                    exit(0)
                case 12:
                    print(lista_de_usuarios.listar())

menu = Menu()
menu.menu_inicial()