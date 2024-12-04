import time

from models.computador_model import Computador
from tabulate import tabulate


class ComputadorCLI:
    def __init__(self, computador_db):
        self.db = computador_db

    # Somente pra exibir melhor os dados com tabulate
    def _exibir_tabela(self, headers, data):
        if not data:
            print("Nenhum dado disponível")
            return
        print(tabulate(data, headers=headers, tablefmt="grid"))

    def adicionar_computador(self):
        try:
            codigo = int(input("Código do computador: "))
            if self.db.collection.find_one({"codigo": codigo}):
                print("Código já existe no banco de dados. Tente outro.")
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
                codigo=codigo,
                quantidade=quantidade,
                custo_unitario=custo_unitario,
                preco_unitario=preco_unitario,
                memoria_ram=memoria_ram,
                armazenamento=armazenamento,
                processador=processador,
                placa_mae=placa_mae,
                placa_de_video=placa_de_video,
            )

            # Salvar no banco de dados convertendo para dicionário
            self.db.collection.insert_one(computador.__dict__)
            print("Computador adicionado com sucesso ao banco de dados!")
        except ValueError:
            print("Erro: Entrada inválida. Tente novamente.")

    def listar_computadores(self):
        computadores = self.db.collection.find()
        if not computadores:
            print("Nenhum computador cadastrado no banco de dados.")
            return

        print("\nLista de computadores:")

        headers = [
            "Código", "Quantidade", "Custo Unitário", "Preço Unitário",
            "Memória RAM", "Armazenamento", "Processador", "Placa Mãe", "Placa de Vídeo"
        ]
        data = []
        for computador_data in computadores:
            computador_data.pop('_id', None)
            computador = Computador(**computador_data)

            data.append([
                computador.codigo,
                computador.quantidade,
                f"R$ {computador.custo_unitario:.2f}",
                f"R$ {computador.preco_unitario:.2f}",
                computador.memoria_ram,
                computador.armazenamento,
                computador.processador,
                computador.placa_mae,
                computador.placa_de_video,
            ])

        self._exibir_tabela(headers, data)

        time.sleep(2)


    def editar_computador(self):
        try:
            codigo = int(input("Informe o código do computador que deseja editar: "))
            computador_data = self.db.find_one({"codigo": codigo})
            if not computador_data:
                print("Computador não encontrado no banco de dados.")
                return

            computador = Computador(**computador_data)

            print("Deixe o campo vazio para manter o valor atual.")

            quantidade = input(f"Quantidade [{computador.quantidade}]: ")
            custo_unitario = input(f"Custo unitário [{computador.custo_unitario:.2f}]: ")
            preco_unitario = input(f"Preço unitário [{computador.preco_unitario:.2f}]: ")
            memoria_ram = input(f"Memória RAM [{computador.memoria_ram}]: ")
            armazenamento = input(f"Armazenamento [{computador.armazenamento}]: ")
            processador = input(f"Processador [{computador.processador}]: ")
            placa_mae = input(f"Placa mãe [{computador.placa_mae}]: ")
            placa_de_video = input(f"Placa de vídeo [{computador.placa_de_video}]: ")

            # Atualizar os atributos do objeto
            computador.quantidade = int(quantidade) if quantidade else computador.quantidade
            computador.custo_unitario = float(custo_unitario) if custo_unitario else computador.custo_unitario
            computador.preco_unitario = float(preco_unitario) if preco_unitario else computador.preco_unitario
            computador.memoria_ram = memoria_ram if memoria_ram else computador.memoria_ram
            computador.armazenamento = armazenamento if armazenamento else computador.armazenamento
            computador.processador = processador if processador else computador.processador
            computador.placa_mae = placa_mae if placa_mae else computador.placa_mae
            computador.placa_de_video = placa_de_video if placa_de_video else computador.placa_de_video

            # Atualizar no banco de dados
            self.db.update_one({"codigo": codigo}, {"$set": computador.__dict__})
            print("Computador atualizado com sucesso no banco de dados!")
        except ValueError:
            print("Erro: Entrada inválida. Tente novamente.")

    def remover_computador(self):
        try:
            codigo = int(input("Informe o código do computador que deseja remover: "))
            resultado = self.db.delete_one({"codigo": codigo})
            if resultado.deleted_count == 0:
                print("Computador não encontrado no banco de dados.")
            else:
                print("Computador removido com sucesso do banco de dados!")
        except ValueError:
            print("Erro: Entrada inválida. Tente novamente.")
