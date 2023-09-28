import pytest

from src.phone import Phone


@pytest.fixture
def iphone():
    return Phone('iPhone XR', 32000, 15, 1)


def test_repr(iphone):
    assert repr(iphone) == "Phone('iPhone XR', 32000, 15, 1)"


def test_number_of_sim(iphone):
    with pytest.raises(ValueError):
        Phone('iPhone XR', 32000, 15, 0)
    with pytest.raises(ValueError):
        iphone.number_of_sim = 0
    iphone.number_of_sim = 2


