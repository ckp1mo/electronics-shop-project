from src.item import Item


class MixinLang:
    """
    Этот миксин хранит и меняет раскладку клавиатуры с EN на RU.
    По умолчанию стоит язык EN.
    """

    def __init__(self, language='EN'):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(Item, MixinLang):
    pass
