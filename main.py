__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import Tag, User, Product, Transaction
import models
from populator import populate_test_DB

populate_test_DB(models)

def search(term):
    return Product.select(Product.name).where(Product.name.contains(term))   
    


def list_user_products(user_id):    
    query = (User
        .select(Product.name)
        .where(User.id == user_id))
    for row in query:
        return row.name

def list_products_per_tag(tag_id):
    return (Product
            .select()
            .join(Tag, on=(Product.tag == Tag.id))
            .where(Tag.id == tag_id))

    

def add_product_to_catalog(user_id, product):
    ...


def update_stock(product_id, new_quantity):
    ...


def purchase_product(product_id, buyer_id, quantity):
    ...


def remove_product(product_id):
    ...

print(list_user_products("1"))
print(list_products_per_tag("1"))