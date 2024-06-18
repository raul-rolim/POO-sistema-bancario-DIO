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
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(nome, cpf, data_nascimento)
        self._endereco = endereco
        self._contas = []

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