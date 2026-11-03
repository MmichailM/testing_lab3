from python.src.Product import Product


class ShoppingCart:
    PROMO_CODES = {
        "STUDENT": 5,
        "SALE15": 15,
        "SECRETCODE14531861": 27
    }

    def __init__(self):
        self.list = {}
        self.promo_code = None

    def add(self, product: Product, count: int):
        if count <= 0:
            raise ValueError("Количество добавляемого товара должно быть положительным")

        current_count = self.list.get(product, 0)
        new_count = current_count + count

        if new_count > product.stock:
            raise ValueError("Недостаточно товаров на складе")

        self.list[product] = new_count

    def delete(self, product: Product, count: int):
        if count <= 0:
            raise ValueError("Количество удаляемого товара должно быть положительным")

        current_count = self.list.get(product, 0)
        new_count = current_count - count

        if new_count < 0:
            raise ValueError("Количество удаляемого товара не должно превышать количество этого товара в корзине")

        if new_count == 0:
            self.list.pop(product)

        else:
            self.list[product] = new_count

    def apply_promo_code(self, promo: str):
        promo = promo.upper()
        if promo not in self.PROMO_CODES:
            raise ValueError("Недействительный промокод")

        self.promo_code = promo

    def remove_promo_code(self, promo: str):
        self.promo_code = None

    def calculate_price(self) -> float:
        sum = 0.0

        for product in self.list:
            sum += self.list.get(product) * product.price

        if self.promo_code is not None:
            discount = self.PROMO_CODES[self.promo_code]
            sum *= (100 - discount) / 100.0

        return round(sum, 2)

