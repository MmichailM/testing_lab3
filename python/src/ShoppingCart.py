from python.src.Product import Product


class ShoppingCart:
    def __init__(self):
        self.list = {}

    def add(self, product: Product, count: int):
        if count <= 0:
            raise ValueError("Количество добавляемого товара должно быть положительным")

        current_count = self.list.get(product.id, 0)
        new_count = current_count + count

        if new_count > product.stock:
            raise ValueError("Недостаточно товаров на складе")

        self.list[product.id] += new_count

    def delete(self, product: Product, count: int):
        if count <= 0:
            raise ValueError("Количество удаляемого товара должно быть положительным")

        current_count = self.list.get(product.id, 0)
        new_count = current_count - count

        if new_count < 0:
            raise ValueError("Количество удаляемого товара не должно превышать количество этого товара в корзине")

        if new_count == self.list[product.id]:
            self.list.pop(product.id)

        else:
            self.list[product.id] -= new_count

    def calculate_price(self) -> float:
        sum = 0.0

        for product in self.list:
            sum += self.list[product.id] * product.price

        return sum
