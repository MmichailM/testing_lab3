class Product:
    def __init__(self, id: str, name: str, price: float, stock: int):
        if price <= 0:
            raise ValueError("Цена на товар должна быть положительной")

        if stock < 0:
            raise ValueError("Количество товара не должно быть отрицательным")

        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
