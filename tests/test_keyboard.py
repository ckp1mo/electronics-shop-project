from src.keyboard import Keyboard
import pytest


@pytest.fixture
def my_keyboard():
    return Keyboard('HV_KB432L', 3300, 1)


def test_change_lang(my_keyboard):
    assert my_keyboard.language == 'EN'
    my_keyboard.change_lang()
    assert my_keyboard.language == 'RU'
    my_keyboard.change_lang()
    assert my_keyboard.language == 'EN'
    with pytest.raises(AttributeError):
        my_keyboard.language = 'CH'
