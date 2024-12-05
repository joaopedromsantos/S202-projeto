from datetime import datetime


class Venda:
    def __init__(self, cliente_cpf, computador_codigo, quantidade, data=None, lucro=0.0):
        self.cliente_cpf = cliente_cpf
        self.computador_codigo = computador_codigo
        self.quantidade = quantidade
        self.data = data or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.lucro = lucro
