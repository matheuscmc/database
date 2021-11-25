from models import *

def handle_customer(option: int):
    if option > 4 or option < 1: return ""

    cpf = int(input("CPF > "))

    if option == 1: 
        name = input("Nome > ")

        user = Customer.create(
            cpf=cpf,
            name=name
        )

        return "Cliente {name}, com CPF {cpf} criado com sucesso.".format(
            name=user.name,
            cpf=user.cpf
        )
    elif option == 2:
        user = Customer.get(cpf=cpf)

        return "O CPF {cpf} está cadastrado com o cliente {name}.".format(
            cpf=cpf,
            name=user.name
        )
    elif option == 3:
        name = input("Novo nome > ")

        user = Customer.get(cpf=cpf)
        old_name = user.name

        user.name = name
        user.save()

        return "Cliente {name} teve seu nome alterado para {username} com sucesso.".format(
            name=old_name,
            username=user.name
        )
    else:
        user = Customer.get(Customer.cpf == cpf)
        user.delete_instance()

        return "O sr(a). {name} já não é mais um cliente.".format(
            name=user.name
        )

def handle_employeer(option: int):
    if option > 4 or option < 1: return ""

    cpf = int(input("CPF > "))

    if option == 1: 
        name = input("Nome > ")
        role = input("Cargo > ")

        user = Employeer.create(
            cpf=cpf,
            name=name,
            role=role
        )

        return "Funcionário {name}, de cargo {role}, com CPF {cpf} criado com sucesso.".format(
            name=user.name,
            cpf=user.cpf,
            role=role
        )
    elif option == 2:
        user = Employeer.get(cpf=cpf)

        return "O CPF {cpf} está cadastrado com o funcionário {name}, de cargo {role}.".format(
            cpf=cpf,
            name=user.name,
            role=user.role
        )
    elif option == 3:
        role = input("Novo cargo > ")

        user = Employeer.get(cpf=cpf)

        user.role = role
        user.save()

        return "Fucionário {name} teve seu cargo alterado para {role} com sucesso.".format(
            name=user.name,
            role=user.role
        )
    else:
        user = Employeer.get(Employeer.cpf == cpf)
        user.delete_instance()

        return "O sr(a). {name} já não é mais um funcionário.".format(
            name=user.name
        )

def handle_provider(option: int):
    if option > 4 or option < 1: return ""

    cnpj = int(input("CNPJ > "))

    if option == 1: 
        name = input("Nome > ")

        provider = Provider.create(
            cnpj=cnpj,
            name=name
        )

        return "Fornecedor {name} com CNPJ {cnpj} criado com sucesso.".format(
            cnpj=cnpj,
            name=name
        )
    elif option == 2:
        provider = Provider.get(cnpj=cnpj)

        return "O fornecedor com CPNJ {cnpj} está cadastrado com nome {name}.".format(
            cnpj=cnpj,
            name=provider.name
        )
    elif option == 3:
        return "Operação não suportada."
    else:
        provider = Provider.get(Employeer.id == id)
        provider.delete_instance()

        return "{cnpj} | {name} já não fornece mais produtos.".format(
            cnpj=cnpj,
            name=provider.name
        )

def handle_category(option: int):
    if option > 4 or option < 1: return ""

    id = int(input("ID > "))

    if option == 1: 
        name = input("Nome > ")

        category = Category.create(
            id=id,
            name=name
        )

        return "Categoria {name} com ID {id} criado com sucesso.".format(
            id=id,
            name=name
        )
    elif option == 2:
        category = Category.get(id=id)

        return "A categoria {id} está cadastrada com nome {name}.".format(
            id=id,
            name=category.name
        )
    elif option == 3:
        return "Operação não suportada."
    else:
        category = Category.get(Employeer.id == id)
        category.delete_instance()

        return "{name} já não existe.".format(
            name=category.name
        )

def handle_product(option: int):
    if option > 4 or option < 1: return ""

    id = int(input("ID > "))

    if option == 1: 
        name = input("Nome > ")
        price = int(input("Preço > "))
        amount = int(input("Quantidade > "))
        category = int(input("ID da Categoria > "))
        provider = int(input("CNPJ do Fornecedor > "))

        product = Product.create(
            id=id,
            price=price,
            name=name,
            category_id=category,
            provider_id=provider,
            amount=amount
        )

        return "Produto {name} com ID {id} criado com sucesso.".format(
            id=id,
            name=name
        )
    elif option == 2:
        product = Product.get(id=id)

        return "O produto {id} está cadastrado com nome {name}.".format(
            id=id,
            name=Product.name
        )
    elif option == 3:
        price = int(input("Novo preço > "))
        amount = int(input("Nova quantidade > "))

        product = Product.get(id=id)

        product.price = price
        product.amount = amount

        product.save()

        return "O produto {id} teve o seu preço e quantidade alteradas.".format(
            id=id
        )
        
    else:
        product = Product.get(Employeer.id == id)
        product.delete_instance()

        return "{name} já não existe.".format(
            name=Product.name
        )

def handle_cart(option: int):
    if option > 4 or option < 1: return ""

    id = int(input("ID > "))

    if option == 1: 
        cpf = input("CPF do cliente > ")
        payment_type = input("Método de pagamento (CRÉDITO | DÉBITO | DINHEIRO) > ").upper()

        products = []
        total = 0

        while True:
            product = int(input("ID do Produto (-1 para parar) > "))

            if product < 0: break

            data = Product.get(id=product)

            if data.amount == 0:
                print("Produto fora de estoque, ignorando...")
            else:
                data.amount -= 1
                data.save()

                products.append(product)

                total += data.price

        cart = Cart.create(
            id=id,
            owner=cpf,
            total=total,
            payment_type=payment_type
        )

        return "Compras salvas com sucesso."
        
    elif option == 2:
        cart = Cart.get(id=id)

        return "O produto {id} está cadastrado com total de {total} e forma de pagamento em {pt}.".format(
            id=id,
            total=cart.total,
            pt=cart.payment_type
        )
    elif option == 3:
        return "Operação não suportada."
        
    else:
        cart = Cart.get(Employeer.id == id)
        cart.delete_instance()

        return "{name} já não existe.".format(
            name=Cart.name
        )