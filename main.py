class Product:

    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock

if __name__ == '__main__':
    external_date = {
        "name": "Laptop",          # Anahtar ve değer arasında virgül olmalı
        "price": "9999.99",       # Anahtar ve değer arasında virgül olmalı
        "in_stock": "True"        # Anahtar ve değer arasında virgül olmalı
    }

    product = Product(
        name=external_date.get("name"),
        price=external_date.get("price"),
        in_stock=external_date.get("in_stock") == "True"  # "True" stringini boolean'a çeviriyoruz
    )

    print(product.name)
    print(product.price)