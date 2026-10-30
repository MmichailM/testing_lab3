import pytest

from python.src.Product import Product
from python.src.ShoppingCart import ShoppingCart


def test_constructor():
    shopping_cart = ShoppingCart()

    assert len(shopping_cart.list) == 0

@pytest.mark.parametrize(
    "id, name, price, stock, count",
    [
        ("prod_102", "Смартфон", 18000, 15, 10),
        ("prod_110", "Ноутбук", 77000, 10, 4),
        ("prod_111", "Монитор", 22000, 14, 7)
    ]
)


def test_simple_add(id, name, price, stock, count):
    product = Product(id=id, name=name, price=price, stock=stock)

    shopping_cart = ShoppingCart()
    shopping_cart.add(product, count)

    assert len(shopping_cart.list) == 1
    assert shopping_cart.list.get(product) == count

@pytest.mark.parametrize(
    "id, name, price, stock, count1, count2",
    [
        ("prod_102", "Смартфон", 18000, 15, 10, 3),
        ("prod_110", "Ноутбук", 77000, 10, 4, 6),
        ("prod_111", "Монитор", 22000, 14, 7, 3)
    ]
)
def test_add_to_existed(id, name, price, stock, count1, count2):
    product = Product(id=id, name=name, price=price, stock=stock)

    shopping_cart = ShoppingCart()
    shopping_cart.add(product, count1)
    shopping_cart.add(product, count2)

    assert len(shopping_cart.list) == 1
    assert shopping_cart.list.get(product) == count1 + count2

@pytest.mark.parametrize(
    "count",
    [-10, -2, -1, 0]
)
def test_add_impossible(count):
    product = Product("id", "name", 15000, 3)
    shopping_cart = ShoppingCart()
    with pytest.raises(ValueError):
        shopping_cart.add(product, count)

@pytest.mark.parametrize(
    "id, name, price, stock, count",
    [
        ("prod_102", "Смартфон", 18000, 15, 16),
        ("prod_110", "Ноутбук", 77000, 10, 11),
        ("prod_111", "Монитор", 22000, 14, 17)
    ]
)
def test_add_more_then_have(id, name, price, stock, count):
    product = Product(id=id, name=name, price=price, stock=stock)

    shopping_cart = ShoppingCart()
    with pytest.raises(ValueError):
        shopping_cart.add(product, count)


@pytest.mark.parametrize(
    "id, name, price, stock, count_add, count_delete",
    [
        ("prod_102", "Смартфон", 18000, 15, 4, 3),
        ("prod_110", "Ноутбук", 77000, 10, 7, 2),
        ("prod_111", "Монитор", 22000, 14, 5, 3)
    ]
)
def test_simple_delete(id, name, price, stock, count_add, count_delete):
    product = Product(id=id, name=name, price=price, stock=stock)

    shopping_cart = ShoppingCart()
    shopping_cart.add(product, count_add)
    shopping_cart.delete(product, count_delete)

    assert len(shopping_cart.list) == 1
    assert shopping_cart.list.get(product) == count_add - count_delete

@pytest.mark.parametrize(
    "id, name, price, stock, count_add, count_delete",
    [
        ("prod_102", "Смартфон", 18000, 15, 4, 4),
        ("prod_110", "Ноутбук", 77000, 10, 7, 7),
        ("prod_111", "Монитор", 22000, 14, 5, 5)
    ]
)
def test_delete_all(id, name, price, stock, count_add, count_delete):
    product = Product(id=id, name=name, price=price, stock=stock)

    shopping_cart = ShoppingCart()
    shopping_cart.add(product, count_add)
    shopping_cart.delete(product, count_delete)

    assert len(shopping_cart.list) == 0
    assert shopping_cart.list.get(product, 0) == 0
    
@pytest.mark.parametrize(
    "count",
    [-10, -2, -1, 0]
)
def test_delete_impossible(count):
    product = Product("id", "name", 15000, 13)
    
    shopping_cart = ShoppingCart()
    shopping_cart.add(product, 10)
    with pytest.raises(ValueError):
        shopping_cart.delete(product, count)

@pytest.mark.parametrize(
    "id, name, price, stock, count",
    [
        ("prod_102", "Смартфон", 18000, 15, 4),
        ("prod_110", "Ноутбук", 77000, 10, 7),
        ("prod_111", "Монитор", 22000, 14, 5)
    ]
)
def test_delete_more_then_have(id, name, price, stock, count):
    product = Product(id=id, name=name, price=price, stock=stock)

    shopping_cart = ShoppingCart()
    shopping_cart.add(product, count)
    with pytest.raises(ValueError):
        shopping_cart.delete(product, count + 1)



@pytest.mark.parametrize(
    "products",
    [
        [
            (Product("prod_102", "Смартфон", 18000, 15), 4),
            (Product("prod_110", "Ноутбук", 77000, 10), 7),
            (Product("prod_113", "Компьютерная мышь", 3500, 16), 3),
        ],
        [
            (Product("prod_111", "Монитор", 22000, 14), 5),
            (Product("prod_112", "Клавиатура", 3000, 20), 2),
            (Product("prod_114", "Процессор", 15000, 4), 2)
        ]
    ]
)
def test_calculate_price(products):
    shopping_cart = ShoppingCart()

    sum = 0

    for product, count in products:
        shopping_cart.add(product, count)
        sum += product.price * count

    assert shopping_cart.calculate_price() == sum