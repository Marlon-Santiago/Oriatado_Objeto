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

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_cacar = slfe.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_cacar
        

    def saca(self, valor):
        if(self.__pode_sacar(valo)):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou do limete disponivel para saque')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.settersetter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'
    
    @staticmethod
    def condigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

 