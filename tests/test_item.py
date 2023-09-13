"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def smartphone():
    return Item("Смартфон", 10000, 20)


def test_calculate_t_price(smartphone):
    assert smartphone.calculate_total_price() == 200000


def test_apply_discount(smartphone):
    assert smartphone.pay_rate == 1.0
    assert smartphone.apply_discount() is None
    assert smartphone.price == 10000
