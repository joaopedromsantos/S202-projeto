from database import Database
from clis.computadores_cli import ComputadorCLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
computador_db = Database(database="siscom", collection="computadores")
vendas_db = Database(database="siscom", collection="vendas")

crud_computador = ComputadorCLI(computador_db)


def exibir_menu():
    print("\nBem-vindo à loja de computadores - SISCOM")
    print("1. Gerenciamento de Computadores")
    print("2. Gerenciamento de Compras e Vendas")
    print("3. Sair")

def menu_computadores():
    print("\n--- CRUD de Computadores ---")
    print("1. Adicionar Computador")
    print("2. Remover Computador")
    print("3. Editar Computador")
    print("4. Listar Computadores")
    print("5. Voltar")

def menu_compras():
    print("\n--- Compras e Vendas ---")
    print("1. Adicionar Compra")
    print("2. Remover Compra")
    print("3. Editar Compra")
    print("4. Mostrar Histórico")
    print("5. Voltar")


while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            while True:
                menu_computadores()
                escolha = input("Escolha uma opção: ")
                if escolha == '1':
                    crud_computador.adicionar_computador()
                elif escolha == '4':
                    crud_computador.listar_computadores()
                elif escolha == '5':
                    break
        elif opcao == '2':
            while True:
                menu_compras()
                escolha = input("Escolha uma opção: ")
                if escolha == '1':
                    pass
                elif escolha == '4':
                    pass
                elif escolha == '5':
                    break
        elif opcao == '3':
            print("Encerrando o sistema. Obrigado!")
            break
        else:
            print("Opção inválida, tente novamente.")