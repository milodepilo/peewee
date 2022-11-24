import models

def populate_test_DB(models):
    models.db.connect()
    models.db.create_tables(
        {
            models.Tag,
            models.Product,
            models.User,
            models.BillingInfo,
            models.Transaction            
        }
    )


    product_data=(
        ("productname", "bla", 1500, 1, ["tag_name"]),

    )
    for product_name, description, price, stock, tags in           product_data:
        product = models.Product.create(
            name=product_name,
            description=description,
            price=price,
            stock=stock
            )
        for tag_name in tags:
            tag = models.Tag.create(name="tag_name")


    user_data = (
        ("name", "adress",["product name"]),
    )
    for name, adress, products in user_data:
        user = models.User.create(name=name, adress=adress)
        for product in products:
            models.Product.create(name=product)
