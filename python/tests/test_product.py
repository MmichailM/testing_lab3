import pytest

from python.src.Product import Product


@pytest.mark.parametrize(
    "id, name, price, stock",
    [
        ("prod_102", "Смартфон", 18000, 15),
        ("prod_110", "Ноутбук", 77000, 4),
        ("prod_111", "Монитор", 22000, 10)
    ]
)
def test_constructor(id, name, price, stock):
    product = Product(id, name, price, stock)

    assert product.id == id
    assert product.name == name
    assert product.price == price
    assert product.stock == stock

@pytest.mark.parametrize(
    "price",
    [-1000.0, -1.0, 0.0]
)
def test_impossible_price(price):
    with pytest.raises(ValueError):
        Product("id", "name", price, 10)

@pytest.mark.parametrize(
    "stock",
    [-10, -5, -1]
)
def test_impossible_stock(stock):
    with pytest.raises(ValueError):
        Product("id", "name", 15000, stock)

def test_zero_stock():
    product = Product("id", "name", 15000, 0)

    assert product.id == "id"
    assert product.name == "name"
    assert product.price == 15000
    assert product.stock == 0