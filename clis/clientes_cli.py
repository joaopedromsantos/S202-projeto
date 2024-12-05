import time
from tabulate import tabulate
from models.clientes_model import Cliente


class ClienteCLI:
    def __init__(self, cliente_db):
        self.db = cliente_db

    def _exibir_tabela(self, headers, data):
        if not data:
            print("Nenhum dado disponível")
            return
        print(tabulate(data, headers=headers, tablefmt="grid"))

    def adicionar_cliente(self):
        try:
            # Verificando existência
            cpf = input("CPF do cliente: ")
            if self.db.collection.find_one({"cpf": cpf}):
                print("CPF já existe no banco de dados. Tente outro.")
                return

            nome = input("Nome do cliente: ")
            email = input("Email do cliente: ")

            cliente = Cliente(nome=nome, email=email, cpf=cpf)

            self.db.collection.insert_one(cliente.__dict__)
            print("Cliente adicionado com sucesso!")
        except Exception as e:
            print(f"Erro ao adicionar cliente: {e}")

    def listar_clientes(self):
        # Verificando existência
        clientes = self.db.collection.find()
        if not clientes:
            print("Nenhum cliente cadastrado no banco de dados.")
            return

        print("\nLista de clientes:")

        headers = ["Nome", "Email", "CPF"]
        data = []
        for cliente_data in clientes:
            cliente_data.pop('_id', None)
            cliente = Cliente(**cliente_data)
            data.append([cliente.nome, cliente.email, cliente.cpf])

        self._exibir_tabela(headers, data)
        time.sleep(2)

    def editar_cliente(self):
        try:
            cpf = input("Informe o CPF do cliente que deseja editar: ")

            # Verificando existência
            cliente_data = self.db.collection.find_one({"cpf": cpf})
            if not cliente_data:
                print("Cliente não encontrado no banco de dados.")
                return

            cliente_data.pop('_id', None)

            # Desestruturando o dicionário para passar para parâmetros
            cliente = Cliente(**cliente_data)

            print("Deixe o campo vazio para manter o valor atual.")
            nome = input(f"Nome [{cliente.nome}]: ")
            email = input(f"Email [{cliente.email}]: ")

            cliente.nome = nome if nome else cliente.nome
            cliente.email = email if email else cliente.email

            # Atualizando
            self.db.collection.update_one({"cpf": cpf}, {"$set": cliente.__dict__})
            print("Cliente atualizado com sucesso no banco de dados!")
        except Exception as e:
            print(f"Erro: {e}")

    def remover_cliente(self):
        try:
            cpf = input("Informe o CPF do cliente que deseja remover: ")
            resultado = self.db.collection.delete_one({"cpf": cpf})
            if resultado.deleted_count == 0:
                print("Cliente não encontrado no banco de dados.")
            else:
                print("Cliente removido com sucesso do banco de dados!")
        except Exception as e:
            print(f"Erro: {e}")
