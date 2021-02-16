from movimiento import Movimiento
from cliente import Cliente

class Cuenta:

    __numero_cuenta = 0

    def __init__(self, titular, saldo):
        Cuenta.__numero_cuenta += 1
        self.__numero = Cuenta.__numero_cuenta
        self.__titular = titular
        self.__movimientos = []
        self.__saldo = saldo

    def anyadir_movimientos(self, movimiento):
        self.__movimientos.append(Movimiento(movimiento))
        self.__set_saldo(self.movimiento.cantidad())

    def movimientos(self):
        return self.__movimientos

    def __set_saldo(self, cantidad):
        self.__saldo += cantidad

    def numero(self):
        return self.__numero

    def titular(self):
        return f'{self.__titular.apellidos()} {self.__titular.nombre()}'
