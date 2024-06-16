from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, cliente, numero):
        self._numero = numero
        self._cliente = cliente

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia, saldo, historico):
        Conta.__init__(self, cliente, numero)
        self._saldo = 0
        self._agencia = "0001"
        self._historico = Historico()

    