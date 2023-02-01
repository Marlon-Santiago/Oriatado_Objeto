class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        
        print(f'Construindo objeto... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular}')

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.settersetter
    def limite(self, limite):
        self.__limite = limite

