from models import init
from text import *
from handlers import *

# Iniciando as tabelas
init()

# Controlando opções
def main(message: str):
    render(message)

    option = int(input("> "))

    if option >= 1 and option <= 6: 
        render_option(option)

        parent = option

        option = int(input("> "))

        if option >= 1 and option < 5:
            handler = ''

            if parent == 1: handler   =   handle_customer(option)
            elif parent == 2: handler = handle_employeer(option)
            elif parent == 3: handler = handle_provider(option)
            elif parent == 4: handler = handle_category(option)
            elif parent == 5: handler = handle_product(option)
            elif parent == 6: handler = handle_cart(option)

            main(handler)
        else:
            main("")

# Executando o programa
main("")
    