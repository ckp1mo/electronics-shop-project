"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def cvs_file():
    return 'src/items.csv'


@pytest.fixture
def class_item():
    return Item


@pytest.fixture
def smartphone():
    return Item("iPhone 15", 124990, 20)


def test_calculate_t_price(smartphone):
    assert smartphone.calculate_total_price() == 2499800


def test_apply_discount(smartphone):
    assert smartphone.pay_rate == 1.0
    assert smartphone.apply_discount() is None
    assert smartphone.price == 124990


def test_name(smartphone):
    smartphone.name = 'СуперСмартфон'
    assert smartphone.name == 'СуперСмарт'
    smartphone.name = 'Кофеварка'
    assert smartphone.name == 'Кофеварка'


def test_instantiate_from_csv(cvs_file, class_item):
    class_item.instantiate_from_csv(cvs_file)
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('4.5') == 4
    assert Item.string_to_number('3') == 3


def test_repr(smartphone):
    smartphone.price = 18900
    assert repr(smartphone) == "Item('iPhone 15', 18900, 20)"


def test_str(smartphone):
    assert str(smartphone) == 'iPhone 15'
    smartphone.name = 'iPhone XR'
    assert str(smartphone) == 'iPhone XR'
