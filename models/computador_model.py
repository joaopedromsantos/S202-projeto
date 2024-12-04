class Computador:
    def __init__(self, codigo: int, quantidade: int, custo_unitario: float, preco_unitario: float, memoria_ram: str,
                 armazenamento: str, processador: str, placa_mae: str, placa_de_video: str):
        self.codigo = codigo
        self.quantidade = quantidade
        self.custo_unitario = custo_unitario
        self.preco_unitario = preco_unitario

        self.memoria_ram = memoria_ram
        self.armazenamento = armazenamento
        self.processador = processador
        self.placa_mae = placa_mae
        self.placa_de_video = placa_de_video
