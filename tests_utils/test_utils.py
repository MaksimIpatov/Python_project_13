
import pytest

from src.category_1 import Category
from src.product_1 import Product
import pytest


@pytest.fixture
def test_category(test_product):
    return Category('Автотовары', 'Товары для авто', [test_product])
def test_Category(test_category):
    assert test_category.title == 'Автотовары'
    assert test_category.description == 'Товары для авто'
    assert test_category.products == ['Яблоки, 49.99 руб. Остаток: 78 шт.']
    assert Category.number_categories == 1
    assert Category.unique_products == 1


@pytest.fixture
def test_product():
    return Product('Яблоки', 'зеленые', 49.99, 78)
def test_Product(test_product):
    assert test_product.title == 'Яблоки'
    assert test_product.description == 'зеленые'
    assert test_product.price == 49.99
    assert test_product.quantity_in_stock == 78
