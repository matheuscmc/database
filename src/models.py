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
    cnpj = IntegerField()
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
    provider = ForeignKeyField(Provider, field='cnpj')
    price    = IntegerField()
    amount   = IntegerField()
    
    class Meta:
        database = db

class Cart(Model):
    id           = IntegerField(primary_key=True)
    owner        = ForeignKeyField(Customer, field='cpf')
    total        = IntegerField()
    payment_type = CharField(max_length=32)

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
        Cart
    ])

    print('Tables created.')