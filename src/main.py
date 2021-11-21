import models
from text import *

# Iniciando as tabelas
models.init()

# Controlando opções
def main(message: str):
    render(message)

    parent = 0
    option = int(input("> "))

    if option <= 6 or option >= 1: 
        render_option(option, parent)

        parent = option

        option = int(input("> "));

        if option >= 5 or option <= 0: main()
        else:
            print(" ")

            if parent == 1 or parent == 2:
                if option == 1:
                    cpf = int(input("CPF > "))
                    name = input("Nome > ")
                
                    if parent == 2:
                        role = input("Cargo > ")

                        # TODO: Cadastrar funcionário aqui!
                        print(cpf, name, role)
                    else:
                        # TODO: Cadastrar cliente aqui!
                        print(cpf, name)
                
                    main("Usuário cadastrado com sucesso")
                elif option == 2:
                    cpf = int(input("CPF > "))

                    # if parent == 2:
                        # TODO: Consultar funcionário aqui!
                    # else:
                        # TODO: Consultar cliente aqui!
                    
                    main("<dados do usuário>")
                elif option == 3:
                    cpf = int(input("CPF > "))

                    if parent == 1:
                        main("Processo não disponível em clientes.")
                    # else:
                        # role = input("Cargo > ")
                        # TODO: Atualizar cargo do funcionário aqui!
                elif option == 4:
                    cpf = int(input("CPF > "))

                    # if parent == 1:
                        # TODO: Deletar o cliente
                    # elif parent == 2:
                        # TODO: Demitir o funcionário
            elif parent == 3:
                cnpj = int(input("CNPJ > "))
                name = input("Nome > ")

                # TODO: Cadastrar fornecedor aqui!

                main("Fornecedor cadastrado com sucesso.")
            elif parent == 4:
                name = input("Nome > ")

                # TODO: Cadastrar categoria aqui!

                main("Categoria cadastrada com sucesso.")
            elif parent == 5:
                name = input("Nome > ")
                # TODO: Mostrar todas as categorias aqui e esperar ele pegar uma!
                # TODO: Mostrar todos os fornecedores aqui e esperar ele pegar um!
                price = int(input("Preço > "))
                amount = int(input("Quantidade disponível > "))

                # TODO: Cadastrar produto!

                main("Produto cadastrado com sucesso.")
            elif parent == 6:
                cpf = input("CPF > ")

                # TODO: Mostrar todos os produtos COM ESTOQUE DISPONÍVEL e 
                # esperar ele pegar até quando quiser parar!

                # TODO: Calcular preço total

                payment_type = input("Pagamento (Crédito/Débito/Dinheiro) > ").replace('é', 'e').upper()

                while not payment_type in ['CREDITO', 'DEBITO', 'DINHEIRO']:
                    print("Insira uma opção válida!")

                    payment_type = input("Pagamento (Crédito/Débito/Dinheiro) > ").replace('é', 'e').upper()

                # TODO: Cadastrar carrinho!

                main("Compra feita com sucesso.")

# Executando o programa
main("")
    