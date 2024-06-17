from abc import ABC, abstractmethod

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Historico:

    def adicionar_transacao(self, transacao):
        pass
class Deposito(Transacao):

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        pass

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
        #Inserir o registro da transação no histórico
        valor_valido = valor > 0
        if valor_valido:
            self._saldo += valor
            print("Depósito realizado com sucesso")
            return True
        else:
            print("O processo falhou, pois o valor inserido é inválido")
            return False
    #é um método que pode ser usado sem necessidade de instanciar
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        pass

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
        pass

    def adicionar_conta(self, conta):
        pass