from peewee import Model,CharField,AutoField,ForeignKeyField,TextField,IntegerField,SqliteDatabase

db = SqliteDatabase("betsy.db")

class BaseModel(Model):
    class Meta:
        database = db


class Tag(BaseModel):
    name = CharField()


class Product(BaseModel):       
    name = CharField()
    description = TextField()
    price = IntegerField()
    stock = IntegerField()
    tag = ForeignKeyField(Tag)


class User(BaseModel):    
    name = CharField()
    adress = CharField()
    products = ForeignKeyField(Product)  
    
    
class BillingInfo(BaseModel):
    user = ForeignKeyField(User, backref='BillingInfo')
    info = TextField()    


class Transaction(BaseModel):    
    from_seller = ForeignKeyField(User, backref="Sold")
    to_buyer = ForeignKeyField(User, backref='Bought')
    product = ForeignKeyField(Product)
    ammount = IntegerField()
    
    class Meta:
        indexes =(
            (("from_seller", "to_buyer"), True),
        )


