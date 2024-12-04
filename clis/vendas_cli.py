from models.computador_model import Computador


class ComputadorCLI:
    def __init__(self):
        self.computadores = {}

    def adicionar_computador(self):
        try:
            codigo = int(input("Código do computador: "))
            if codigo in self.computadores:
                print("Código já existe. Tente outro.")
                return

            quantidade = int(input("Quantidade: "))
            custo_unitario = float(input("Custo unitário: "))
            preco_unitario = float(input("Preço unitário: "))
            memoria_ram = input("Memória RAM: ")
            armazenamento = input("Armazenamento: ")
            processador = input("Processador: ")
            placa_mae = input("Placa mãe: ")
            placa_de_video = input("Placa de vídeo: ")

            computador = Computador(
                codigo, quantidade, custo_unitario, preco_unitario,
                memoria_ram, armazenamento, processador, placa_mae, placa_de_video
            )
            self.computadores[codigo] = computador
            print("Computador adicionado com sucesso!")
        except ValueError:
            print("Erro: Entrada inválida. Tente novamente.")


    def listar_computadores(self):
        if not self.computadores:
            print("Nenhum computador cadastrado.")
            return

        print("\nLista de computadores:")
        for computador in self.computadores.values():
            print(computador)


    def editar_computador(self):
        try:
            codigo = int(input("Informe o código do computador que deseja editar: "))
            if codigo not in self.computadores:
                print("Computador não encontrado.")
                return

            print("Deixe o campo vazio para manter o valor atual.")
            computador = self.computadores[codigo]

            quantidade = input(f"Quantidade [{computador.quantidade}]: ")
            custo_unitario = input(f"Custo unitário [{computador.custo_unitario:.2f}]: ")
            preco_unitario = input(f"Preço unitário [{computador.preco_unitario:.2f}]: ")
            memoria_ram = input(f"Memória RAM [{computador.memoria_ram}]: ")
            armazenamento = input(f"Armazenamento [{computador.armazenamento}]: ")
            processador = input(f"Processador [{computador.processador}]: ")
            placa_mae = input(f"Placa mãe [{computador.placa_mae}]: ")
            placa_de_video = input(f"Placa de vídeo [{computador.placa_de_video}]: ")

            computador.quantidade = int(quantidade) if quantidade else computador.quantidade
            computador.custo_unitario = float(custo_unitario) if custo_unitario else computador.custo_unitario
            computador.preco_unitario = float(preco_unitario) if preco_unitario else computador.preco_unitario
            computador.memoria_ram = memoria_ram if memoria_ram else computador.memoria_ram
            computador.armazenamento = armazenamento if armazenamento else computador.armazenamento
            computador.processador = processador if processador else computador.processador
            computador.placa_mae = placa_mae if placa_mae else computador.placa_mae
            computador.placa_de_video = placa_de_video if placa_de_video else computador.placa_de_video

            print("Computador atualizado com sucesso!")
        except ValueError:
            print("Erro: Entrada inválida. Tente novamente.")


    def remover_computador(self):
        try:
            codigo = int(input("Informe o código do computador que deseja remover: "))
            if codigo not in self.computadores:
                print("Computador não encontrado.")
                return

            del self.computadores[codigo]
            print("Computador removido com sucesso!")
        except ValueError:
            print("Erro: Entrada inválida. Tente novamente.")
