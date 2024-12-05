from database import Database
from clis.computadores_cli import ComputadorCLI
from clis.clientes_cli import ClienteCLI
from clis.vendas_cli import VendaCLI

computador_db = Database(database="siscom", collection="computadores")
vendas_db = Database(database="siscom", collection="vendas")
clientes_db = Database(database="siscom", collection="clientes")

crud_computador = ComputadorCLI(computador_db)
crud_cliente = ClienteCLI(clientes_db)
crud_vendas = VendaCLI(cliente_db=clientes_db, computador_db=computador_db, venda_db=vendas_db)


def exibir_menu():
    print("\nBem-vindo à loja de computadores - SISCOM")
    print("1. Gerenciamento de Computadores")
    print("2. Gerenciamento de Clientes")
    print("3. Gerenciamento de Compras e Vendas")
    print("4. Sair")

def menu_computadores():
    print("\n--- CRUD de Computadores ---")
    print("1. Adicionar Computador")
    print("2. Remover Computador")
    print("3. Editar Computador")
    print("4. Listar Computadores")
    print("5. Voltar")

def menu_clientes():
    print("\n--- CRUD de Clientes ---")
    print("1. Adicionar Cliente")
    print("2. Remover Cliente")
    print("3. Editar Cliente")
    print("4. Listar Clientes")
    print("5. Voltar")

def menu_compras():
    print("\n--- Compras e Vendas ---")
    print("1. Adicionar Compra")
    print("2. Remover Compra")
    print("3. Mostrar Histórico")
    print("4. Voltar")


while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            while True:
                menu_computadores()
                escolha = input("Escolha uma opção: ")
                if escolha == '1':
                    crud_computador.adicionar_computador()
                elif escolha == '2':
                    crud_computador.remover_computador()
                elif escolha == '3':
                    crud_computador.editar_computador()
                elif escolha == '4':
                    crud_computador.listar_computadores()
                elif escolha == '5':
                    break
        elif opcao == '2':
            while True:
                menu_clientes()
                escolha = input("Escolha uma opção: ")
                if escolha == '1':
                    crud_cliente.adicionar_cliente()
                elif escolha == '2':
                    crud_cliente.remover_cliente()
                elif escolha == '3':
                    crud_cliente.editar_cliente()
                elif escolha == '4':
                    crud_cliente.listar_clientes()
                elif escolha == '5':
                    break

        elif opcao == '3':
            while True:
                menu_compras()
                escolha = input("Escolha uma opção: ")
                if escolha == '1':
                    crud_vendas.registrar_venda()
                elif escolha == '2':
                    crud_vendas.remover_venda()
                elif escolha == '3':
                    crud_vendas.listar_vendas()
                elif escolha == '4':
                    break

        elif opcao == '4':
            print("Encerrando o sistema. Obrigado!")
            break
        else:
            print("Opção inválida, tente novamente.")