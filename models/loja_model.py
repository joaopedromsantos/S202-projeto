from models.computador_model import Computador
from models.comprador_model import Comprador


class Loja:
    def __init__(self, database, nome: str, cnpj: str, saldo: float, computadores=None):
        self.db = database

        self.nome = nome
        self.cnpj = cnpj
        self.saldo = saldo
        self.computadores = computadores or []
        self.clientes = []
