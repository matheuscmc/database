from peewee import *
from playhouse.db_url import connect

db = connect('mysql://root:@localhost:3306/pyshop')

class Employeer(Model):
    cpf  = IntegerField(primary_key=True)
    name = CharField()
    role = CharField()

    class Meta:
        database = db

class Customer(Model):
    cpf  = IntegerField(primary_key=True)
    name = CharField()

    class Meta:
        database = db

class Provider(Model):
    id   = IntegerField(primary_key=True)
    name = CharField()

    class Meta:
        database = db

class Category(Model):
    id   = IntegerField(primary_key=True)
    name = CharField()

    class Meta:
        database = db

class Product(Model):
    id       = IntegerField(primary_key=True)
    name     = CharField()
    category = ForeignKeyField(Category, field='id')
    provider = ForeignKeyField(Provider, field='id')
    price    = IntegerField()
    
    class Meta:
        database = db

class Cart(Model):
    id           = IntegerField(primary_key=True)
    owner        = ForeignKeyField(Customer, field='cpf')
    total        = IntegerField()
    created_at   = DateTimeField()
    payment_type = CharField(max_length=32)

    class Meta:
        database = db

class CartProduct(Model):
    cart_id    = ForeignKeyField(Cart, field='id')
    product_id = ForeignKeyField(Product, field='id')

    class Meta:
        database = db

def init():
    print('Creating tables...')

    db.create_tables([
        Employeer, 
        Customer,
        Provider,
        Category,
        Product,
        Cart,
        CartProduct
    ])

    print('Tables created.')