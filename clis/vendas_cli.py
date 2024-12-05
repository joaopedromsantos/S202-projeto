import time
from tabulate import tabulate
from models.vendas_model import Venda


class VendaCLI:
    def __init__(self, cliente_db, computador_db, venda_db):
        self.cliente_db = cliente_db
        self.computador_db = computador_db
        self.venda_db = venda_db

    def _exibir_tabela(self, headers, data):
        if not data:
            print("Nenhum dado disponível")
            return
        print(tabulate(data, headers=headers, tablefmt="grid"))

    def registrar_venda(self):
        try:
            cliente_cpf = input("Informe o CPF do cliente: ")
            cliente = self.cliente_db.collection.find_one({"cpf": cliente_cpf})
            if not cliente:
                print("Cliente não encontrado no banco de dados. Registre-o primeiro!")
                return

            computador_codigo = int(input("Informe o código do computador: "))
            computador = self.computador_db.collection.find_one({"codigo": computador_codigo})
            if not computador:
                print("Computador não encontrado no banco de dados. Registre-o primeiro!")
                return

            elif computador["quantidade"] <= 0:
                print("Computador sem estoque")
                return

            lucro = computador["preco_unitario"] - computador["custo_unitario"]

            novo_estoque = computador["quantidade"] - 1

            self.computador_db.collection.update_one(
                {"codigo": computador_codigo}, {"$set": {"quantidade": novo_estoque}}
            )

            venda = Venda(
                cliente_cpf=cliente_cpf,
                computador_codigo=computador_codigo,
                quantidade=1,
                lucro=lucro
            )
            self.venda_db.collection.insert_one(venda.__dict__)
            print("Venda registrada com sucesso!")

        except ValueError:
            print("Erro: Entrada inválida.")

    def listar_vendas(self):
        vendas = self.venda_db.collection.find()
        if not vendas:
            print("Nenhuma venda registrada.")
            return

        print("\nLista de vendas:")
        headers = ["Cliente (CPF)", "Computador (Código)", "Quantidade", "Data", "Lucro"]
        data = []
        for venda in vendas:
            venda.pop('_id', None)
            data.append([
                venda["cliente_cpf"],
                venda["computador_codigo"],
                venda["quantidade"],
                venda["data"],
                f"R$ {venda['lucro']:.2f}",
            ])
        self._exibir_tabela(headers, data)
        time.sleep(2)

    def remover_venda(self):
        try:
            cliente_cpf = input("Informe o CPF do cliente da venda que deseja remover: ")
            computador_codigo = int(input("Informe o código do computador da venda que deseja remover: "))

            venda = self.venda_db.collection.find_one({"cliente_cpf": cliente_cpf, "computador_codigo": computador_codigo})
            if not venda:
                print("Venda não encontrada no banco de dados.")
                return

            computador = self.computador_db.collection.find_one({"codigo": computador_codigo})
            if not computador:
                print("Erro: Computador associado à venda não encontrado no banco de dados.")
                return

            self.computador_db.collection.update_one(
                {"codigo": computador_codigo}, {"$set": {"quantidade": computador["quantidade"] + 1}}
            )

            self.venda_db.collection.delete_one({"_id": venda["_id"]})
            print("Venda removida com sucesso, e o estoque foi atualizado!")

        except ValueError:
            print("Erro: Entrada inválida.")
