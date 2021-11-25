import os

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def title():
    print(" ")
    print("  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░░░░░██████╗░██╗░░░██╗░██████╗██╗░░██╗░█████╗░██████╗░░░░░░░░░")
    print("░░░░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██║░░██║██╔══██╗██╔══██╗░░░░░░░░")
    print("░░░░░░░░██████╔╝░╚████╔╝░╚█████╗░███████║██║░░██║██████╔╝░░░░░░░░")
    print("░░░░░░░░██╔═══╝░░░╚██╔╝░░░╚═══██╗██╔══██║██║░░██║██╔═══╝░░░░░░░░░")
    print("░░░░░░░░██║░░░░░░░░██║░░░██████╔╝██║░░██║╚█████╔╝██║░░░░░░░░░░░░░")
    print("░░░░░░░░╚═╝░░░░░░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░░░░░░░░░")
    print("  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print(" ")

def options():
    options = [
        "1 -> Cliente",
        "2 -> Funcionário",
        "3 -> Fornecedor",
        "4 -> Categoria",
        "5 -> Produto",
        "6 -> Carrinho",
        "7 -> Sair",
        " "
    ]

    for option in options:
        print(option)

    print(" ")

def render(message: str):
    clear()
    title()

    if not len(message) == 0:
        print(message)
        print(" ")

    options()

def render_option(option: int):
    clear()
    title()

    keys = ['cliente', 'funcionário', 'fornecedor', 'categoria', 'produto', 'carrinho']

    key = keys[option - 1]

    options = [
        "1 -> Cadastrar {key}", 
        "2 -> Consultar {key}", 
        "3 -> Atualizar {key}", 
        "4 -> Deletar {key}", 
        "5 -> Voltar"
    ]

    for option in options:
        print(option.format(key = key))
